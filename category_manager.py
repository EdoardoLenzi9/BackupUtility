import glob, os, time
import localizations as loc, file_manager as fm

# App folder
# Foreach file check if there is any backup in the destination folder and copy if not

def scan_app():
    os.chdir("{0}{1}".format(loc.source_dir, loc.download_dir))
    for file_name in glob.glob("*"):
        filename, file_extension = os.path.splitext(file_name) #get file extension
        
        if file_extension == ".iso": 
            fm.copy("{0}{1}{2}".format(loc.source_dir, loc.download_dir, file_name), "{0}{1}{2}".format(loc.destination_dir, loc.deb_dir, file_name))
        
        #print(file_name)
        #print(time.ctime(os.path.getmtime(file_name)))
        #print(os.stat(file_name).st_size)


# Download folder
# Cut .iso and .deb file,
# foreach other file check if there is any backup in the destination folder and copy if not

def scan_download():
    os.chdir("{0}{1}".format(loc.source_dir, loc.download_dir))
    for file_name in glob.glob("*"):
        filename, file_extension = os.path.splitext(file_name) #get file extension
        
        if file_extension == ".iso":
            fm.cut("{0}{1}{2}".format(loc.source_dir, loc.download_dir, file_name), "{0}{1}".format(loc.destination_dir, loc.iso_dir))
        if file_extension == ".deb":  
            fm.cut("{0}{1}{2}".format(loc.source_dir, loc.download_dir, file_name), "{0}{1}".format(loc.destination_dir, loc.deb_dir))
        if file_extension == ".sh":  
            fm.copy("{0}{1}{2}".format(loc.source_dir, loc.download_dir, file_name), "{0}{1}".format(loc.destination_dir, loc.deb_dir))
        
        #print(file_name)
        #print(time.ctime(os.path.getmtime(file_name)))
        #print(os.stat(file_name).st_size)

# Folder        Syncronized
# App               []   
# Code              [X]
# Desktop           []
# Documents         [X]
# Downloaded        []
# Downloads         [X]
# Games             []
# Ideas             [X]
# Music             [X]
# Pictures          [X]
# Videos            [X]