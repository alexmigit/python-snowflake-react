import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Slack webhook URL from environment variables
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

# Function to send a notification to Slack
def notify_slack(message):
    if not SLACK_WEBHOOK_URL:
        raise ValueError("SLACK_WEBHOOK_URL is not set in the environment variables.")
    
    # Prepare the payload for the Slack message
    payload = {
        "text": message,
        "username": "Manufacturing ELT Bot",
        "icon_emoji": ":robot_face:"
    }
    
    # Send the POST request to the Slack webhook URL
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")
    