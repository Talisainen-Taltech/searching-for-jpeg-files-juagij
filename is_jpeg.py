import os


def is_jpeg(file_path):
    with open(file_path, 'rb') as file:
        header = file.read(3)
        return header == b'\xFF\xD8'


directory = 'E:\\random_files'

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):
        if is_jpeg(file_path):
            print(f'{file} is JPEG')
        else:
            os.remove(file_path)
            print(f'{file} deleted')
