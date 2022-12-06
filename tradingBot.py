import pprint
import xlwt
from xlwt import Workbook
from mttkinter import mtTkinter as tk
import time
import datetime
from td.client import TDClient
from tkinter import *

#login info for api
ACCOUNT_NUMBER = ''
ACCOUNT_PASSWORD = ''
CONSUMER_ID = ''
REDIRECT_URI = ''
JSON_PATH = None

#testapi
TDSession = TDClient(consumer_id=CONSUMER_ID, redirect_uri=REDIRECT_URI, json_path=JSON_PATH)
# Login to the session
TDSession.login()
# Create a streaming session
TDStreamingClient = TDSession.create_streaming_session()


root = Tk()
def mornhighstrat():
    global startmin
    global startsec
    global mornData

    quotes_single = TDSession.get_quotes(instruments=['SPY'])
    SPY_DATA = (quotes_single['SPY'])
    #GUI information

    time1 = datetime.datetime.now()
    time1 = time1.replace(microsecond=0)

    #Get start time
    date = datetime.datetime.now()
    startmin = date.minute
    startsec = date.second
    mornData = 0

    quotes_single = TDSession.get_quotes(instruments=['SPY'])
    SPY_DATA = (quotes_single['SPY'])
    # Creating label widget
    timeLabel1_1 = Label(root, text="Time:")
    timeLabel1_2 = Label(root, text=time1)

    tickerLabel1_1 = Label(root, text="Ticker:")
    tickerLabel1_2 = Label(root, text=SPY_DATA['symbol'])

    priceLabel1_1 = Label(root, text="Last Price:")
    priceLabel1_2 = Label(root, text=SPY_DATA['lastPrice'])

    dayHighLabel1_1 = Label(root, text="Day High:")
    dayHighLabel1_2 = Label(root, text=SPY_DATA['highPrice'])

    dayLowLabel1_1 = Label(root, text="Day Low:")
    dayLowLabel1_2 = Label(root, text=SPY_DATA['lowPrice'])

    morningHighLabel1_1 = Label(root, text="Morning High:")
    morningHighLabel1_2 = Label(root, text="Morn_high")

    morningLowLabel1_1 = Label(root, text="Morning Low:")
    morningLowLabel1_2 = Label(root, text="Morn_low")

    fillLabel1_1 = Label(root, text="--------")
    fillLabel1_2 = Label(root, text="--------")
    fillLabel1_3 = Label(root, text="--------")
    fillLabel1_4 = Label(root, text="--------")

    apdHighLabel1_1 = Label(root, text="Approaching Daily High")
    apdHighLabel1_2 = Label(root, text="False")

    pushdHighLabel1_1 = Label(root, text="Pushing Daily High")
    pushdHighLabel1_2 = Label(root, text="False")

    apdLowLabel1_1 = Label(root, text="Approaching Daily Low")
    apdLowLabel1_2 = Label(root, text="False")

    pushdLowLabel1_1 = Label(root, text="Pushing Daily Low")
    pushdLowLabel1_2 = Label(root, text="False")

    apMornHighLabel1_1 = Label(root, text="Approaching Morning High")
    apMornHighLabel1_2 = Label(root, text="False")

    pushMornHighLabel1_1 = Label(root, text="Pushing Morning High")
    pushMornHighLabel1_2 = Label(root, text="False")

    apMornLowLabel1_1 = Label(root, text="Approaching Morning Low")
    apMornLowLabel1_2 = Label(root, text="False")

    pushMornLowLabel1_1 = Label(root, text="Pushing Morning Low")
    pushMornLowLabel1_2 = Label(root, text="False")
    #Row start value
    x = 0
    # shove it onto screen
    timeLabel1_1.grid(row=x, column=x)
    timeLabel1_2.grid(row=x+1, column=x)

    tickerLabel1_1.grid(row=x, column=x+1)
    tickerLabel1_2.grid(row=x+1, column=x+1)

    priceLabel1_1.grid(row=x, column=x+2)
    priceLabel1_2.grid(row=x+1, column=x+2)

    dayHighLabel1_1.grid(row=x, column=x+3)
    dayHighLabel1_2.grid(row=x+1, column=x+3)

    dayLowLabel1_1.grid(row=x, column=x+4)
    dayLowLabel1_2.grid(row=x+1, column=x+4)

    morningHighLabel1_1.grid(row=x, column=x+5)
    morningHighLabel1_2.grid(row=x+1, column=x+5)

    morningLowLabel1_1.grid(row=x, column=x+6)
    morningLowLabel1_2.grid(row=x+1, column=x+6)

    fillLabel1_1.grid(row=x, column=x+7)
    fillLabel1_2.grid(row=x+1, column=x+7)

    apdHighLabel1_1.grid(row=x, column=x+8)
    apdHighLabel1_2.grid(row=x+1, column=x+8)

    pushdHighLabel1_1.grid(row=x, column=x+9)
    pushdHighLabel1_2.grid(row=x+1, column=x+9)

    apdLowLabel1_1.grid(row=x, column=x+10)
    apdLowLabel1_2.grid(row=x+1, column=x+10)

    pushdLowLabel1_1.grid(row=x, column=x+11)
    pushdLowLabel1_2.grid(row=x+1, column=x+11)

    fillLabel1_3.grid(row=x, column=x+12)
    fillLabel1_4.grid(row=x+1, column=x+12)

    apMornHighLabel1_1.grid(row=x, column=x+13)
    apMornHighLabel1_2.grid(row=x+1, column=x+13)

    pushMornHighLabel1_1.grid(row=x, column=x+14)
    pushMornHighLabel1_2.grid(row=x+1, column=x+14)

    apMornLowLabel1_1.grid(row=x, column=x+15)
    apMornLowLabel1_2.grid(row=x+1, column=x+15)

    pushMornLowLabel1_1.grid(row=x, column=x+16)
    pushMornLowLabel1_2.grid(row=x+1, column=x+16)
    now_min = datetime.datetime.now()
    now_min = now_min.replace(microsecond=0)
    if now_min.hour == 10:
        if now_min.minute == 50:
            if now_min.second == 59:
                apMornHigh = SPY_DATA['highPrice'] - (SPY_DATA['lastPrice'] * .01)
                apMornLow = SPY_DATA['lowPrice'] + (SPY_DATA['lowPrice'] * .01)
                mornHigh = SPY_DATA['highPrice']
                mornLow = SPY_DATA['lowPrice']
                morningHighLabel1_2.config(text=mornHigh)
                morningLowLabel1_2.config(text=mornLow)
                mornData = 1
                print('joe')

    if now_min.second != startsec:
        timeLabel1_2.config(text=now_min)
        startsec = now_min.second
        priceLabel1_2.config(text=SPY_DATA['lastPrice'])
        dayHighLabel1_2.config(text=SPY_DATA['highPrice'])
        dayLowLabel1_2.config(text=SPY_DATA['lowPrice'])
        apdHigh = SPY_DATA['highPrice'] - ((SPY_DATA['highPrice']-SPY_DATA['lowPrice']) * .15)
        apdLow = SPY_DATA['lowPrice'] + ((SPY_DATA['highPrice']-SPY_DATA['lowPrice']) * .15)
        #spy approaching daily high
        if SPY_DATA['lastPrice'] >= apdHigh:
            if SPY_DATA['lastPrice'] < SPY_DATA['highPrice']:
                apdHighLabel1_2.config(text='TRUE')
        else:
            apdHighLabel1_2.config(text='False')
        #spy pushng daily high
        if SPY_DATA['lastPrice'] >= SPY_DATA['highPrice']:
            pushdHighLabel1_2.config(text='TRUE')
        else:
            pushdHighLabel1_2.config(text='False')
        # spy approaching daily low
        if SPY_DATA['lastPrice'] <= apdLow:
            if SPY_DATA['lastPrice'] > SPY_DATA['lowPrice']:
                apdLowLabel1_2.config(text='TRUE')
        else:
            apdLowLabel1_2.config(text='False')
        #spy pushng daily low
        if SPY_DATA['lastPrice'] <= SPY_DATA['lowPrice']:
            pushdLowLabel1_2.config(text='TRUE')
        else:
            pushdLowLabel1_2.config(text='False')

        if mornData == 1:
            # spy approaching morning high
            if SPY_DATA['lastPrice'] >= apMornHigh:
                if SPY_DATA['lastPrice'] < mornHigh:
                    apMornHighLabel1_2.config(text='TRUE')
            else:
                apMornHighLabel1_2.config(text='False')
                # spy pushing morning high
            if SPY_DATA['lastPrice'] >= mornHigh:
                pushMornHighLabel1_2.config(text='TRUE')
            else:
                pushMornHighLabel1_2.config(text='False')
                # spy approaching daily low
            if SPY_DATA['lastPrice'] <= apMornLow:
                if SPY_DATA['lastPrice'] > mornLow:
                    apMornLowLabel1_2.config(text='TRUE')
            else:
                apMornLowLabel1_2.config(text='False')
            # spy pushng daily high
            if SPY_DATA['lastPrice'] <= mornLow:
                pushMornLowLabel1_2.config(text='TRUE')
            else:
                pushMornLowLabel1_2.config(text='False')

                # run every min on the min
    if now_min.minute != startmin:
        timeLabel1_2.config(text=now_min)
        startmin = now_min.minute

    timeLabel1_2.after(400, mornhighstrat)

    root.mainloop()

mornhighstrat()