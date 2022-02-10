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

def uploaded_documents(data):
    list = data["formSubmission"].get("fieldValues")
    
    if(len(list) != 0):
        name = str(list.get("Name")).strip("[']")
        email = str(list.get("Email")).strip("[']")
        applicant = str(list.get("Applicant ID (K0012345)")).strip("[']")
        description = str(list.get("Describe the document(s) you are loading.")).strip("[']")
        upload = str(list.get("No file chosen")).strip("[']")
        department = str(list.get("Submit your document(s) to the follwoing department.")).strip("[']")
        print("Name: ", name, "\nEmail: ", email, "\nK#: ", applicant, "\nDescription: ", description, "\nUpload: ", upload, "\nDepartment: ", department)
