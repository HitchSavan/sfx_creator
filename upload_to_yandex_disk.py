import os
import yadisk
import json
import sys
from datetime import date
from create_sfx import create_sfx


def upload_to_disk(token):
    y = yadisk.YaDisk(token=token)
    if y.check_token():
        print('Token is correct, uploading')
    else:
        print("Token is incorrect, can't upload")
        sys.exit(3)

    for file in os.listdir():
        if file.endswith('.exe'):
            presentation_name = file

    td = date.today().strftime("%d_%m_%Y")

    folder_name = '/presentations/'
    try:
        y.mkdir(folder_name)
    except yadisk.exceptions.DirectoryExistsError:
        pass

    folder_name += td
    try:
        y.mkdir(folder_name)
    except yadisk.exceptions.DirectoryExistsError:
        pass

    print(f'Uploading {presentation_name}')
    y.upload(presentation_name, f"{folder_name}/{presentation_name}")
    print('Upload complete')

if __name__ == '__main__':
    with open('settings.json', encoding='utf-8') as json_file:
        settings = json.load(json_file)
    
    try:
        presentation_folder_path = sys.argv[1]
    except:
        print(f'usage: upload_to_yandex_disk.py <input build folder>')
        sys.exit(2)

    create_sfx(presentation_folder_path)

    upload_to_disk(settings["token"])