#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import argparse
import csv
import pandas as pd


bqclient = bigquery.Client()
project_id = "ishitashah-ctr-sandbox"
dataset_id = "airbnb"
table_id = "listings"

def table_exists(table_list):
    bqclient=bigquery.Client(project_id)
    #dataset_ref=bqclient.dataset(dataset_id)
    #table_ref=dataset_ref.table(table_id)
    #table_info=bqclient.get_table(table_id)

    for table_id in table_list:
        try:
            table=bqclient.get_table(table_id)
            print("Got table '{}.{}.{}'.".format(table.project, table.dataset_id, table.table_id))
        except NotFound:
            print("Couldn't find table {}".format(table_id))
            pass
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if BQ table exists")
    parser.add_argument('csvfile', type=argparse.FileType('r'), help='Input csv file with table data')
    args = parser.parse_args()
    file_name = args.csvfile 
    #print('main(): type(args.csvfile)) = {}'.format(args.csvfile))

    #provide the name of the column which consists of tables names in the format projectId.datasetId.tableId
    table_list = pd.read_csv(args.csvfile,usecols=['BQ - Dev'])
    table_exists(table_list['BQ - Dev'])
