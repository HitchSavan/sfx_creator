
Tool for SFX packing and automatic uploading to yandex disk.

### Settings JSON example

{
    "token": "", // yandex disk token
    "default_folder": "/folder_structure", // target folder in ya.disk (upload destination)
    "include_files": [ // files to upload
        "\\file.one",
        "\\file.two"
    ],
    "additional_files": [ // files to upload
        "\\file.img",
        "\\folder"
    ]
}
