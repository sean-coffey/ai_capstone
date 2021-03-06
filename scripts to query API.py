import json

import requests
import re

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
    print(f"Result from test_03_predict: {r.text}")
    response = json.loads(r.text)

    return response


if __name__ == "__main__":

    try:
        requests.post(f'http://127.0.0.1:{port}/predict')
        server_available = True
    except:
        server_available = False

    if server_available:
        train()


        country='all'
        results = []
        for month in range(1,7):
            revenue_predict=predict(country=country, month=month)
            results.append(revenue_predict)

        print(results)
