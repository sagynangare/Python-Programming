import random
import urllib

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=2&e=8&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv'

def download_image(url):
    name = random.randrange(1,100)
    full_name = str(name) + ".jpg"
    urllib.urlretrieve(url,full_name)


def download_file(csv_url):
    response = urllib.urlopen(csv_url)
    csv = response.read()
    csv_url =str(csv)
    lines = csv_url.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

    
download_file(goog_url)







    
#download_image("https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSGCUd1juB7U5V6GyaLU8-zwBKd-uW6w442iBc2-ZRrSb1HaBlPajufOGs")
