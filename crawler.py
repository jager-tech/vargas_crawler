import threading
import requests
from bs4 import BeautifulSoup
from io import StringIO # python3; python2: BytesIO
import boto3
from src.parsers import parser
import pandas as pd
from datetime import date

max_pages = 20
properties = []
remainingPages = True
main_page = 'http://www.vargasinmobiliaria.com.uy'

PREFIX = 'vargas_data'
BUCKET = 'jager-raw-data'


def getPage(page):
    url = f'{main_page}/propiedades/Alquiler/U$S/Sin_precio_m%C3%ADnimo/Sin_precio_m%C3%A1ximo/Todos_los_tipos/Todas_las_zonas/P%C3%A1gina-{page}'
    print('Getting page: ' + str(page))
    response = requests.get(url)
    if response.status_code < 400:
        plain_txt = response.text
        soup = BeautifulSoup(plain_txt, 'html5lib')
        properties.extend(parser.parse(soup))
    else:
        print("Got to the end")


def store_data(properties):
    properties_df = pd.DataFrame(properties)
    s3_client = boto3.client('s3', aws_access_key_id='AKIATJRLJTQ2EUZWKMDR', aws_secret_access_key='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')
    full_prefix = get_s3_full_file_path()
    copy_to_s3(s3_client, properties_df, BUCKET, f'{full_prefix}/vargas_data.csv')
    store_complete(s3_client, BUCKET, full_prefix)


def get_s3_full_file_path():
    today_split = str(date.today()).split('-')
    year = today_split[0]
    month = today_split[1]
    day = today_split[2]
    return f'{PREFIX}/{year}/{month}/{day}'


def copy_to_s3(client, df, bucket, filepath):
    csv_buf = StringIO()
    df.to_csv(csv_buf, header=True, index=False)
    csv_buf.seek(0)
    client.put_object(Bucket=bucket, Body=csv_buf.getvalue(), Key=filepath)
    print(f'Copy {df.shape[0]} rows to S3 Bucket {bucket} at {filepath}, Done!')


def store_complete(client, bucket, filepath):
    client.put_object(Bucket=bucket, Key=f'{filepath}/COMPLETE')


def main():
    page = 1
    print(f'Getting {max_pages} pages from Vargas')
    while page <= max_pages and remainingPages:
        threading.Thread(target=getPage(page)).start()
        page += 1
    print(f'Se obtuvieron {len(properties)} propiedades')
    store_data(properties)

if __name__ == '__main__':
    main()
