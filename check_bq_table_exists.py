from google.cloud import bigquery
from google.cloud.exceptions import NotFound

bqclient = bigquery.Client()
project_id = "ishitashah-ctr-sandbox"
dataset_id = "airbnb"
table_id = "listings"

def table_exists(project_id,dataset_id,table_id):
    print("In function")
    bqclient=bigquery.Client(project_id)
    dataset_ref=bqclient.dataset(dataset_id)
    table_ref=dataset_ref.table(table_id)
    #table_info=bqclient.get_table(table_id)
    try:
        table=bqclient.get_table(table_ref)
        print(table)
        return True
    except NotFound:
        return False

print("here first")
output = table_exists(project_id,dataset_id,table_id)

print(output)
