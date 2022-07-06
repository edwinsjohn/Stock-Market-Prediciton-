import json
import time
import pandas
import csv
from datetime import datetime
from py5paisa import FivePaisaClient
import websockets
import asyncio
ts = time.time()


class LiveData:
    def __init__(self):
        self.data=[]
        self.cred={
            "APP_NAME": "5P51035409",
            "APP_SOURCE": "10077",
            "USER_ID": "F36rW3WT6ei",
            "PASSWORD": "7ehs8tC3EZb",
            "USER_KEY": "SiOqz4ExATxvpwQ0jXsPl2kFj0006DQ8",
            "ENCRYPTION_KEY": "yhjovTPjGtCY7qwNRr1LJUHKlZE5gkKn"
        }
        self.client = FivePaisaClient(email="edwinsajee@gmail.com", passwd="edwinsj@2000", dob="20000310", cred=self.cred)
        self.client.login()
        scrip_list=[
            { "Exch":"N","ExchType":"C","ScripCode":3499}
            ]
        self.feed_data=self.client.Request_Feed('mf','s',scrip_list)
        self.client.connect(self.feed_data)

    def callWS(self):
        def on_message(ws, message):
            live_datas = json.loads(message)
            self.data = (live_datas[0])
            ws.close()

        self.client.receive_data(on_message)
        return self.data


    #
    # def getPrice(self):
    #     def on_message(ws,message):
    #         obj = json.loads(message)
    #         time=int(ts)
    #         # time = int(obj[0]["TickDt"][6:16])
    #         # print(time, time % 60)
    #         if self.starting_ == True:
    #             open = int(obj[0]["LastRate"])
    #             high = open
    #             low = open
    #             self.starting_ == False
    #             print("mod")
    #         if (time % 60 == 0):
    #             open = int(obj[0]["LastRate"])
    #             high = open
    #             low = open
    #         close = int(obj[0]["LastRate"])
    #         if (high < close):
    #             high = close
    #         if (low > close):
    #             low = close
    #         # collection.insert_one({"time": time, "open": open, "high": high, "low": low, "close": close})
    #         print(high, low, open, close)






