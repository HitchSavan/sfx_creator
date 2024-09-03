import os
import sys
import json

def create_sfx(settings, source_folder_path, ignored=[]):
    executable_name = ''
    for file in os.listdir(source_folder_path):
        if file.endswith('.exe'):
            executable_name = file

    archive_name = os.path.split(source_folder_path)[-1]

    create_archive_command = f'7z a -t7z {archive_name}.7z -m0=lzma2 -mx=9 -aoa'

    if settings:
        for item in settings["include_files"]:
            create_archive_command += f' {source_folder_path}{item}'
        else:
            if "additional_files" in settings.keys():
                for item in settings["additional_files"]:
                    create_archive_command += f' {source_folder_path}{item}'
    else:
        create_archive_command += f' {source_folder_path}\\*'


    if executable_name:
        config = f';!@Install@!UTF-8!\nInstallPath="{executable_name[:-4]}"\nRunProgram="{executable_name}"\nGUIMode="2"\n;!@InstallEnd@!'
    else:
        config = f';!@Install@!UTF-8!\nInstallPath="{archive_name}"\nGUIMode="2"\n;!@InstallEnd@!'
        executable_name = f'{archive_name}.exe'

    for file in os.listdir(os.path.dirname(__file__)):
        if file.endswith('.sfx'):
            zip_module = file

    create_sfx_command = f'COPY /b {zip_module} + config.txt + {archive_name}.7z {executable_name}'

    with open(f'config.txt', 'w') as f:
        f.write(config)


    print(create_archive_command)
    os.system(create_archive_command)
    print('---------------')
    print(create_sfx_command)
    os.system(create_sfx_command)

    os.remove(f'{archive_name}.7z')

if __name__=='__main__':
    try:
        source_folder_path = sys.argv[1]
    except IndexError:
        print(f'Not Enough Arguments:')
        print(f'\tusage: create_sfx.py <input source folder>')
        sys.exit(2)
        
    with open('settings.json', encoding='utf-8') as json_file:
        settings = json.load(json_file)

    ignored = []

    create_sfx(settings, source_folder_path, ignored)