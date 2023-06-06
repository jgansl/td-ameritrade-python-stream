import asyncio
import csv
import io
import json
import os
import textwrap
import unicodedata
import urllib

from typing import List
from typing import Union

import websockets
import websockets.client
#from td.enums import CSV_FIELD_KEYS
from constants import CSV_FIELD_KEYS
#from td.enums import CSV_FIELD_KEYS_LEVEL_2
from constants import CSV_FIELD_KEYS_LEVEL_2
#from td.enums import STREAM_FIELD_IDS
from constants import STREAM_FIELD_IDS


class TDStreamerClient():
   def __init__(
      self, 
      websocket_url: str, 
      user_principal_data: dict, 
      credentials: dict
   ) -> None:
      return