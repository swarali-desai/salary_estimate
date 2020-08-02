import glassdoor_webscrapper as gs
import pandas as pd 

path = "C:/Program Files (x86)/chromedriver.exe"

df = gs.get_jobs('data scientist',1000, False, path, 15)
# print(df.head())

df.to_csv('glassdoor_jobs.csv', index = False)