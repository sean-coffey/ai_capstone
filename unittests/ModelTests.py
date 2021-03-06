#!/usr/bin/env python
"""
model tests
"""

import sys, os
import unittest

sys.path.insert(1, os.path.join('..', os.getcwd()))

# import model specific functions and variables
from model import *


class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """

    def test_01_train(self):
        """
        test the train functionality
        """

        # train the model
        data_dir = os.path.join(".", "data", "cs-train")
        file_name = os.path.join("models", "test-all-0_1.joblib")
        if os.path.exists(file_name):
            os.remove(file_name)
        model_train(data_dir, test=True)
        self.assertTrue(os.path.exists(file_name))

    def test_02_load(self):
        """
        test the load functionality
        """

        # load the model
        all_data, all_models = model_load(test=True)
        model = all_models['all']
        self.assertTrue('estimator' in dir(model))

    def test_03_predict(self):
        """
        test the predict function input
        """

        # load model first
        all_data, all_models = model_load(test=True)
        country = 'all'
        year = '2018'
        month = '01'
        day = '05'
        model = all_models[country]
        model_data = all_data[country]
        result = model_predict(country, year, month, day, model, model_data, test=True)
        y_pred = result['y_pred']
        self.assertTrue(y_pred[0] > 0)


# Run the tests
if __name__ == '__main__':
    unittest.main()
