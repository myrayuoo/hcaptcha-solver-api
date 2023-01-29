from .http_ import HTTPClient
from .agents import random_agent
from .utils import is_main_process, parse_jsw
import json
import os

def download_script_files():
    files = ("hsw.js", )

if is_main_process():
    download_script_files()