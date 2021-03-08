# IBM AI Enterprise Workflow Capstone
Notes for the IBM AI Enterprise Workflow Capstone project. 

A summary by required deliverable is included in the notebook:

		Capstone Deliverables.ipynb

## Part 1

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

Time-series analysis is a new subject area for me, so I focused on leveraging the provided solution and ensuring understanding of that approach.

1. State the different modeling approaches that you will compare to address the business opportunity.

		model.py includes the functions to train a Random Forest Classifier and uses Grid search to alter some of the hyperparameters

2. Iterate on your suite of possible models by modifying data transformations, pipeline architectures, hyperparameters and other relevant factors.

		Done

3. Re-train your model on all of the data using the selected approach and prepare it for deployment.
Done

4. Articulate your findings in a summary report.

		WiP - running short on time to write this up.
  
## Part 3

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

Table of predictions from the API:

		country date	 y_known     y_pred 	   y_proba
		all  2017-11-30  170445.260  170418.35720    None
		all  2017-12-31  173092.473  170589.10270    None
		all  2018-01-31  129925.585  133476.87405    None
		all  2018-02-28  263632.401  269517.11650    None
		all  2018-03-31  116642.342  117181.30100    None
		all  2018-04-30  144481.060  145168.12250    None
		all  2018-05-31  236716.830  235655.49755    None
		all  2018-06-30   93654.340   96385.45850    None
		all  2018-07-31  152791.380  148481.70770    None
		all  2018-08-31  219264.551  229374.80445    None
		all  2018-09-30  270842.590  244044.53360    None
		all  2018-10-31  320371.492  318685.87700    None
		all  2018-11-30  387279.740  385130.53500    None
		all  2018-12-31  178314.260  175340.66410    None
		all  2019-01-31  135549.990  130746.47355    None
		all  2019-02-28  165443.920  164121.92850    None
		all  2019-03-31  125779.021  134689.01955    None
		all  2019-04-30  195218.250  188127.34520    None
		all  2019-05-31  191391.680  194427.89650    None
		all  2019-06-30    1793.980  138915.06960    None

		 country 	target_date y_known   	 y_pred 	y_proba
		 united_kingdom  2017-11-30  160736.980  159026.26332    None
		 united_kingdom  2017-12-31  148110.823  148124.26808    None
		 united_kingdom  2018-01-31  116077.065  117399.65768    None
		 united_kingdom  2018-02-28  217019.201  214622.90820    None
		 united_kingdom  2018-03-31  103206.131  107707.73292    None
		 united_kingdom  2018-04-30  125986.030  126940.41360    None
		 united_kingdom  2018-05-31  224732.640  221815.13448    None
		 united_kingdom  2018-06-30   77115.230   84733.77644    None
		 united_kingdom  2018-07-31  135398.810  129720.75160    None
		 united_kingdom  2018-08-31  201918.791  205726.52100    None
		 united_kingdom  2018-09-30  235499.470  235164.62640    None
		 united_kingdom  2018-10-31  299139.572  295841.59880    None
		 united_kingdom  2018-11-30  375412.060  364785.72128    None
		 united_kingdom  2018-12-31  163467.850  166148.73200    None
		 united_kingdom  2019-01-31  122629.750  120224.73296    None
		 united_kingdom  2019-02-28  142085.490  141947.36444    None
		 united_kingdom  2019-03-31  104058.691  109359.64300    None
		 united_kingdom  2019-04-30  174900.620  184747.48936    None
		 united_kingdom  2019-05-31  170593.560  166606.77960    None
		 united_kingdom  2019-06-30    1793.980  121572.19012    None







