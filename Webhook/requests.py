import wget
import os
import Webhook
from datetime import datetime

def month_year():
    month_year = datetime.now()
    month_year_format = month_year.strftime("%B %Y")
    return month_year_format #Returns the current month and year

def today():
    today = datetime.now()
    today_format = today.strftime("%m.%d.%Y")
    return today_format #Returns the current month/date/year

def start(data):
    list = data["formSubmission"].get("fieldValues")
    
    if(len(list) != 0):
        name = str(list.get("Name")).strip("[']")
        email = str(list.get("Email")).strip("[']")
        applicant = str(list.get("Applicant ID (K0012345)")).strip("[']")
        description = str(list.get("Describe the document(s) you are loading.")).strip("[']")
        upload = str(list.get("No file chosen")).strip("[']")
        department = str(list.get("Submit your document(s) to the follwoing department.")).strip("[']")
        path = "//fs16.tamuk.edu/ds$/Admissions/Documents for Imaging/Clive/%s/%s/%s" %(Webhook.month_year(), Webhook.today(), applicant.replace(" ", ""))
        Webhook.download(name, email, applicant, description, upload, department, path)

def download(name, mail, applicant, description, upload, department, path, method, first, last):
    url = str(upload).replace("\\", "/")

    doc = wget.download(url, path)
