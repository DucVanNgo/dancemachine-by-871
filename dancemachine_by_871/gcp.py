from google.cloud import storage
import os
from termcolor import colored

PROJECT_NAME="wagon-data-bootcamp-871"
BASE_URL = "https://storage.googleapis.com"
BUCKETNAME = "dance_871"

def get_urls(input_name):
    # Instantiates a client
    client = storage.Client(project=PROJECT_NAME)
    # Instantiates a bucket
    bucket = client.bucket(BUCKETNAME)

    videos_fine = [filename.name for filename in list(bucket.list_blobs(prefix='cutted/fine/dance_')) if filename == input_name ]

    return videos_fine


#from dancemachine_by_871.params import BUCKET_NAME, MODEL_NAME, MODEL_VERSION
# https://docs.streamlit.io/knowledge-base/tutorials/databases/gcs
### GCP Storage - - - - - - - - - - - - - - - - - - - - - -
BUCKET_NAME = 'wagon-data-871-wanli'
#BUCKET_NAME = 'wagon-data-bootcamp-871'
# model folder name (will contain the folders for all trained model versions)
MODEL_NAME = 'uploaded'

def storage_upload(path,rm=False):
    client = storage.Client().bucket(BUCKET_NAME)
    local_model_name = 'dance1.mp4'
    storage_location = f"vids/{MODEL_NAME}/{local_model_name}"
    blob = client.blob(storage_location)
    blob.upload_from_filename(path)
    print(colored(f"=> video uploaded to bucket {BUCKET_NAME} inside {storage_location}",
                  "green"))
    if rm:
        os.remove(path)
