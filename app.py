import Webhook
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Welcome!</h1>"

@app.route('/metadata', methods=['GET'])
def get_webhook():
    if request.method == 'GET':
        return jsonify({
            "MESSAGE" : "Connection confirmed.",
            "METHOD": "GET"
        })

@app.route('/webhook', methods=['POST'])
def post_webhook():
    if request.method == 'POST':
        data = request.json
        #Webhook.uploaded_documents(data)
        print(data)
        return jsonify({
            "MESSAGE" : "Connection confirmed.",
            "METHOD": "POST"
        })
        
if __name__ == '__main__':
    app.run(threaded=True)
