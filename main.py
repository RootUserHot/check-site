import requests
import argparse
import time
import webbrowser

parser = argparse.ArgumentParser(description='desc')
parser.add_argument('a', help='Write site without https://')
parser.add_argument('b', help='Write timeout check site')
args = parser.parse_args()

def manageSite(a, b):
    result = False
    try:
        result = requests.get(str("{}{}".format('https://', a))).ok
        if result is False:
            print('Checking...')
            timeCheck = round(time.time()) + int(b)
            while True:
                if timeCheck <= round(time.time()):
                    result = requests.get(str("{}{}".format('https://', args.a))).ok
                    timeCheck + int(b)
                    if result:
                        webbrowser.open(str("{}{}".format('https://', args.a)))
                        break
    except:
        print('Checking...')
        time.sleep(int(b))
        manageSite(args.a, args.b)
    if result:
        exit('Site is available')

if __name__ == '__main__':
    while True:
        input(manageSite(args.a, args.b))