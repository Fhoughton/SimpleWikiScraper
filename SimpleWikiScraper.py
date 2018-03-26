from urllib.request import urlopen
from bs4 import BeautifulSoup

func = lambda s: s[:1].upper() + s[1:] if s else ''

wiki="https://en.wikipedia.org/wiki/" + func(str(input("Enter then name of the article to scrape (e.g Whistling duck)\n").replace(" ","_")))
page = urlopen(wiki)
soup = BeautifulSoup(page, "lxml")
wordList=[]

title=soup.title.string.replace(" - Wikipedia","")

all_links=soup.find_all("a")
for link in all_links:
    wordList.append(link.get("href"))
    
images=soup.find_all("img")

hyperlinkcount=len(wordList)-63
imagecount=len(images)-4



print("Page Title: " + title, "\nHyperlink Count: " + str(hyperlinkcount), "\nImage Count: " + str(imagecount))