from logging import DEBUG
from typing import Dict
from df_response_lib import *
from flask import Flask, request
from flask.logging import create_logger
from flask import jsonify
from dialogflow_fulfillment import WebhookClient
import json

#app = Flask(__name__)       # Initializing our Flask application
app = Flask(__name__)
# logger = create_logger(app)
# logger.setLevel(DEBUG)

ACCESS_TOKEN = 'GENERATED_TOKEN_FROM_FACEBOOK'
VERIFY_TOKEN = 'UNIQE_TOKEN'
def handler(agent: WebhookClient) -> None:
    """Handle the webhook request.."""
    agent.add('How are you feeling today?')
    agent.add("Happy")


@app.route('/', methods=['POST'])
def webhook() -> Dict:
    """Handle webhook requests from Dialogflow."""
    # Get request body
    request_ = request.get_json(force=True)

    # print("This is the request",r)

    # Log request headers and body
    # logger.info(f'Request headers: {dict(request.headers)}')
    # logger.info(f'Request body: {request_}')

    f = open('storeInfo.json',)
    data = json.load(f)

    text_body = json.loads(request.data.decode("utf-8"))
    # print(text_body['queryResult'])
    day = text_body['queryResult']['parameters']['day']
    print(day)
    service = text_body['queryResult']['parameters']['service-type']

    for opt in  data[service+"Hours"]:
        if day.lower() == opt["day"].lower():

            return_open_time =  opt["openTime"]
            return_close_time =  opt["closeTime"]

    # Handle request
    # agent = WebhookClient(request_)
    # agent.handle_request(handler)

    # upload_blob("foliox","download.png","img.png")
#     reply = {
#   "facebook": {
#     "attachment": {
#       "type": "image",
#       "payload": {
#         "url": "https://storage.googleapis.com/foliox/img.png"
#       }
#     }
#   }
# }

#     reply = {
#             "fulfillmentMessages": [
#   {
#         "image": {
#           "imageUri": "https://storage.googleapis.com/foliox/img.png"
#         },
#         "platform": "FACEBOOK"
#       },

#       {
#     "text": {
#       "text": [
#         "We could find few matching products based on your query"
#       ]
#     },
#     "platform": "FACEBOOK"
#   },
#   {
#     "text": {
#       "text": [
#         "We could find few matching products based on your query"
#       ]
#     },
#     "platform": "TWILIO"
#   },
#   {
#     "text": {
#       "text": [
#         "We could find few matching products based on your query"
#       ]
#     }
#   }

# ]
#         }

    return {
        'fulfillmentText': 'We are open from {} to {} on {}.'.format(return_open_time,return_close_time,day)
    }
    # return jsonify(reply)
    

    # logger.info(f'Response body: {agent.response}')
    # return jsonify(reply)


    # Log response body
    

    # return agent.response


if __name__ == '__main__':
    app.run(debug=True)
