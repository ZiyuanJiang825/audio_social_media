import boto3
import pandas as pd

df = pd.read_csv('answer_file.csv')
s3 = boto3.client('s3', aws_access_key_id='AKIASA7M4MP6GG7AKC4J', aws_secret_access_key='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')
path = '/Users/ziyuanjiang/Desktop/Graduate Life/2021 Fall/6998BigData/Project/TEDLIUM_release-3/data/sph/'

for i, file in enumerate(df['answerFile']):
    s3.upload_file(path + file, 'acme-answers', df['answerId'][i]+'.sph')

{'Records':
     [{'messageId': '9d73b232-1048-4a31-b6eb-f1ceceaf507b',
       'receiptHandle': 'AQEBxtS604k7H1QzvvcMcWXQnTc/korDyp5CUcrgwIK/9HcIgKSDRd0k6pWR3D5mBwqpvqRqkFK4K7J9hk95w9cIWXN+6rl8yxMFax29ldk+dnjeTbku3mt+Tv8zN1f0u0HoxaLYEeUwN8Ks7+J3p6AQtcs5OAB1XDqPoVeIuK63fIl4o79r1lhjZtdVz+f3+sPHFcP5HvqXvJOs8J0Gy5id5Qc9aV9KKmJKc9jAnlzSdTcXr02X3e4GTmZo6fRyufawgTKbIC5T0f8qAHLoz1ABw6apb0ecebGjFM2laU29cDNv/soEfqkUofZr28FGI5X68vTono+vIzvWufK/ssGW7XbG9BgzDuhExPsPyVmXnxQfl6uHmqR2KtlXTbqZME7w+gMdiPPjtS18IGb5c1vWiQ==',
       'body': 'testtest',
       'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1639967426884', 'SenderId': 'AIDASA7M4MP6I2H2CUXCX', 'ApproximateFirstReceiveTimestamp': '1639967426885'}, 'messageAttributes': {}, 'md5OfBody': '05a671c66aefea124cc08b76ea6d30bb', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-1:139546354684:questions-for-processing', 'awsRegion': 'us-east-1'
       }]}
