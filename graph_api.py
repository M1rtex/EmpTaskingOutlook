import os
import sys
import requests
import msal
import webbrowser
from datetime import datetime
import json

GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0'


def generate_access_token(app_id, scopes, main_window) -> dict:
    access_token_cache = msal.SerializableTokenCache()

    # read the token file
    if os.path.exists('data/ms_token.json'):
        access_token_cache.deserialize(open("data/ms_token.json", "r").read())
        token_detail = json.load(open('data/ms_token.json', ))
        token_detail_key = list(token_detail['AccessToken'].keys())[0]
        token_expiration = datetime.fromtimestamp(int(token_detail['AccessToken'][token_detail_key]['expires_on']))
        if datetime.now() > token_expiration:
            os.remove('data/ms_token.json')
            access_token_cache = msal.SerializableTokenCache()

    client = msal.PublicClientApplication(client_id=app_id, token_cache=access_token_cache)

    accounts = client.get_accounts()
    if accounts:
        token_response = client.acquire_token_silent(scopes, accounts[0])
    else:
        # authenticate your account as usual
        flow = client.initiate_device_flow(scopes=scopes)
        if flow['user_code']:
            print(111)
            print(222)
            main_window.login_app.login_code_lable.setText(flow['user_code'])
            print(flow['user_code'])
            print(333)
            webbrowser.open('https://microsoft.com/devicelogin')
            token_response = client.acquire_token_by_device_flow(flow)
        else:
            sys.exit(flow)
    with open('data/ms_token.json', 'w') as _f:
        _f.write(access_token_cache.serialize())
    return token_response


def get_messages(access_token: dict, folder='inbox', select='subject,sender,bodyPreview', top=10, *args,
                 **kwargs) -> list:
    headers = {
        'Authorization': f"{access_token['token_type']} {access_token['access_token']}",
    }
    params = {
        'top': top,
        'select': select,
    }

    response = requests.get(GRAPH_API_ENDPOINT + f"/me/mailFolders/{folder}/messages", headers=headers, params=params)
    if response.status_code == 200:
        emails = response.json()['value']
        return emails
    elif response.status_code != 200:
        raise Exception(response.text)


def send_text_mail(access_token: dict, subject: str, body: str, recipient: str):
    request_url = GRAPH_API_ENDPOINT + '/me/sendmail'
    headers = {
        'Authorization': f"{access_token['token_type']} {access_token['access_token']}",
        'Content-Type': 'application/json',
    }
    request_body = {
        'message': {
            'subject': subject,
            'body': {
                'contentType': 'text',
                'content': body
            },
            'toRecipients': [
                {
                    'emailAddress': {
                        'address': recipient
                    }
                }
            ]
        }
    }
    res = requests.post(request_url, data=json.dumps(request_body), headers=headers)
    return res


if __name__ == '__main__':
    raise SystemExit
