import json

import requests
import re
import pandas as pd

port = 8080

def train():
    
    request_json = {'mode': 'prod'}
    print("...starting training")
    r = requests.post(f'http://127.0.0.1:{port}/train', json=request_json)
    train_complete = re.sub("\W+", "", r.text)
    if train_complete:
        print("...training complete")
    else:
        print("An error occurred in training")

def predict(country='all',year=2018, month=1, day=1):

    query_data = {'country': country,
                  'year': year,
                  'month': month,
                  'day': day
                  }

    query_type = 'dict'
    request_json = {'query': query_data, 'type': query_type, 'mode': 'prod'}
    r = requests.post(f'http://127.0.0.1:{port}/predict', json=request_json)
    response = json.loads(r.text)

    return response


if __name__ == "__main__":

    try:
        requests.post(f'http://127.0.0.1:{port}/predict')
        server_available = True
    except:
        server_available = False

    if server_available:
        #train()

        countries=['all','united_kingdom']
        start= '2017-11-01'
        end= '2019-06-30'
        date_range = pd.date_range(start=start,end=end,freq='M')
        results = []
        for country in countries:
            for date in date_range:
                revenue_predict=predict(country=country, year=date.year, month=date.month, day=date.day)
                results.append(pd.DataFrame.from_dict(revenue_predict))
            results_df = pd.concat(results)
        print(results_df)
