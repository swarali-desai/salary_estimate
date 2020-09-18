# Data Science Salary Estimator

## Project overview
This is an end-to-end data science project for salary estimation of any data science roles. 
* Web scrapping is done using selenium and python from glassdoor for various job roles ( upto 1000 jobs). 
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Exploratory data analysis was performed using seaborn, matplotlib and pandas libraries. 
* Linear regression, Lasso regression and random forest regression models were used,Random forest performed the best ( MAE ~ 45k Rs). 
* Built Flask API endpoint was created.
* Created a webapp using streamlit and python.

## Web scrapping
Using selenium and python managed to scrape folling parameters from glassdoor for data science roles
1. Job title
2. Salary Estimate
3. Job Description
4. Rating
5. Company
6. Location
7. Company Headquarters
8. Company Size
9. Company Founded Date
10. Type of Ownership
11. Industry
12. Sector
13. Revenue
14. Competitors

Data for following job roles was scrapped
'AI engineer', 'Business analyst', 'Big data engineer', 'Deep learning engineer', 'Machine learning engineer','NLP engineer', 'Data analyst', 'Data engineer', 'Data Scientist', 'manager' and 'software engineer'.

## Data cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
* Parsing the salary column to get the numeric data only.
* Edit the company name column. Split rating appended with the company name and remove duplicates.
* Parsed out important details out of job description column.
* Created separate columns for skills mentioned such as Python, R, AWS, Spark, database, R studio, Tableau, Tensorflow, NLTK, Power BI, Excel, Hadoop, Azure, scikit-learn, etc.
* another column for degree requirement.
* Simplified job roles into broader categories.
   1. Data scientist
   2. Data analyst
   3. Machine learning Engineer
   4. Big data engineer
   5. Data engineer
   6. NLP engineer
   7. AI engineer
   8. manager
   9. director
   10. business analyst
* Column for description length.
Final cleaning reduced the the csv to 594 columns. Thus the data on which the model is trained is very small.

## Exploratory data analysis
I looked at the distributions of the data and the value counts for the various categorical variables.
![alt text](https://github.com/swarali-desai/salary_estimate/blob/master/images/eda_word_cloud.png)
![alt text](https://github.com/swarali-desai/salary_estimate/blob/master/images/heatmap.PNG)
![alt text](https://github.com/swarali-desai/salary_estimate/blob/master/images/job_simplifier.PNG)
![alt text](https://github.com/swarali-desai/salary_estimate/blob/master/images/location.PNG)

## Model building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:

Multiple Linear Regression – Baseline for the model
Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.

## Productionization
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the resources section below. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
Created a Webapp using Streamlit and python on local host.

## Resources
- Glassdoor web scrapper: https://github.com/arapfaik/scraping-glassdoor-selenium

    **CHANGES:**
    
      1. changes made for the Indian glassdoor webpage (https://www.glassdoor.co.in/)
      2. salary estimate extraction from the salary tab for data scientist
      
- Code productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

- Project Inspiration: 
1. Github: https://github.com/PlayingNumbers/ds_salary_proj
2. Youtube: https://youtu.be/MpF9HENQjDo
