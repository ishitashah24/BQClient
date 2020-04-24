# Check BigQuery Tables 
  Command-line utility to validate the existence of BigQuery tables 
	
## Purpose
  This allows to test the tables during migration from any data source to BigQuery
	
## Usage  
  `python check_bq_table_exists.py tables_list.csv`
  
  The argument is a csv file(tables_list) that contains the list of all the `table ids` that need to be checked against.
  
  The format of the table_id should be `projectId.datasetId.tableId`.
	
  For multiple columns in a file, specify the column name which consists of all the `table ids`. Here, that column is 
  `BQ - Dev`.  
	
## Example
   `table_id=test_project.test_dataset.test_table` is the table id, an argument passed to the `table_exists()`
	
   `get_table()` fetches the information of the table if it exists otherwise returns a message- "Table Not Found"
 
## File Layout
 [check_bq_table_exists.py](BQClient/check_bq_table_exists.py) is a BigQuery client wrapper and command-line executable


## Pre-requisites

[Python 3.4 or later](https://www.python.org/downloads/)

[Google Cloud Python Client](https://github.com/googleapis/google-cloud-python)


## Installation

cd to repository root and run `python3 -m pip install`


## Disclaimer
 This is not an official Google project
