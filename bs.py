import re
import urllib.request as ur
from bs4 import BeautifulSoup
import data

html = ur.urlopen("http://sophist.hse.ru/exes/tables/CPI_Y_CHI.htm").read().decode("cp1251")
soup = BeautifulSoup(html, "html.parser")

nums = soup.findAll("font", string=re.compile("\d+\,\d+"))
years = soup.findAll("font", string=re.compile("\d\d\d\d"))
for i in range(len(nums)):
    nums[i] = nums[i].getText()
    
for i in range(len(years)):
    years[i] = years[i].getText()

x = []

for i in range(len(nums)):
    if int(years[i]) >= 2000 and int(years[i]) <= 2018:
        x.append(float(nums[i].replace(",", ".")))
        
d = data.Data(x)
print(d)