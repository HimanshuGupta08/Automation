import json
import os
import requests
from mailjet_rest import Client
import sys

Text = sys.argv[1]
Subject = sys.argv[2]

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
recipient_email = "himanshu.gupta@cloudeq.com"
email_data = {
    "Messages": [
        {
            "From": {
                "Email": "Opsbot-noreply@ext.mcdonalds.com",
                "Name": ""
            },
            "To": [
                {
                    "Email": recipient_email,
                    "Name": ""
                }
            ],
            "Subject": Subject,
            "TextPart": Text,
            "HTMLPart": ""
        }
    ]
}

api_url = "https://api.mailjet.com/v3.1/send"
mailjet = Client(auth=(api_key, api_secret))
response = requests.post(api_url, auth=mailjet.auth, json=email_data)

if response.status_code == 200:
    print("Email sent successfully.")
else:
    print(f"Email sending failed with status code: {response.status_code}")
    print(response.text)
