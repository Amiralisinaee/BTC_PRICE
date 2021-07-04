import requests
from json import loads
from notify import notification
from os import system


def price():
    api = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    req = requests.get(api)
    json_con = req.text
    json_loader = loads(json_con)
    api_response = json_loader['bpi']
    response_st_sm = api_response['USD']
    response_nd_sm = response_st_sm['rate']


    return response_nd_sm


def send_mssg():
    mssg = price()
    notification(mssg, title = 'BTC')
    system('sleep 300')
    send_mssg()

send_mssg()