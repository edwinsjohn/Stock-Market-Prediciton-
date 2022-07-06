import pandas as pd
from nsetools import Nse
from datetime import datetime
import csv


class Live_data:
    def __init__(self):
        self.pricel = []
        self.timestamp = []
        self.nse = Nse()

    def fetch(self):
        now = datetime.now()
        self.stock_data = self.nse.get_quote('TATASTEEL')
        self.price = self.stock_data['averagePrice']
        current_time = now.strftime("%H:%M")
        self.timestamp.append(current_time)
        with open("live.csv", 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            row = [[self.price, current_time]]
            csvwriter.writerows(row)
        return self.price