import csv
import gzip
import os

from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = 'this command will download a source archive, extract it and populate items into the database'
    
    def __init__(self):
        self.source = 'http://download.db-ip.com/free/dbip-city-2017-08.csv.gz'
         
        # How to use my google drive direct download link
#         self.source = 'https://drive.google.com/uc?export=download&id=0B3U2lEjglUqHOHYzX1ZOWlNOeDg'

    def downloadContent(self):
        try:
            file_data = requests.get(self.source, stream=True) # we send request of url self.source for file downloading(stream=True)
            file_data_size = int(file_data.headers['Content-Length']) # we get full size of download content
            download_size = 0 #we set counter of download_size content
            if file_data.status_code == 200:#if request had been successfully passed>> 
                 
                #this is how I handle string of link to get name of my file to download
                # file_name = file_for_down.headers['Content-Disposition'].split(';')[1].split('=')[1]
                 
                file_name = '{}'.format(self.source.strip().split('/')[-1])# than get me a file_name from url
                with open(file_name, 'wb') as file2save: # prepare file for saving in form of binary data
                    for chunk in file_data.iter_content(chunk_size = 1024): # we iterate through requested download data 
                        if chunk:# if chunk exist
                            download_size += len(chunk) # add to dowload_size length of current chunk
                            print('\r{:.02f} %'. format((download_size/file_data_size)*100),end='')# proces for getting percents of download data
                            file2save.write(chunk) # write chunk on HDD chunk by chunk
                    print('DOWNLOAD DONE :D')
                return file_name # return file_name for using in handle method
            else:
                print("Request code of download process is {} for requested url {}".format(file_data.status_code, self.source))
        except Exception as e:
            self.exception(str(e))
        return None
                            
    
    
    def handle(self, **args):
        # try to open the csv file
        csv_file = os.path.split(self.source )[-1].strip('.gz')
        if not os.path.isfile(csv_file):
            # try to open the archive
            filename = os.path.split(self.source )[-1]
            if not os.path.isfile(filename): 
                # download archive file from it's source
                filename = self.downloadContent()
             
            with gzip.open(filename, 'rb') as gz:
                with open(filename.strip('.gz'), 'wb') as csvf:
                    csvf.write(gz.read())
         
        csvf = csv.reader(open(csv_file))
        counter = 0
        for row in csvf:
            print(row)
            if counter > 20:
                break
            counter += 1
            
    