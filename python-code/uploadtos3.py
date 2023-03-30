import boto3
import os

s3_client = boto3.client("s3")

def get_jsonfiles(file_path = 'C:/Users/drago/scrapyprojects/news/'):
    all_files = os.listdir(file_path) # get all files in directory
    json_files = [file for file in all_files if file[-5:] == '.json'] #get only json files
    return json_files

def upload_to_s3(file_path = 'C:/Users/drago/scrapyprojects/news/', bucket_name = 'yi-news'):
    for file in get_jsonfiles():
        full_file_path = file_path + file
        s3_client.upload_file(full_file_path, bucket_name, file)

upload_to_s3()