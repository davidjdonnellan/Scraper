# import libraries
import urllib.request
import urllib.error
import time
from bs4 import BeautifulSoup


def scraper():
##    for x in range(1998,2019):
        scrape_page = "https://www.irishlottery.com/archive-2018"
        page = urllib.request.urlopen(scrape_page).read()
        soup = BeautifulSoup(page, 'html.parser')
        name_box = soup.find('ul', attrs={'class': 'balls'})
        table = soup.find('table',attrs={'class':'table lotto archiveTable'})
##        print(table.text)
        table = table.text.split("\n")
        #splits results into arrays
        newLst = list(table)
        print(newLst)
        newLst = list(table)
        #print(newLst)
        
