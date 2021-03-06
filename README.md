# IBM AI Enterprise Workflow Capstone
Notes for the IBM AI Enterprise Workflow Capstone project. 

## Part 1

### Case study part 1

Overall this part of the case study is meant to tell the story of the data by investigating the relationship between the data and the business opportunity.

1. Assimilate the business scenario and articulate testable hypotheses.

The business requirement is to predict the next month's revenue on any given day (note: model uses 30ays for consistency). This can be achieved using regression.

2. State the ideal data to address the business opportunity and clarify the rationale for needing specific data.

To support the regression analysis, we can combine revenue features and other drivers:

	- revenue: past week, past month, same period last year and "next 30 days" will become the target
	- drivers: unique streams, purchases, total views (a stream can be viewed more than once)


3. Create a python script to extract relevant data from multiple data sources, automating the process of data ingestion.

The python module ingestion.py includes the necessary functions to ingest the data 

4. Investigate the relationship between the relevant data, the target and the business metric.

The notebook EDA.ipynb explores the relationships between the data.

The code for the charts is included in "charts.py"

5. Articulate your findings using a deliverable with visualizations.

The notebook EDA.ipynb explores the relationships between the data. Notes:
 - Data shows a significant year end peak in revenue for UK, Eire
 - Monthly Purchases and Revenue correlate for UK, Germany, Netherlands, Spain, France(?), but not for Singapore, Norway, Hong Kong, Portugal
 - UK Purchase volumes are 80x next largest country and 15x revenue
 - Hong Kong and Singapore are incomplete time-series, no data for 2019




## Part 2

### Case study part 2

Time-series analysis is a new subject area for me, so I focused on leveraging the provided solution and ensuring understanding of that approach.


## Deliverable goals

1. State the different modeling approaches that you will compare to address the business opportunity.

model.py includes the functions to train a Random Forest Classifier and uses Grid search to alter some of the hyperparameters

2. Iterate on your suite of possible models by modifying data transformations, pipeline architectures, hyperparameters and other relevant factors.

Done

3. Re-train your model on all of the data using the selected approach and prepare it for deployment.
Done

4. Articulate your findings in a summary report.

WiP - running short on time to write this up.
  
## Part 3

## Outline

1. Build a draft version of an API with train, predict, and logfile endpoints.

Done

2. Using Docker, bundle your API, model, and unit tests.

Done 
	~$ docker build -t capstone .
	~$ docker run -p 4000:8080 capstone

3. Using test-driven development iterate on your API in a way that anticipates scale, load, and drift.

WIP, currently the python module "scripts to query API.py" allows training of the model via the API and prediction of revenue for a number of dates

4. Create a post-production analysis script that investigates the relationship between model performance and the business metric.

To do

5. Articulate your summarized findings in a final report.

To do


At a higher level you are being asked to:





