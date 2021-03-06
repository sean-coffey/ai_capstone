#!/usr/bin/env python
"""
api tests

these tests use the requests package however similar requests can be made with curl

e.g.

data = '{"key":"value"}'
curl -X POST -H "Content-Type: application/json" -d "%s" http://localhost:8080/predict'%(data)
"""
import json
import sys
import os
import unittest
import requests
import re
from ast import literal_eval
import numpy as np

port = 8080

try:
    requests.post(f'http://127.0.0.1:{port}/predict')
    server_available = True
except:
    server_available = False
    
## test class for the main window function
class ApiTest(unittest.TestCase):
    """
    test the essential functionality
    """

    @unittest.skipUnless(server_available, "local server is not running")
    def test_01_train(self):
        """
        test the train functionality
        """
      
        request_json = {'mode':'test'}
        r = requests.post(f'http://127.0.0.1:{port}/train', json=request_json)
        train_complete = re.sub("\W+", "", r.text)
        self.assertEqual(train_complete, 'true')

    @unittest.skipUnless(server_available, "local server is not running")
    def test_02_predict_empty(self):
        """
        ensure appropriate failure types
        """

        ## provide no data at all
        r = requests.post(f'http://127.0.0.1:{port}/predict')
        self.assertEqual(re.sub('\n|"', '', r.text), "[]")

        ## provide improperly formatted data
        r = requests.post(f'http://127.0.0.1:{port}/predict', json={"key": "value"})
        self.assertEqual(re.sub('\n|"', '', r.text), "[]")


    @unittest.skipUnless(server_available, "local server is not running")
    def test_03_predict(self):
        """
        test the predict functionality
        """

        query_data = {'country': 'all',
                      'year': 2018,
                      'month': 1,
                      'day': 5
                      }

        query_type = 'dict'
        request_json = {'query': query_data, 'type': query_type, 'mode': 'test'}
        r = requests.post(f'http://127.0.0.1:{port}/predict', json=request_json)
        print(f"Result from test_03_predict: {r.text}")
        response = json.loads(r.text)
        response['y_pred']
        self.assertTrue(response['y_pred'][0] > 0)


    @unittest.skipUnless(server_available, "local server is not running")
    def test_04_logs(self):
        """
        test the log functionality
        """

        file_name = 'train-test.log'
        request_json = {'file': file_name}
        r = requests.get(f'http://127.0.0.1:{port}/logs/{file_name}')
        log_dir = os.path.join("logs")
        if not os.path.isdir(log_dir):
            print("ERROR: API (log): cannot find log dir")

        file_path = os.path.join(log_dir, file_name)

        with open(file_path, 'wb') as f:
            f.write(r.content)

        self.assertTrue(os.path.exists(file_path))

        if os.path.exists(file_path):
            os.remove(file_path)


        
### Run the tests
if __name__ == '__main__':
    unittest.main()
