"""
Takes a text file of terms, breaks them down into key terms and returns search results of key terms.
Brett Hobbs
Oct. 2022
Help from:
https://hackernoon.com/how-to-use-google-trends-api-with-python

TODO:
plot or rank the data in some manner
display said ranking on a plot
"""

from pytrends.request import TrendReq
from datetime import datetime
import plotly.express as p

#Reads the terms from a text file
f = open("terms.txt", "r")
#Splits each term into an array
term_array = []# List of keywords to be searched 

for term in f:#Gets a keyword per line of text file
    term_array.append(term.strip("\n"))
f.close()
#Gets the current date to be plugged into the data
date = datetime.today().strftime('%Y%m%d')
year = date[:4]
month = date[4:6]
day = date[6:]
#feeds the array into google trends and gets todays search amounts
pytrend = TrendReq()
data = pytrend.get_historical_interest(term_array,
                                       year_start=int(year),
                                       month_start=int(month),
                                       day_start=int(day),
                                       hour_start=0,

                                       year_end=int(year),
                                       month_end=int(month),
                                       day_end=int(day),
                                       hour_end=23,

                                       sleep=60)  # Delay added for rate limit

figure = p.line(data, x=['youtube'], y=['machine learning'], title='Keyword Web Search Interest Over Time')
figure.show()

#Returns the data and does stuff with it
#print(data)