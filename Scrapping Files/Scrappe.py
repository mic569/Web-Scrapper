
#Importation from Libraries and Decleration
import bs4
import random
from urllib import urlopen as uRequest
from bs4 import BeautifulSoup as Soup
#Establishing Connection

urls = 'https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptop'
client = uRequest(urls)
htmlp=client.read()

#Parsing Page
sp = Soup(htmlp,"html.parser")

#Grabs each product
container = sp.findAll("div",{"class":"item-container"})

filename = "laps.csv"
fi = open(filename, "w")

headers = "brand, product_name, shipping"

fi.write(headers)

for con in container:
	the_brand = con.img["title"]

titles = con.findAll("a",{"class":"item-title"})
brand_names = titles[0].text

ship_cons = con.findAll("li", {"class" :"price-ship"})
shipping_cons =ship_cons[0].text.strip()

print("Brand: " + the_brand)
print("Product Name: " + brand_names)
print("Shipping: " + shipping_cons)

fi.write(the_brand + "," + brand_names.replace(","," ") + "," + shipping_cons + "\n")
fi.close()