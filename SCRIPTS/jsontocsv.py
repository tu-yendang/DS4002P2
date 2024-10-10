import json
import csv
import os
from datetime import datetime

json_file_path=os.path.join(os.path.dirname(__file__), '../DATA/Raw JSON Data/sabrina_carpenter.json')
csv_file_path=os.path.join(os.path.dirname(__file__), '../DATA/monthly_listeners/sabrina_carpenter.csv')

with open(json_file_path) as json_file:
    data = json.load(json_file)

popularity = data["popupInfo"]["seriesData"][0]['data']
monthly_listeners = data["popupInfo"]["seriesData"][1]['data']

with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Date', 'Monthly Listeners'])

    for entry in monthly_listeners:
        if len(entry) == 2:
            timestamp = entry[0]/1000
            readable_date=datetime.fromtimestamp(timestamp).strftime('%m-%d-%Y')
            monthly_listeners=entry[1]
            csv_writer.writerow([readable_date, monthly_listeners])
