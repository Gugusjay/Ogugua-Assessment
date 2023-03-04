import requests

def get_exoplanet_data():
    try:
        response = requests.get('https://exoplanet-data.com')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise ValueError(f"HTTP error occurred: {err}")
    except requests.exceptions.Timeout as err:
        raise ValueError(f"Timeout error occurred: {err}")
    except requests.exceptions.RequestException as err:
        raise ValueError(f"An error occurred: {err}")
