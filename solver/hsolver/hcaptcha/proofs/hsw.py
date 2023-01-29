from os.path import dirname
import os
import httpx
import requests
def get_proof(req):
    s = requests.Session()
    #res = requests.get(f"http://127.0.0.1:8080/hsw?hsw="+req, timeout=None).text
    res = s.get(f"http://127.0.0.1:2030/bypass?hsw="+req, timeout=None).text
    return res
