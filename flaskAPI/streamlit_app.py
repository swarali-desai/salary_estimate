import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
from data_input import data_in

def encode_data(param, data_in, value=None, categorical=False):
    if param in data_in.keys():
        if categorical:
            data_in[param] = 1
        else:
            data_in[param] = value
 

st.title('Salary estimator for Data Science roles')
st.write('''
## Following are the parameters to determine the salary of any data science job:
1. Location of the company
2. Age of the company
3. Company revenue
4. The sector and Industry of the company (automobile, advertisement and entertainment, healthcare, technology, IT, etc)
5. Current competitors of the company
6. The seniority of the position
7. The skills required for a candidate

##### Choose parameters from the sidebar
''')
'---'
'#### Parameters you selected are: '
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
'job role selected: ', job_role

# enter job description
desc_len = st.sidebar.text_input('enter job description')

# take user input for job location
loc = list(df['Location'].unique())
job_location = "Location_" + st.sidebar.selectbox("enter job location", loc)
st.sidebar.write("*select India if location is not present")
'job location selected: ', job_location


# select the different skills required 
skills = ['python', 'sas', 'aws', 'spark',
       'sql', 'tableau', 'tensorflow', 'nltk', 'power bi', 'excel', 'hadoop',
       'azure', 'scikit-learn', 'r_prog']
option = st.sidebar.multiselect(
    'select all the skills required?', skills)
'skills selected: ', str(option)

# select seniority 
seniority = ['na','junior', 'senior']
job_seniority = 'seniority_' + st.sidebar.selectbox('choose seniority', seniority)
'seniority selected: ', job_seniority

# select sector
sectors = list(df.Sector.unique())
sectors[sectors.index('-1')] = 'other'
job_sector = 'Sector_' + st.sidebar.selectbox(
    'select a sector', sectors)
if job_sector == 'Sector_other':
    job_sector = 'Sector_-1'
'sector selected: ', job_sector

# select industry
industry = list(df.Industry.unique())
industry[industry.index('-1')] = 'other'
job_industry = 'Industry_' + st.sidebar.selectbox(
    'select an Industry', industry)
if job_industry == 'Industry_other':
    job_industry = 'Industry_-1'
'industry selected: ', job_industry

# degree required
deg_req = st.sidebar.radio('Is degree required?', ['yes', 'no'])
'degree required: ',deg_req

# size of the company
size = st.sidebar.select_slider('How many employees work here?', ['unknown', '1 to 50', '51 to 200', '201 to 500', '501 to 1000',
                    '1001 to 5000', '5001 to 10000', '10000+'], value='unknown')
'company size: ', size


# select revenue
revenue = list(df.Revenue.unique())
job_revenue = 'Revenue_' + st.sidebar.selectbox(
    "select company's revenue", revenue)
'revenue selected: ', job_revenue


age = st.sidebar.text_input(
    "select company's age", int())
'company age: ', age

test = st.button('TEST API')
if test:
    try:
        URL = 'http://127.0.0.1:5000/hello'
        headers = {"Content-Type": "application/json"}
        r = requests.get(URL,headers=headers)
        st.success(r.text)

    except:
        st.warning("Flask app is not running")


submit = st.button('ESTIMATE')
if submit:
    data_in = {k:0 for k in data_in.keys()}

    # encode data for model
    encode_data('age', data_in, int(age), categorical=False)
    encode_data('desc_len', data_in, len(desc_len), categorical=False)
    encode_data(job_role, data_in, job_role, categorical=True)
    encode_data(job_location, data_in, job_location, categorical=True)
    for skill in option:
        encode_data(skill, data_in, skill, categorical=True)
    encode_data(job_seniority, data_in, job_seniority, categorical=True)
    encode_data(job_sector, data_in, job_sector, categorical=True)
    encode_data(job_industry, data_in, job_industry, categorical=True)
    if deg_req=='yes':
        encode_data('degree_req', data_in, categorical=True)
    encode_data(size, data_in, size, categorical=True)
    encode_data(job_revenue, data_in, job_revenue, categorical=True)

    input_list = []
    for val in data_in.values():
        input_list.append(val)
    with st.spinner('Estimating salary...'):
        try:
            URL = 'http://127.0.0.1:5000/predict'
            headers = {"Content-Type": "application/json"}
            data = {"input": input_list}
            r = requests.post(URL,headers=headers, json=data)
            r = r.json()
            st.success(str(r['response']) + ' Rs')
            # st.balloons()
        except:
            st.error("ERROR! try test to check if flask app is running")



