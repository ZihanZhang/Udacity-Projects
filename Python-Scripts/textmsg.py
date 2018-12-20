from twilio.rest import TwilioRestClient

account_sid = "AC26ef542424d68fdfa53557c159d69a83" # Your Account SID from www.twilio.com/console
auth_token  = "cd7fa03a31d9934126424f197a22671e"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Dudu is a bitch",
    to="+18572729469",    # Replace with your phone number
    from_="+16174874046") # Replace with your Twilio number

print(message.sid)