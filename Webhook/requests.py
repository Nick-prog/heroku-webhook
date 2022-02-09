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
        mail = str(list.get("Email")).strip("[']")
        applicant = str(list.get("Applicant ID (K0012345)")).strip("[']")
        description = str(list.get("Describe the document(s) you are loading.")).strip("[']")
        upload = str(list.get("No file chosen")).strip("[']")
        department = str(list.get("Submit your document(s) to the follwoing department.")).strip("[']")
        #path = "//fs16.tamuk.edu/ds$/Admissions/Documents for Imaging/Clive/%s/%s/%s" %(Webhook.month_year(), Webhook.today(), applicant.replace(" ", ""))
        path = "C:/Users/KUNRR004/Downloads/%s/%s/%s" %(Webhook.month_year(), Webhook.today(), applicant.replace(" ", ""))
        Webhook.download(name, mail, applicant, description, upload, department, path, 1, "None", "None")

def download(name, mail, applicant, description, upload, department, path, method, first, last):
    url = str(upload).replace("\\", "/")
    filename = path + "/" + os.path.basename(url) #Acquire the filename

    if not os.path.exists(path): #Does a folder currently exist for this student?
        os.makedirs(path) #If not, create one...
        option = os.path.exists(filename)
        download_sent_file(url, path, applicant, description, option, method) #Downloads the user's sent file
        download_info_file(path, applicant, name, mail, department, first, last, method) #Creates a txt file based on the user's information
    else: #Else store the file in the student's folder
        option = os.path.exists(filename)
        download_sent_file(url, path, applicant, description, option, method)
        download_info_file(path, applicant, name, mail, department, first, last, method)

def download_sent_file(url, path, applicant, description, option, method):
    index = 0
    ssl._create_default_https_context = ssl._create_unverified_context

    doc = wget.download(url, path)
    old_file = os.path.join(path, doc)
    ext = os.path.splitext(doc)

    #Upload Documents Webhook download method
    if(option == False and method == 1): #File doesn't exist yet in the given folder?
        if(ext == ""):#File has special characters preventing proper capturing of the extension
            new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description))
            while(os.path.exists(new_file) == True): #File now exists...
                new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + Webhook.exists(index))
                index += 1
        else:
            new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + ext[1])
            while(os.path.exists(new_file) == True): #File now exists...
                new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + Webhook.exists(index) + ext[1])
                index += 1
    elif(option == True and method == 1):#File does exist in the given folder?
        if(ext == ""):#File has special characters preventing proper capturing of the extension
            new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description))
            while(os.path.exists(new_file) == True): #Need to index beforehand to prevent crashing
                index += 1
                new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + Webhook.exists(index))
        else:
            new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + Webhook.exists(index) + ext[1])
            while (os.path.exists(new_file) == True): #Need to index beforehand to prevent crashing
                index +=1
                new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + Webhook.exists(index) + ext[1])

    #Fee Waiver Request Webhook download method
    elif(option == False and method == 2):#File doesn't exist yet in the given folder?
        if(ext == ""):#File has special characters preventing proper capturing of the extension
            new_file = os.path.join(path, applicant + "_AFWR")
            while(os.path.exists(new_file) == True):#File now exists...
                new_file = os.path.join(path, applicant + "_AFWR" + Webhook.exists(index))
                index += 1
        else:
            new_file = os.path.join(path, applicant + "_AFWR" + ext[1])
            while(os.path.exists(new_file) == True):#File now exists...
                new_file = os.path.join(path, applicant + "_AFWR" + Webhook.exists(index) + ext[1])
                index += 1
    elif(option == True and method == 2):#File does exist in the given folder?
        if(ext == ""):#File has special characters preventing proper capturing of the extension
            new_file = os.path.join(path, applicant + "_AFWR" + Webhook.exists(index))
            while (os.path.exists(new_file) == True):#Need to index beforehand to prevent crashing
                index+=1
                new_file = os.path.join(path, applicant + "_AFWR" + Webhook.exists(index))
        else:
            new_file = os.path.join(path, applicant + "_AFWR" + Webhook.exists(index) + ext[1])
            while (os.path.exists(new_file) == True):#Need to index beforehand to prevent crashing
                index+=1
                new_file = os.path.join(path, applicant + "_AFWR" + Webhook.exists(index) + ext[1])

    os.rename(old_file, new_file)

def download_info_file(path, applicant, name, mail, department, first, last, method):
    if(method == 1): #Uploaded documents clive info form
        file_name = f"{path}" + "/" + f"{applicant}" + "_" + "info.txt"
        file_info = open(file_name, "w")
        file_info.write("Name: " + name + "\n"
        + "Email: " + mail + "\n"
        + "Applicant: " + applicant + "\n"
        + "Department: " + department)
    else: #Fee Waiver request clive info form
        file_name = f"{path}" + "/" + f"{applicant}" + "_" + "info.txt"
        file_info = open(file_name, "w")
        file_info.write("First: " + first + "\n"
        + "Last: " + last + "\n"
        + "Email: " + mail + "\n"
        + "Applicant: " + applicant + "\n")
        
    file_info.close()
