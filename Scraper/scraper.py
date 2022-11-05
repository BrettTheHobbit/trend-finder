'''
Author: B. Hobbs
Date: Nov. 2022
Desc:
'''

from urllib.request import urlopen

#The url that will be scraped
url = "https://www.zillow.com/homes/Kingston,-ON_rb/"

#Opens the url and gets the html code
webPage = urlopen(url)

print(webPage)