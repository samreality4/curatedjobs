import requests
from bs4 import BeautifulSoup
import json

indeed = requests.get(
    "https://www.indeed.com/jobs?q=javascript&l=rosemead&radius=50&sort=date"
)

print(indeed)

def scrapeIndeed():
    soup = BeautifulSoup(indeed.text, "html.parser")
    jobs = json.loads(soup.find("script", type="text/javascript").string)
    print(jobs)

scrapeIndeed()



