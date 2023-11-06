from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import time
import base64

app = Flask(__name__)

@app.route('/krafty', methods=['POST'])
def api_message():
    data = request.data
    print(data)
    return "already run"

timestamp = str(time.strftime("%Y%m%d%H%M%S"))

password = base64.b64encode(bytes(u'601754' + 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' + timestamp, 'UTF-8'))

consumer_key = "f86v9yOOe0EwAT1CGUQnvXEwdHvUPSFL"
consumer_secret = "2wRTiDK2ApKiDUkI"
api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

access_token = r.json().get("access_token")

print(access_token)

api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = {"Authorization": f"Bearer {access_token}"}
request = {
    "BusinessShortCode": "601754",
    "Password": "{}".format(password),
    "Timestamp": "{}".format(timestamp),
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "100",
    "PartyA": "0113515227",
    "PartyB": "501675",
    "PhoneNumber": "0013515227",
    "CallBackURL": "https://kraftycoder.ml/callback.html",
    "AccountReference": "account",
    "TransactionDesc": "test"
}

response = requests.post(api_url, json=request, headers=headers)

print(response.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
