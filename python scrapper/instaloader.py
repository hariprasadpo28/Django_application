import pandas as pd
from geotext import GeoText
from instaloader import Instaloader, Profile

instance = Instaloader()
instance.login("username", "password")
username = []
df = pd.read_csv("Instagram.csv")
for item in df['Instagram URL']:
    username.append(item.split('\')[-2])

dic = {}
dic["Name"] = []
dic["Followers"] = []
dic["Followees"] = []
dic["Category"] = []
dic["Contact"] = []
dic["City"] = []
dic["Bio"] = []

for item in username:
     profile = Profile.from_username(instance.context, item)
     if profile.followers:
         dic['Followers'].append(profile.followers)
     else:
         dic['Followers'].append("None")
     if profile.followees:
         dic['Followees'].append(profile.followees)
     else:
         dic['Followees'].append("None")
     if profile.business_category_name:
         dic['Category'].append(profile.business_category_name)
     else:
         dic['Category'].append("None")
     if profile.full_name:
         dic['Name'].append(profile.full_name)
     else:
         dic['Name'].append("None")
     if profile.biography:

         dic['Bio'].append(profile.biography)
         places = GeoText(profile.biography)
         cities = list(places.cities)
         if cities:
             dic['City'].append(cities[0])
         else:
             dic['City'].append("None")
     else:
         dic['Bio'].append("None")

df1 = pd.DataFrame(dic)
df1.to_csv("Details.csv", index = False)
