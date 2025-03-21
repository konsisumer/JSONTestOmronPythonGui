def fetch_json_data(url):
    import requests
    import json

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None

def send_json_data(url, data):
    import requests
    import json

    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None