import Webhook

def start(data):
    list = data["formSubmission"].get("fieldValues")
    
    if(len(list) != 0):
        name = str(list.get("Name")).strip("[']")
        print(name)
