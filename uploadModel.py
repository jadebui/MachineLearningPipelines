import os
import pandas as pd #Libraries for processing data in python
import numpy as np #Libraries for processing numeric in python
import pickle as pkl #save model and sclaer
import json #read file json
from io import StringIO
from google.cloud import storage
def upload_to_bucket(blob_name, path_to_file, bucket_name):
    """ Upload data to a bucket"""
    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json('ml_gsa.json')
    #print(buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)
    #returns a public url
    return blob.public_url