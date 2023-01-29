import requests, os 

os.system("cls")

site_key = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"
site_url = "https://discord.com"

solver_api = "https://hcaptcha-solver.notexploit.tech/solve"

def get_solved_captcha(site_key, site_url):
    print("[+] Solving captcha for %s" % site_url)
    api = solver_api + "?site_key=%s&site_url=%s" % (site_key, site_url)
    r = requests.get(api, headers={"Authorization": "Exploit321$"})
    print(r.text)
    print("\n\n")
    print("[+] Captcha Solved")
    print("[+] Runtime: %s" % r.json()["time"])
    return r.json()["key"]

captcha_key = get_solved_captcha(site_key, site_url)
print(captcha_key)


