import os
import csv
from main import process_to_csv

def test_fetch_weather_data():
    process_to_csv()
    assert os.path.exists('data/filtered_data.csv')
    with open('data/filtered_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        assert len(rows) == 60 # 10 locations, 6 rows for each location