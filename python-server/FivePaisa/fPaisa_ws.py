from live_data_5p import LiveData

live_data=LiveData()
for i in range (0,4):
    a=live_data.callWS()
    print(a["Exch"])
