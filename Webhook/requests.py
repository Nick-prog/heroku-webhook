import Webhook
import json

def start(data):
    dict = data
    list = dict["data"]

    if(len(list) != 0):
        for total in range (len(list)):
            if(list[total].get("event").get("method") == "POST" and list[total].get("event").get("body") != ""):
                fieldValues = list[total].get("event").get("body").get("formSubmission").get("fieldValues") #Cycle through all 6 of the field values we acquire
                print(fieldValues)
