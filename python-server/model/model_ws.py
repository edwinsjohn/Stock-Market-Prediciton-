import asyncio
import json
import websockets
import time
import random
import numpy as np
from stable_baselines3 import A2C
from nse_tool_live import Live_data
from Five import LiveData
import pandas as pd

live_data=LiveData()


def process_data(price_lst):
    p_len = len(price_lst)
    prices = price_lst[p_len - 10:]
    print(prices)
    diff = np.insert(np.diff(prices), 0, 0)
    signal_features = np.column_stack((prices, diff))
    return signal_features

def model_loading_AWT(obs):
    model = A2C.load("A2C_without_features.h5")
    action, _states = model.predict(obs)
    print(action)
    action_list = [0.002, 0.005, 0.008, 0.011, 0.014, 0.017, 0.02, -0.002, -0.005,
                   -0.008, -0.011, -0.014, -0.017, -0.02]
    price_inc = action_list[action]
    if (price_inc > 0):
        state = "Buy"
    else:
        state = "Sell"
    return price_inc, state

def model_loading_AT(obs):
    model = A2C.load("A2C_without_features.h5")
    action, _states = model.predict(obs)
    print(action)
    action_list = [0.002, 0.005, 0.008, 0.011, 0.014, 0.017, 0.02, -0.002, -0.005,
                   -0.008, -0.011, -0.014, -0.017, -0.02]
    price_inc = action_list[action]
    if (price_inc > 0):
        state = "Buy"
    else:
        state = "Sell"
    return price_inc, state

def model_loading_A2CD(obs):
    model = A2C.load("A2C_diff_reward.h5")
    action, _states = model.predict(obs)
    print(action)
    action_list = [0.002, 0.005, 0.008, 0.011, 0.014, 0.017, 0.02, -0.002, -0.005,
                   -0.008, -0.011, -0.014, -0.017, -0.02]
    price_inc = action_list[action]
    if (price_inc > 0):
        state = "Buy"
    else:
        state = "Sell"
    return state



async def handler(websocket):
   tqty=0
   live=[]
   counter = 0
   start_=True
   while True:
    nse_t_price=Live_data()
    ntp=nse_t_price.fetch()
    fivePdata = live_data.callWS()
    fprice = fivePdata["LastRate"]
    lqty=fivePdata["LastQty"]
    tqty=tqty+lqty
    if(counter%2==0):
        live.append(fprice)
        print("added",len(live))
        if(len(live)>15):
            print("staeted")
            observations=process_data(live)
            aWT_p,aWT_s=model_loading_AWT(observations)
            a2c_T_p, a2c_T_s = model_loading_AT(observations)
            a2cd_s = model_loading_A2CD(observations)
            awt_f = {'price':fprice+fprice*aWT_p, "state": aWT_s}
            a2c_t={'price': fprice+fprice*a2c_T_p, "state": a2c_T_s}
            a2cd = {"state": a2cd_s}
            main = {'A2C_W_T': awt_f,'A2CT':a2c_t,'A2CD':a2cd}
            await websocket.send(json.dumps(main))
    print(counter)
    counter=counter+1


    await asyncio.sleep(.1)




async def main():
    async with websockets.serve(handler, "", 8005):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())