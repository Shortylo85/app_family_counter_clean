from django.conf import settings
from django.core.management.base import BaseCommand
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class Command(BaseCommand):
    help = 'this command will download a source archive, extract it and populate items into the database'
    
    def __init__(self):
        # How to use my google drive direct download link
        self.source = 'https://drive.google.com/uc?export=download&id=0B3U2lEjglUqHOHYzX1ZOWlNOeDg'
        
        # get google drive authorization
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(settings.BASE_DIR + "/../credentials.txt")
        if gauth.credentials is None:
            gauth.CommandLineAuth()
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
 
        gauth.SaveCredentialsFile(settings.BASE_DIR + "/../credentials.txt")

        # initialize google drive
        self.drive = GoogleDrive(gauth)

    def handle(self, **args):
        # Auto-iterate through all files in the root folder.
        
        file_list = self.drive.ListFile({'q': "'0B3U2lEjglUqHdzdyU2xybGh3aFE' in parents and trashed=false"}).GetList()
        for file1 in file_list:
            print('title: %s, id: %s' % (file1['title'], file1['id']))
            
        file_for_download = self.drive.CreateFile({'id': '0B3U2lEjglUqHbkltX1hwR3hzRXc'})
        print('Please wait until the download is complete...')
        file_for_download.GetContentFile(file_for_download['title'])
        print('Download complete, thank you for waiting...')