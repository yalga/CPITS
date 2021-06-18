# I watched a youtube video, research on twilio site and other articles. Finally I made it. Thank you RaphaBot
import os
from twilio.rest import Client


account_sid =  'AC61ab867f5cfd714a74d926dd7f075f7c'
auth_token = '18a145f5d626bc98394b373e62ba470d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="This message is from Getachew Ferede. CPITS is amazing. Thank you Trend Micro",
                     from_='+19704441341',
                     to='+12023527923'
                 )

print(message.sid)
