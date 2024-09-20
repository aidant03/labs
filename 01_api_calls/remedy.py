import urllib.request
import json
import pandas as pd
import streamlit as st

url = 'https://www.saferproducts.gov/RestWebServices/' # Location of the API
query = 'Recall?format=json&ProductType=Exercise' # The query
response = urllib.request.urlopen(url+query)
response_bytes = response.read()
data = json.loads(response_bytes) # Convert response to json
response.close()
# print(data)

def flatten(df):
    temp = df['RemedyOptions']
    clean_values = []
    for i in range(len(temp)):
        if len(temp[i])>0:
            values = []
            for j in range(len(temp[i])):
                values.append(temp[i][j]['Option'] )
            clean_values.append(values)
        else:
            clean_values.append('')
    df['remedy'] = clean_values
    
newdf = pd.json_normalize(data)
flatten(newdf)
# print(newdf['remedy'])

remedy_counts = newdf['remedy'].value_counts()
st.title('Remedy Statistics')
st.write(remedy_counts)