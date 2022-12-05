import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://bootcamp.mapsahr.com/bootcamps/"


response = requests.get(url)


# print(response.status_code)
# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")
dict_camp_data = []

camps_data = soup.find_all("div", class_="course-content-holder")
for item in camps_data:
    dict_camp_data.append({
        "title": item.find("h3").get_text().strip(),
        "description": item.find("div", class_="course-description").get_text().strip(),
        "price":  item.find("bdi").get_text().strip().replace("\xa0", " ")
    })


df = pd.DataFrame(dict_camp_data)
print(df)
df.to_csv("mapsa_data.csv", index=False)
