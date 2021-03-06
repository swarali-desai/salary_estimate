'''
part of project salary estimate for data science roles
author: Swarali Desai
dated: 08/08/2020
'''

import glassdoor_webscrapper as gs
import pandas as pd 

path = "C:/Program Files (x86)/chromedriver.exe"
'''
# fetched data for following roles:
1. Data scientist : 150
2. Data analyst : 75
3. Machine learning engineer : 75
4. Deep learning engineer : 75
5. Business Analyst: 75
6. Big Data Engineer: 75
7. NLP engineer : 75
'''
df = gs.get_jobs('Data scientist',150, False, path, 15)


df.to_csv('glassdoor_jobs_ds.csv', index = False)