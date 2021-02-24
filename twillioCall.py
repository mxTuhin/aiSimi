import os
from twilio.rest import Client

account_sid= "AC009a1d5c4127eee9ec88d5e5969a6587"
auth_token = "a9b268e5c4bfce57f8771943f8a6fd13"

client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+8801678710456",
    from_="+12563636244",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)