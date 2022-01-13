import Webhook

def start(data):
    print(data["formSubmission"].get("fieldValues"))
