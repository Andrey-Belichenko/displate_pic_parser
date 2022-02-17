from bs4 import BeautifulSoup
import requests

url = ""
print("ENTER YOUR URL FROM displate.com")
url = str(input(""))


page = requests.get(url)

if page.status_code != 200:
    print("Connection error")
    quit()

print("Getting page")

soup = BeautifulSoup(page.text, "html.parser")

scripts = soup.findAll("script", type="application/ld+json")

script = scripts[1]

script_string = str(script)

print("Extracting link to img")

img_url_start_index = script_string.find("image") + 9

script_string = script_string[img_url_start_index:]

img_url = script_string[:script_string.find('"')]

print("IMG URL:")

print(img_url)

print("Saving")

p = requests.get(img_url)

index = img_url.rindex("/")

save_name = img_url[index:]

print("Save as "+save_name)

out = open("out_img"+save_name, "wb")

out.write(p.content)

out.close()
