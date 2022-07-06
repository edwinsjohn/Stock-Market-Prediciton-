import asyncio
import json
import websockets
import time
import random

from nse_tool_live import Live_data
from live_data_5p import LiveData

live_data=LiveData()
# print(nse_t_price.fetch())



async def handler(websocket):
   start_=True
   while True:
    nse_t_price=Live_data()
    ntp=nse_t_price.fetch()
    fivePdata = live_data.callWS()
    fprice = fivePdata["LastRate"]
    time_t = int(fivePdata["TickDt"][6:16])
    ts = int(time.time())
    if(start_==True):
        ts2=ts
        open = fprice
        high = open
        low = open
        start_=False
    if(ts%60==0):
        ts2=ts
        open = fprice
        high = open
        low = open
    close = fprice
    if (high < close):
        high = close
    if (low > close):
        low = close

    chartdata={"time":time_t,"open":open,"high":high,"low":low,"close":close}
    print(chartdata)
    ntp_dict={'price':ntp}
    main={'time':ts2,"nse_t":ntp_dict,"chartdata":chartdata,"full":fivePdata}
    await websocket.send(json.dumps(main))
    await asyncio.sleep(1)




async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())