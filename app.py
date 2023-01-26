

from flask import Flask, send_file, jsonify, request
#import utility, carbon
#from flask_cors import CORS
import asyncio
import os
import json
import requests
import flask
from flask import Flask, request,jsonify
import asyncio
from solver import Solver
import random, time

apikey = "slapcord-cc92b90d-73f7-14d6-40ff-e6480e5cc410"


app = Flask(__name__)

async def getcap(sk,s,key=None):
    #bk = random.choice(bks)
    uid = "not uwu at all"
    # if key != "1":
    #   apikey = random.choice(keys)
    # else:
    site = s#"https://discord.com/api/oauth2/authorize"
    sitekey = sk#"f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"
    if uid == "" or apikey == "" or site == "" or sitekey == "":
        print("You need to set uid apikey site and sitekey first.")
        return False
    config = {
        "solver": {
            "uid": uid,#Do not modify this
            "apikey": apikey#Do not modify this
        },
        "hcaptcha": {
            "url": site,#Do not modify this
            "sitekey": sitekey#Do not modify this
        },
        "headless": False,
        #"bk": bk
      # browser visibility
    }
    solver = Solver(config["hcaptcha"]["url"], config["hcaptcha"]["sitekey"], config["solver"]["uid"],config["solver"]["apikey"], config["headless"])
    result = await solver.solveCaptcha()
  #sl = Solver("discord.com", "sk", "no-n", "ak")
  #result = await sl.solveCaptcha()
  #result = await sl._getCaptcha()
    print(result)
    if result:
      print("solved")
      return result
    else:
      print("fail")
      return await getcap(sk,s)

#cap = asyncio.run(getcap("f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34","https://discord.com/api/oauth2/authorize"))
#print(cap)

@app.route("/")
def main():
  return "hcaptcha solver"

@app.route("/solve")
def index():
  if request.headers["Authorization"] != "Exploit321$":
    return "None"
  args = request.args
  sitekey = args.get('site_key')
  site = args.get('site_url')
  time1 = time.time()
  cap = asyncio.run(getcap(sitekey,site,apikey))
  time2 = time.time()
  return jsonify({"time": time2-time1, "key": cap})

@app.route("/balance")
def balancex():
  if request.headers["Authorization"] != "Exploit321$":
    return "None"
  balance = requests.get('https://free.nocaptchaai.com/balance', headers={'apikey': apikey})
  print(balance.json())
  return str(balance.json())




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)