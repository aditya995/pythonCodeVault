from urllib.request import urlopen

def is_internet():
    try:
        urlopen('https://www.google.com', timeout=3)
        return True
    except Exception as Error:
        print('Error->', Error)
        return False


if is_internet():
    print("Connected to the Internet")
else:
    print("Not connected to the Internet")