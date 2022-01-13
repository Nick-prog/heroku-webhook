import Webhook
import http.client
import json

IDs = {}

def GET():
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/%s/event_summaries?expand=event' %(Webhook.__sourceTest__), '', {
            'Authorization': '%s' %(Webhook.__authorization__)})
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data #Returns JSON Snipper metadata for every entry
