import requests

def plaid_get_Transactions(CLIENT_ID, SECRET, token):
    print('get all transactions ')
    url = 'https://development.plaid.com/transactions/get'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "client_id": F"{CLIENT_ID}",
        "secret": f"{SECRET}",
        "access_token": f'{token}',
        "start_date": "2022-11-02",
        "end_date": "2023-11-04",
        "options": {
            "count": 3,
            "offset": 0
        }
    }

    # Transaction data received
    transaction_data = requests.post(url, headers=headers, json=data).json()['transactions']
    return transaction_data


def plaid_get_account_balance(CLIENT_ID, SECRET, token):
    print('get account balance ')
    url = 'https://development.plaid.com/accounts/balance/get'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "client_id": F"{CLIENT_ID}",
        "secret": f"{SECRET}",
        "access_token": f'{token}',
        "options": {
            "account_ids": ['X1YAdz9x9Zsj6J19JDeRc736mB1Aw7iaMmvkM']
        }

    }
    # Account balance received
    account_balance = requests.post(url, headers=headers, json=data).json()
    return account_balance