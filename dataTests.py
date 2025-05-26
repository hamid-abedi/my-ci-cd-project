import unittest
import pandas as pd
import json
import os

class DataTests(unittest.TestCase):
    def setUp(self):
        self.csv_file = 'profiles1.csv'
        self.json_file = 'data.json'
        self.expected_columns = [
            'Givenname', 'Surname', 'Streetaddress', 'City', 'Zipcode', 
            'Country', 'CountryCode', 'NationalId', 'TelephoneCountryCode', 
            'Telephone', 'Birthday', 'ConsentToContact'
        ]
        self.min_rows = 900

    def test_csv_columns(self):
        df = pd.read_csv(self.csv_file)
        self.assertEqual(list(df.columns), self.expected_columns, 
                        f"CSV should have {self.expected_columns} columns")

    def test_csv_rows(self):
        df = pd.read_csv(self.csv_file)
        self.assertGreaterEqual(len(df), self.min_rows, 
                              f"CSV should have at least {self.min_rows} rows")

    def test_json_properties(self):
        if not os.path.exists(self.json_file):
            self.skipTest(f"JSON file {self.json_file} does not exist")
        with open(self.json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for record in data:
            for prop in self.expected_columns:
                self.assertIn(prop, record, f"JSON record missing property {prop}")

    def test_json_rows(self):
        if not os.path.exists(self.json_file):
            self.skipTest(f"JSON file {self.json_file} does not exist")
        with open(self.json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertGreaterEqual(len(data), self.min_rows, 
                              f"JSON should have at least {self.min_rows} rows")

if __name__ == '__main__':
    unittest.main()