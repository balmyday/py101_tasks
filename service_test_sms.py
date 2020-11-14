import time 
import logging
import requests
from requests.exceptions import (ConnectionError, HTTPError)
from datetime import datetime
import random
from dotenv import load_dotenv
import os 
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


TIMEOUT = 60
URL = 'https://python10.online/week4/api/'
SMS_GATE = '+12059463160'

NUMBERS =['+79104311743','+4915257092479']


load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

# setting up logger with output to console/file

log = logging.getLogger('check_availability')
log.setLevel(logging.DEBUG)

fh = logging.FileHandler('check_availability.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG) 

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

log.addHandler(fh)
log.addHandler(ch)

# defining a function to check if the service is available 

def check_availability(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except ConnectionError as e:
        log.error(f'Connection error: {e}')  
        return False 
    except HTTPError as e:
        log.error(f'HTTP error: {e.response.status_code}')  
        return False

    log.debug(f'{url} looks available')
    return True 

# defining fuction to send sms using Twilio

def send_sms(message_to_send):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for n in NUMBERS:
        log.debug(f'Sending message {message_to_send} to number {n} ')
        try:
            message = client.messages.create(
                body=message_to_send,  
                from_=SMS_GATE,  
                to=n,  
                )
            log.debug('message sent')
        except TwilioRestException as e:
            log.warning(f'cannot send message: {e}')
                 
            
# code to check the status of the server and send a message 

was_available = True 

while True:
    log.debug('--------------------------------')
    now_available = check_availability(URL)
    if was_available and not now_available:
        log.warning(f'{URL} became unavailable')
        send_sms('Service not available')
    if now_available and not was_available:
        log.warning(f'{URL} is available again')
        send_sms('Service available again')
    was_available = now_available 

    time.sleep(TIMEOUT)

    
