import os, sys, threading, httpx, time, logging, flask, datetime, ctypes,threading, random
import requests as xrequests
from . import hcaptcha, logger
import hcaptcha_challenger as aaa

class Solver(object):
    def __init__(self, proxy, site_key, site_url):
        self.proxy = proxy
        self.site_key = site_key
        self.site_url = site_url
    
    def answer_question(self, images, urls):
        x = self.challenger.classify(prompt=self.topic, images=list(images.values()))
        a = 0
        for ans in x:
            try:
                if ans == True:
                    self.client.answer(urls[a])
            except Exception as e:
                print(e)
            a += 1
        
    def solve_captcha(self):
        self.challenger = aaa.new_challenger()
        self.client = hcaptcha.Challenge(site_key=self.site_key, site_url=self.site_url, proxy=self.proxy, ssl_context=__import__("ssl")._create_unverified_context(), timeout=5)
        
        self.task_thread = []
        
        if self.client.token: sys.exit()
        try:
            self.topic = self.client.question["en"].split('Please click each image containing a ')[1].split('.')[0]
        except:
            self.topic = self.client.question["en"].split('Please click each image containing an ')[1].split('.')[0]
        logger.Question(f'Solving hCaptcha... ({self.topic})')

        images = {}
        urls = {}

        a = 0
        for tile in self.client:
            images[a] = xrequests.get(tile).content
            urls[a] = tile
            a += 1
        
        self.answer_question(images, urls)
        
        token = self.client.submit()
        return token