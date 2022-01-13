import Webhook

def start(data):
    print(list(data["formSubmission"].get("fieldValues")))
