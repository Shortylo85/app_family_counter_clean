from urllib import request

csv_url = 'https://drive.google.com/uc?export=download&id=0B3U2lEjglUqHOHYzX1ZOWlNOeDg'

def downloadCSV(url):
    print("Downloading started, please wait...")
    file_response = request.urlopen(url)# open url
    csv_file = file_response.read()# read response of url
    csv_string = str(csv_file) # prepare to string
    lines = csv_string.split('\\n') # break into lines
    file_dest = r'city_data.csv' # create destination for file
    file = open(file_dest, 'w') # open file_dest for writing a file
    total_lines = len(lines) 
    counter = 0
    for line in lines:
        counter += 1
        print("\r{:.02f} %".format((counter/total_lines)*100), end='')
        file.write(line + '\n')
    print("\nDownload finished, nice work")
    file.close()

downloadCSV(csv_url)
    

    