import os
from pathlib import Path
# this division is to define the file types

foldernames={
    "audio":{'aif','cda','mid','midi','mpa','ogg','wav','wma'},
    "Playlist":{'mp3'},                         #don't worry abt this, add this back to the audio as well
    "compressed":{'7z','deb','pkg','rar','rpm', 'tar.gz','z', 'zip'},
    "code":{'js','jsp','html','ipynb','py','java','css'},
    "documents":{'ppt','pptx','xls', 'xlsx','doc','docx','txt', 'tex', 'epub'},
    "Jee":{'pdf'},                              #hehe edit this out if you and add this to the document if you are using this
    'Images':{'bmp','gif .ico','jpeg','jpg','png','jfif','svg','tif','tiff'},
    'Softwares':{'apk','bat','bin', 'exe','jar','msi','py'},
    'Videos':{'3gp','avi','flv','h264','mkv','mov','mp4','mpg','mpeg','wmv'},
    'Others': {'NONE'} }


#extracting the file ( we will just be separating the last extension of the file)

download_path= r"C:\Users\Admin\Downloads"    #this directory can be different so check fo yourself

onlyfiles = [os.path.join(download_path, file) 
        for file in os.listdir(download_path) 
            if os.path.isfile(os.path.join(download_path, file))]

onlyfolders = [os.path.join(download_path, file) 
        for file in os.listdir(download_path) 
            if not os.path.isfile(os.path.join(download_path, file))]

extension_filetype_map = {extension: fileType 
        for fileType, extensions in foldernames.items() 
                for extension in extensions }

# make folders

folder_paths = [os.path.join(download_path, folder_name) 
        for folder_name in foldernames.keys()]

[os.mkdir(folderPath) 
        for folderPath in folder_paths if not os.path.exists(folderPath)]

# move files
def new_path(old_path):
    extension = str(old_path).split('.')[-1]
    amplified_folder = extension_filetype_map[extension] if extension in extension_filetype_map.keys() else 'Others'
    final_path = os.path.join(download_path,amplified_folder, str(old_path).split('\\')[-1])
    return final_path


[Path(eachfile).rename(new_path(eachfile)) for eachfile in onlyfiles]

# Move other folders
[Path(onlyfolder).rename(os.path.join(download_path,'Others', str(onlyfolder).split('\\')[-1])) 
        for onlyfolder in onlyfolders 
                if str(onlyfolder).split('\\')[-1] not in foldernames.keys()]
