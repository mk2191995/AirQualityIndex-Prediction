# Data Collection - Part-1(Predictors)¶

import os
import time
import requests
import sys

#Downloading data from web page: https://en.tutiempo.net/climate/ws-432950.html (For Bangalore)
#as html format
import os
import time
import requests
import sys


def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10):
                url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            else:
                url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')
            
            #Creating path if it doesn't exists
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()

#Main function : for calling :retrive_html       
if __name__=="__main__":
    start_time=time.time() #To Calculate the time taken to retrive data (Start time)
    retrieve_html()  #Function call
    stop_time=time.time() #End time
    print("Time taken {}".format(stop_time-start_time))