import streamlit as st
import numpy as np
import pandas as pd

st.title('Salary estimate for Data Science related roles')
st.write('''
## following are the parameters to determine the salary of any data science job:
1. Location of the company
2. Age of the company
3. Company revenue
4. The sector and Industry of the company (automobile, advertisement and entertainment, healthcare, technology, IT, etc)
5. Current competitors of the company
6. The seniority of the position
7. The skills required for a candidate
''')
# read dataframe
df = pd.read_csv('S:/CAREER/PROJECTS/Salary_estimate/csv_files/salary_data_eda.csv')

# select job role
roles = ['AI engineer', 'Business analyst', 'Big data engineer', 'Deep learning engineer', 'Machine learning engineer',
         'NLP engineer', 'Data analyst', 'Data engineer', 'Data Scientist', 'manager', 'software engineer', 'other']
simplified_roles = ['AIE', 'BA', 'BDE', 'DLE', 'MLE', 'NLPE', 'data analyst', 'data engineer', 'data scientist', 'manager'
                    ,'software engineer', 'na']
job_role = st.sidebar.selectbox(
    'select a job role', roles)

# convert job role to the format we need
job_role = 'job_simplifier_'+ simplified_roles[roles.index(job_role)]
'You selected: ', job_role

# take user input for job location
loc = list(df['Location'].unique())
job_location = "Location_" + st.sidebar.selectbox("enter job location", loc)
st.sidebar.write("*select India if location is not present")
'You selected: ', job_location

# select the different skills required 
skills = ['python', 'sas', 'aws', 'spark',
       'sql', 'tableau', 'tensorflow', 'nltk', 'power bi', 'excel', 'hadoop',
       'azure', 'scikit-learn', 'r_prog']
option = st.sidebar.multiselect(
    'select all the skills required?', skills)

'You selected: ', option

# select seniority 
seniority = ['na','junior', 'senior']
job_seniority = 'seniority_' + st.sidebar.selectbox('choose seniority', seniority)

'You selected: ', job_seniority

# select sector
sectors = list(df.Sector.unique())
sectors[sectors.index('-1')] = 'other'
job_sector = 'Sector_' + st.sidebar.selectbox(
    'select a sector', sectors)
'You selected: ', job_sector

# select industry
industry = list(df.Industry.unique())
industry[industry.index('-1')] = 'other'
job_industry = 'Industry_' + st.sidebar.selectbox(
    'select an Industry', industry)
'You selected: ', job_industry

# degree required
deg_req = st.sidebar.radio('Is degree required?', ['yes', 'no'])

# size of the company
size = st.sidebar.select_slider('How many employees work here?', ['unknown', '1 to 50', '51 to 200', '201 to 500', '501 to 1000',
                    '1001 to 5000', '5001 to 10000', '10000+'], value='unknown')

# select revenue
revenue = list(df.Revenue.unique())
job_revenue = 'Revenue_' + st.sidebar.selectbox(
    "select company's revenue", revenue)
'You selected: ', job_revenue

