import csv
import os

from django.core.management.base import BaseCommand
from ui.models import City


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'


    def handle(self, **args):
        print("Start")
        
        # Direct download file from google drive 
# 'https://drive.google.com/uc?export=download&id=0B3U2lEjglUqHOHYzX1ZOWlNOeDg'
        
#         directory = "/home/danijel/WORKSPACE/my_projects/app_family_counter"       
#         locations = open(os.path.join(directory, 'city_data.csv'))
#         
        directory = "/home/danijel/Downloads/csv_files/family_counter/GeoLite2-City-CSV_20170801"
        locations = open(os.path.join(directory, 'city_data.csv'))  
#         locations = open(os.path.join(directory, 'GeoLiteCity-Location.csv'))
        
        csv_file = csv.reader(locations)
        
        counter = 0
        
        for row in csv_file:
            city = City()
#             data = {
#                'city_name': row[3],
#                 'lat': row[5],
#                 'lng': row[6],
#             }
            city.country = row[1]
            city.city_name = row[3]
            city.lat = row[5]
            city.lng = row[6]
            
            city.save()
            
            print("imported \r{:.02f} %".format((counter/2000)*100), end='')
            
            if counter > 2000:
                break
                print("Import is complete")
                
            counter += 1