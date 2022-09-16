import requests

timeout = 1

def check():
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        # Do something
        print('The internet connection is active')
    except requests.ConnectionError:
        # Do something
        print("The internet connection is down")