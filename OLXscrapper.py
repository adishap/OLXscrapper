#OLX scrapper

#importing modules
import requests
from bs4 import BeautifulSoup
import re
import csv

#definning categories to be searched
categories ={1: 'mobiles-tablets', 2: 'mobile-phones', 3: 'tablets', 4: 'accessories', 5: 'electronics-computers', 
             6: 'computers-laptops-accessories', 7: 'cds-dvds', 8: 'cameras-accessories', 9: 'games-consoles', 
             10: 'tv-video-audio', 11: 'other-electronics', 12: 'vehicles', 13: 'cars', 14: 'motorcycles', 15: 'scooters', 
             16: 'bicycles', 17: 'commercial-vehicles', 18: 'parts-accessories', 19: 'other-vehicles', 20: 'home-furniture', 
             21: 'furniture', 22: 'decor-furnishing', 23: 'fridge-ac-washing-machine', 24: 'home-kitchen-appliances', 
             25: 'paintings-handicrafts', 26: 'other-household-items', 27: 'animals', 28: 'dogs', 29: 'aquariums',
             30: 'birds', 31: 'cats', 32: 'pet-food-accessories', 33: 'other-animals', 34: 'books-sports-hobbies',
             35: 'books-magazines', 36: 'musical-instruments', 37: 'sports-equipment', 38: 'gym-fitness', 
             39: 'coins-collectibles', 40: 'other-hobbies', 41: 'fashion-beauty', 42: 'clothes', 43: 'footwear',
             44: 'jewellery', 45: 'bags-luggage', 46: 'beauty-accessories', 47: 'watches', 48: 'beauty',
             49: 'kids-baby-products', 50: 'strollers', 51: 'kids-furniture', 52: 'car-seats-carriers-rockers', 
             53: 'nutrition', 54: 'clothes-footwear', 55: 'toys-games', 56: 'other-kids-items', 57: 'services',
             58: 'education-classes', 59: 'web-development', 60: 'computer-repair', 61: 'maids-domestic-help', 
             62: 'health-beauty', 63: 'movers-packers', 64: 'drivers-taxi', 65: 'event-services', 66: 'other-services', 67: 'jobs',
             68: 'customer-service', 69: 'it', 70: 'online-part-time', 71: 'marketing', 72: 'advertising-pr', 73: 'sales', 
             74: 'clerical-administration', 75: 'human-resources', 76: 'education', 77: 'hotels-tourism', 78: 'accounting-finance',
             79: 'manufacturing', 80: 'part-time', 81: 'other-jobs', 82: 'real-estate', 83: 'houses', 84: 'apartments', 
             85: 'pg-roommates', 86: 'land-plots', 87: 'commercial-space', 88: 'guest-houses'}

#for selecting one of the categories to search

print("Please select a category to be searched by typing number for a category:")
for key in range( 1 , int(len(categories)),3):
    print(str(key ) + " : " + format(str(categories[key]), " >30s") + "    |     "+ str(key +1 ) + " : " + format(str(categories[key +1]), " >30s") +"    |     "+str(key + 2 ) + " : " + format(str(categories[key+2]), " >30s"))
choice = input()

#for convert choice into int
category = int(choice)

#for definig states
states = {1: 'Andaman & Nicobar Islands', 2: 'Andhra Pradesh', 3: 'Arunachal Pradesh', 4: 'Assam', 5: 'Bihar', 6: 'Chandigarh', 
          7: 'Chhattisgarh', 8: 'Dadra & Nagar Haveli', 9: 'Daman & Diu', 10: 'Delhi', 11: 'Goa', 12: 'Gujarat', 13: 'Haryana', 
          14: 'Himachal Pradesh', 15: 'Jammu & Kashmir', 16: 'Jharkhand', 17: 'Karnataka', 18: 'Kerala', 19: 'Lakshadweep',
          20: 'Madhya Pradesh', 21: 'Maharashtra', 22: 'Manipur', 23: 'Meghalaya', 24: 'Mizoram', 25: 'Nagaland', 26: 'Orissa', 
          27: 'Pondicherry', 28: 'Punjab', 29: 'Rajasthan', 30: 'Sikkim', 31: 'Tamil Nadu', 32: 'Telangana', 33: 'Tripura',
          34: 'Uttar Pradesh', 35: 'Uttaranchal', 36: 'West Bengal'}

