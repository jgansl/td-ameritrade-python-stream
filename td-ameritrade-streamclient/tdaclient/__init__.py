import requests
import typing

from client import Client
from utils import *

from dotenv import load_dotenv
from os import getenv, path
from td.client import TDClient

env_filepath = path.abspath(path.dirname(__file__))
env_location = path.join(env_filepath, '../.env.development')
load_dotenv(env_location)

client = Client()

# Create a new session, credentials path is required.
TDSession = TDClient(
   client_id        = getenv('TDA_CLIENT_ID'),
   redirect_uri     = getenv('TDA_REDIRECT_URI'),
   credentials_path = getenv('TDA_PATH_TO_CREDENTIALS_FILE')
)
#
# Login to the session
TDSession.login()

# Grab real-time quotes for 'MSFT' (Microsoft)
msft_quotes = TDSession.get_quotes(instruments=['MSFT'])

jprint(msft_quotes)

class Client(object):
   
   def __init__(self):
      pass

   def request(self):
      print('Client')
      return 'Client'


