import requests
import pandas as pd
import random

def send_email(api_key, domain, to, subject, body):
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={"from": f"Mailgun Sandbox <postmaster@{domain}>",
              "to": to,
              "subject": subject,
              "text": body})

# Load leads
leads = pd.read_csv('/Users/roxton/.openclaw/workspace/CRM/leads.csv')

# Professional Outreach Templates
templates = [
    "Hello {business_name}, while reviewing most businesses in the Las Vegas area, I noticed that your company offers excellent services. I was curious, do customers usually connect with you through social media channels like Instagram?",
    "Hi {business_name}, I recently came across your business online and was impressed. Would you mind if I shared a suggestion regarding how customers might be reaching you?",
    "Greetings {business_name}, I discovered your business while researching local providers. It appears that some customers might still be reaching out directly. Is that often the case for you?",
]

if __name__ == "__main__":
    MAILGUN_API_KEY = 'YOUR_API_KEY'  # Replace with your API key
    MAILGUN_DOMAIN = 'YOUR_DOMAIN'      # Replace with your domain
    
    total_leads = len(leads)
    print(f"Total leads to process: {total_leads}")

    for index, lead in leads.iterrows():
        try:
            print(f"Processing lead: {lead['business_name']}")  # Debugging line
            if 'outreach_eligible' in lead and lead['outreach_eligible'] == 'True':  # Check if the lead can be contacted
                randomized_template = random.choice(templates)
                subject = "Improve Your Web Presence!"
                body = randomized_template.format(business_name=lead['business_name'])
                
                response = send_email(MAILGUN_API_KEY, MAILGUN_DOMAIN, lead['public_email'], subject, body)
                print(f"Email sent to {lead['public_email']} - Status Code: {response.status_code}")
            else:
                print(f"Skipping lead {lead['business_name']} due to 'outreach_eligible' = {lead.get('outreach_eligible', 'Not Found')}")
        except KeyError as e:
            print(f"Skipping lead {lead['business_name']} due to missing field: {str(e)}")