state_code = {1: 'andamannicobar', 2: 'andhrapradesh', 3: 'arunachalpradesh', 4: 'assam', 5: 'bihar', 6: 'chandigarh', 
          7: 'chhattisgarh', 8: 'dadranagarhaveli', 9: 'damandiu', 10: 'delhi', 11: 'goa', 12: 'gujarat', 13: 'haryana', 
          14: 'himachalpradesh', 15: 'jammukashmir', 16: 'jharkhand', 17: 'karnataka', 18: 'kerala', 19: 'lakshadweep',
          20: 'madhyapradesh', 21: 'maharashtra', 22: 'manipur', 23: 'meghalaya', 24: 'mizoram', 25: 'nagaland', 26: 'orissa', 
          27: 'pondicherry', 28: 'punjab', 29: 'rajasthan', 30: 'sikkim', 31: 'tamilnadu', 32: 'telangana', 33: 'tripura',
          34: 'uttarpradesh', 35: 'uttaranchal', 36: 'westbengal'}

print("Please select a Area to be searched by typing number for corresponding to state:")
for key in range( 1 , int(len(states)),3):
    print(str(key ) + " : " + format(str(states[key]), " >30s") + "    |     "+ str(key +1 ) + " : " + format(str(states[key +1]), " >30s") +"    |     "+str(key + 2 ) + " : " + format(str(states[key+2]), " >30s"))
choice = input()

#for convert choice into int
state = int(choice)

#getting html of website in a variable
website = "http://www.olx.in/" + str(state_code[state])+ "/" +str(categories[category])+'/?search[photos]=false&search[order]=filter_float_price%3Aasc'
print(website)

olxFile = requests.get(website)
olxHtml = olxFile.content

soup = BeautifulSoup(olxHtml)

noResults = "No results found"
if noResults in soup:
  print("Sorry no results found. Try after some days.")
else:
  tables = soup.findAll("table", {"summary" : "Ad"})

  cols = []
  titles = []
  links = []
  cities = []
  productTypes=[]
  prices = []

  for table in tables:
    aas = table.findAll("a",{'class':"marginright5 link linkWithHash detailsLink"})
    for a in aas:
      title = (a.text)
      titles.append(title[1:-1])
      link = (a.get('href'))
      links.append(link)
    ps = table.findAll("p",{'class':"color-9 lheight14 margintop3"})
    for p in ps:
      span = p.find('span')
      city = (span.text)
      cities.append(city)
      small = p.find('small')
      small = (re.sub(' +',' ',str(small)))
      productType = (small[32:small.find(str(span))])
      productTypes.append(productType[2:-1])
      price = table.find('strong',{"class" : "c000"} ).text
      prices.append(price[9:-8])
  
  col = []

  col.append("Title")
  col.append("Product Type and Company")
  col.append("City")
  col.append("Price")
  col.append("Link of product")

  cols.append(col)

  for i in range(0,len(titles)) :
    col = []
    col.append(titles[i])
    col.append(productTypes[i])
    col.append(cities[i])
    col.append(prices[i])
    col.append(links[i])
    cols.append(col)
  
  file_name = str(state_code[state])+ "_" +str(categories[category]) + '.csv'

  csv_file = open(file_name,'w', newline='')
  csv_writer = csv.writer(csv_file, delimiter=',')

  for row in cols:
    print(row)
    csv_writer.writerow(row)
 
  csv_file.close()

