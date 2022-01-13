import Webhook
import json
import wget
import os.path
import os
import ssl
from datetime import datetime

def total(method):
    Data = Webhook.id(method)
    dict = json.loads(Data)
    list = dict["page_info"]
    return list.get("total_count")

def month_year():
    month_year = datetime.now()
    month_year_format = month_year.strftime("%B %Y")
    return month_year_format #Returns the current month and year

def today():
    today = datetime.now()
    today_format = today.strftime("%m.%d.%Y")
    return today_format #Returns the current month/date/year

def start(GET):
    Data = GET
    dict = json.loads(Data)
    list = dict["data"]

    if(len(list) != 0):
        for total in range (len(list)):
            if(list[total].get("event").get("method") == "POST" and list[total].get("event").get("body") != ""):
                fieldValues = list[total].get("event").get("body").get("formSubmission").get("fieldValues") #Cycle through all 6 of the field values we acquire
                print(fieldValues)
