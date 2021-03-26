#!/usr/bin/env python
# coding: utf-8

# # Stock tracker sending email alerts 
#https://medium.com/illumination/how-to-build-a-stock-price-alert-using-python-d7d61ec12f2#https://docs.python.org/3/library/email.examples.html
#How to Create and use app passwords for gmail 


#Go to your Google Account.
#On the left navigation panel, choose Security.
#On the 'Signing in to Google' panel, choose App passwords. ...
#At the bottom, choose Select app and choose the app that you're using.
#Choose Select device and choose the device that you're using.
#Choose Generate.
# In[9]:


import pandas as pd #data manipulation and analysis package
from alpha_vantage.timeseries import TimeSeries #enables data pull from Alpha Vantage
#import matplotlib.pyplot as plt #if you want to plot your findings
import time
import smtplib #enables you to send emails

import schedule
import time
from datetime import datetime


# In[16]:


def job():

    #Getting the data from alpha_vantage
    ts = TimeSeries(key='7R5HTNHSODF74G1Y', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
    #We are currently interested in the latest price
    close_data = data['4. close'] #The close data column
    last_price = close_data[0] #Selecting the last price from the close_data column
    #Check if you're getting a correct value
    print(last_price)
    #Set the desired message you want to see once the stock price is at a certain level
    sender_email = "lidget987@gmail.com" #The sender email
    rec_email = "caliverp123@hotmail.com" #The receiver email
    password = ("Qwjhbnwzzxqowahk")#The password to the sender email
    message = "MSFT STOCK ALERT!!! The stock is at above price you set " + "%.6f" % last_price #The message you want to send
    target_sell_price = 250 #enter the price you want to sell at
    if last_price > target_sell_price:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('lidget987@gmail.com', 'Qwjhbnwzzxqowahk') #logs into your email account
        print("Login Success")#confirms that you have logged in succesfully
        server.sendmail('lidget987@gmail.com', 'caliverp123@hotmail.com', 'Lock you')#send the email with your custom mesage
        print("Email was sent") #confirms that the email was sent
    else:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('lidget987@gmail.com', 'Qwjhbnwzzxqowahk') #logs into your email account
        print("Login Success2")#confirms that you have logged in succesfully
        server.sendmail('lidget987@gmail.com', 'caliverp123@hotmail.com', 'stock price is below target')#send the email with your custom mesage
        print("Email was sent2") #confirms that the email was sent



    
    
schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
#schedule.every().day.at('13:58').do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute


# !pip install alpha_vantage

# In[8]:





# In[ ]:




