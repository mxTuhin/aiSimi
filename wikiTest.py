# import wikipedia
# print(wikipedia.summary(wikipedia.search("শেখ মুজিবুর রহমান"), sentences=3))


import re
import requests
from bs4 import BeautifulSoup

url = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles=Albert_Einstein&format=xml'

res = requests.get(url)
soup = BeautifulSoup(res.text, "xml")

birth_re = re.search(r'(Birth date(.*?)}})', soup.revisions.getText())
birth_data = birth_re.group(0).split('|')
birth_year = birth_data[2]
birth_month = birth_data[3]
birth_day = birth_data[4]

death_re = re.search(r'(Death date(.*?)}})', soup.revisions.getText())
death_data = death_re.group(0).split('|')
death_year = death_data[2]
death_month = death_data[3]
death_day = death_data[4]