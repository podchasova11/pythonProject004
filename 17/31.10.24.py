import http.client
import json

conn = http.client.HTTPSConnection("example.com")
payload = json.dumps({
   "cc": "<Country Code>",
   "cert": "<Valid Cert from Business Manager>",
   "method": "sms",
   "phone_number": "<Phone Number>",
   "pin": "<Two-Step Verification PIN"
})
headers = {
   'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
   'Content-Type': 'application/json',
   'Accept': '*/*',
   'Host': 'example.com',
   'Connection': 'keep-alive'
}
conn.request("POST", "/v1/account", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
