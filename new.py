import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "4oDBgnbS-Aikf8dqUWmY8Mo3lPYc3EASfN9TyomfZKv3"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [Airline,source,destination,depdate,depmonth,depyear,deptimehour,deptimemins,artime,artimehour,artimemins], "values": [GoAir,bangalore,chennai,23,12,5,20,40,12,2,50]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/e52653f6-3287-4114-9910-b18179c5861d/predictions?version=2022-08-28', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())