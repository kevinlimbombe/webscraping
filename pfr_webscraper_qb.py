import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.pro-football-reference.com/years/2018/passing.htm"
soup = BeautifulSoup(requests.get(url).content, "html.parser")

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow([x.get_text() for x in soup.find("tr").find_all("th")])

    for row in soup.find_all("tr"):
        data = [x.get_text() for x in row.find_all("td")]

        if data: 
            writer.writerow(data)