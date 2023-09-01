import os
import sys

def create_sfx(presentation_folder_path):
    for file in os.listdir(presentation_folder_path):
        if file.endswith('.exe'):
            presentation_name = file

    archive_name = os.path.split(presentation_folder_path)[-1]

    if os.path.exists(f'{presentation_folder_path}\\windeployqt'):
        create_archive_command = f'7z a -t7z {archive_name}.7z -m0=lzma2 -mx=9 -aoa {presentation_folder_path}\\*.exe {presentation_folder_path}\\windeployqt\\* {presentation_folder_path}\\data {presentation_folder_path}\\..\\presentation_tool\\hotkeys.txt {presentation_folder_path}\\model.configuration'
    else:
        create_archive_command = f'7z a -t7z {archive_name}.7z -m0=lzma2 -mx=9 -aoa {presentation_folder_path}\\*.exe {presentation_folder_path}\\styles {presentation_folder_path}\\platforms {presentation_folder_path}\\imageformats {presentation_folder_path}\\*.dll {presentation_folder_path}\\data {presentation_folder_path}\\..\\presentation_tool\\hotkeys.txt {presentation_folder_path}\\model.configuration'

    print(create_archive_command)

    config = f';!@Install@!UTF-8!\nRunProgram="{presentation_name}"\nGUIMode="2"\n;!@InstallEnd@!'

    for file in os.listdir(os.path.dirname(__file__)):
        if file.endswith('.sfx'):
            zip_module = file

    create_sfx_command = f'COPY /b {zip_module} + config.txt + {archive_name}.7z {presentation_name}'

    with open(f'config.txt', 'w') as f:
        f.write(config)

    os.system(create_archive_command)
    os.system(create_sfx_command)

    os.remove(f'{archive_name}.7z')

if __name__=='__main__':
    try:
        presentation_folder_path = sys.argv[1]
    except:
        print(f'usage: create_sfx.py <input build folder>')
        sys.exit(2)

    create_sfx(presentation_folder_path)