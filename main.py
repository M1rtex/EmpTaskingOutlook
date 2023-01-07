from graph_api import *
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get('APP_ID')
SCOPES = ['Mail.Read']

ACCESS_TOKEN = generate_access_token(app_id=APP_ID, scopes=SCOPES)

emails = get_messages(access_token=ACCESS_TOKEN)

for email in emails:
    print(f"""
        Sender: {email['sender']['emailAddress']['name']} {email['sender']['emailAddress']['address']}
        Subject: {email['subject']}
        BodyPreview: {email['bodyPreview']}
    """)
