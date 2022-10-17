"""
Takes a text file of terms, breaks them down into key terms and returns search results of key terms.
Brett Hobbs
Oct. 2022
Help from:
https://hackernoon.com/how-to-use-google-trends-api-with-python

TODO:
Fix getting data from google
print out and plot said data
clean up function
"""

from pytrends.request import TrendReq

#Reads the terms from a text file
f = open("terms.txt", "r")
#Splits each term into an array
term_array = []# List of keywords to be searched

for term in f:#Gets a keyword per line of text file
    term_array.append(term.strip("\n"))
f.close()
print(term_array)
#feeds the array into google trends
pytrends = TrendReq(hl = 'en-US', tz = 360)
data = pytrends.interest_over_time(term_array)

#Returns the data and does stuff with it
print(data)