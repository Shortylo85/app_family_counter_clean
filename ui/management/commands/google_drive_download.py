import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from ui.models import City


class Command(BaseCommand):
    help = 'This command will download data from google drive and populate database'

    def __init__(self):


        gauth = GoogleAuth()
        # Try to load saved client credentials
        gauth.LoadCredentialsFile(settings.BASE_DIR + "/../mycreds.txt")
        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved creds
            gauth.Authorize()
        # Save the current credentials to a file
        gauth.SaveCredentialsFile(settings.BASE_DIR + "/../mycreds.txt")
        
        self.drive = GoogleDrive(gauth)
        
       

    def handle(self,**args):
        print("This actually work")
        
        # Auto-iterate through all files in the root folder.
        file_list = self.drive.ListFile({'q': "'0B3U2lEjglUqHdzdyU2xybGh3aFE' in parents and trashed=false"}).GetList()
        for file1 in file_list:
            print('title: %s, id: %s' % (file1['title'], file1['id']))

            
        csv_file = self.drive.CreateFile({'id': '0B3U2lEjglUqHTWdHVS1TMlRDb2c'})
        print('Please be patient, download is in progress')
        csv_file.GetContentFile(csv_file['title']) # Download file as 'catlove.png'.
        print('Download successfully completed')
        
        directory = os.getcwd()
        name = file1['title']
        
        location = open(os.path.join(directory,name))
        csv_file = csv.reader(location)

        counter = 0
        for row in csv_file:
            city = City()
            city.city_name = row[3]+" "+row[1]+" "+row[4]
            city.lat = row[5]
            city.lng = row[6]
                
            city.save()
            
            print("\r{:.02f} % imported".format((counter/1000)*100), end='')

            if counter > 1000:
                print("\n****Import into database completed****")
                break
 
            counter += 1
            
            