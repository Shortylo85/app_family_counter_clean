import csv
import os

from django.core.management.base import BaseCommand
from ui.models import City
from urllib import request


class Command(BaseCommand):
    help = 'This command will download csv file for database'

    def __init__(self):
        # Direct download file from google drive
        self.csv_url = 'https://drive.google.com/uc?export=download&id=0B3U2lEjglUqHbkltX1hwR3hzRXc'


    def downloadCSV(self,url):
        print("Downloading started, please wait...")
        file_response = request.urlopen(url)# open url
        csv_file = file_response.read()# read response of url
        csv_string = str(csv_file) # prepare to string
        lines = csv_string.split('\\n') # break into lines
        file_name = 'city_data.csv' # create destination for file
        file = open(file_name, 'w') # open file_dest for writing a file
        total_lines = len(lines) 
        counter = 0
        for line in lines:
            counter += 1
            print("\r{:.02f} %".format((counter/total_lines)*100), end='')
            file.write(line + '\n')
        print("\nDownload finished, nice work")
        file.close()
        return None

    def handle(self, **args):
        self.downloadCSV(self.csv_url)
        directory = os.getcwd()       
        location = open(os.path.join(directory, 'city_data.csv'))
 
        csv_file = csv.reader(location)

        counter = 0
            
        for row in csv_file:
            city = City()
   
            city.country = row[1]
            city.city_name = row[3]
            city.lat = row[5]
            city.lng = row[6]
                
            city.save()
                
            print("\r{:.02f} % into database imported".format((counter/1000)*100), end='')
                
            if counter > 1000:
                break
                print("Import is complete")
                    
            counter += 1