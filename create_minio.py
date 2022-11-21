from minio import Minio
from minio.error import InvalidResponseError

accessID = 'admin'
accessSecret = 'sample_key'
minioUrl = 'http://localhost:9000'
bucketName = 'mlflow'

minioUrlHostWithPort = minioUrl.split('//')[1]

s3Client = Minio(
    minioUrlHostWithPort,
    access_key=accessID,
    secret_key=accessSecret,
    secure=False
)

s3Client.make_bucket(bucketName)
