import os
import zipfile
import requests

url = "https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip"
zip_path = "files.zip"
extract_path = "random_files"

def is_jpeg(file_path):
    with open(file_path, "rb") as f:
        header = f.read(2)
    return header == b'\xff\x8d'

response = requests.get(url)
with open(zip_path, "wb") as f:
    f.write(response.content)

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_path)

for file in os.listdir(extract_path):
    file_path = os.path.join(extract_path, file)
    if os.path.isfile(file_path):
        if is_jpeg(file_path):
            new_file_path = file_path + ".jpg"
            os.rename(file_path, new_file_path)
            print(f'{file} -> {file}.jpg (renamed)')
        else:
            os.remove(file_path)
            print(f'{file} deleted')
