from bs4 import BeautifulSoup
import urllib2
import requests
from tqdm import tqdm

for team in tqdm(range(0, 255)):
    site = "https://www.thebluealliance.com/team/" + str(team)

    hdr = {'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

    req = urllib2.Request(site, headers=hdr)

    try:
        page = urllib2.urlopen(req)

        soup = BeautifulSoup(page, 'html.parser')

        images = soup.find(id="robot-image").find_all(class_="item")

        for i in range(0, len(images)):
            style = images[i].find("span")["style"]
            
            image_url = style[22:len(style)-2]
            img_data = requests.get(image_url).content

            file_location = "./outputs/" + str(team) + "_" + str(i) + ".jpg"

            with open(file_location, 'wb') as handler:
                handler.write(img_data)

    except urllib2.HTTPError, e:\
        pass

    