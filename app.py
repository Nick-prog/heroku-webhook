import Webhook
import flask
from flask import Flask, request, abort

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def get_webhook():
    if request.method == 'POST':
       data = request.json
       Webhook.start(data)
    else:
        abort(400)
        
if __name__ == '__main__':
    app.run()
