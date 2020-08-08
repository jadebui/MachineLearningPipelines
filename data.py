import pandas as pd #Libraries for processing data in python
import numpy as np #Libraries for processing numeric in python
import pickle as pkl #save model and sclaer
import json #read file json
#===Connect Google Cloud===#
from google.cloud import storage
from io import StringIO
#connect database
import os
from google.cloud.bigquery.client import Client
import google.auth
from google.cloud.bigquery.schema import SchemaField
from google.cloud import bigquery
import datetime, time
import json
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'connect_bigquery.json'
credentials, project = google.auth.default()
credentials = credentials.with_scopes(['https://www.googleapis.com/auth/bigquery'])
client = Client(credentials=credentials)
dataset = client.dataset('ahamove_archive')
sql = """
select 
accept_time,
board_time,
accept_distance as distance,
json_extract_scalar(_extra_props,'$.accept_lat') as accept_lat,
json_extract_scalar(_extra_props,'$.accept_lng')  as accept_lng,
json_extract_scalar(_extra_props,'$.pickup_lat')  as pickup_lat,
json_extract_scalar(_extra_props,'$.pickup_lng')  as pickup_lng,
date_diff (date (o.order_time),date(s.first_complete_time),day) as experience
from ahamove_archive.order_archive o left join  ahamove_archive.supplier s on o.supplier_id = s.id 
where order_time >= '2019-03-01'
and order_time<='2019-03-02'
and o.status = 'COMPLETED'
and o.city_id = 'HAN'
AND service_id in ('HAN-BIKE')
and o.create_time=o.order_time
and path_length =2
and distance is not null
and user_id not in ('84862151477','84905331088','84908633203','8419001240','84966883626','84937217722',
'84944320850','84909535411','84938111549', '84906306874','84358045420','84906804990','84855455399','84394304617',
'84906375565','84336475460','84937303662','84903314422','84396404389','84978265262','84909495665','84385418130', '84327439534','84937252673','84933855653','84976273993','84384002694','8419002170','842871082237',
'84374975918')
"""
def get_gbq_dataframe(sql):
    query = (sql)
    data = client.query(query).to_dataframe()
    return data