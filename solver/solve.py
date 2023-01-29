import sys,hsolver;

try:
    site_key = sys.argv[1];
    site_url = sys.argv[2];
    proxy_url =  sys.argv[3];
except Exception as e:
    print(f'python3 {__name__}.py <site_key> <site_url> <proxy_url>')

try:
    print(hsolver.Solver(proxy_url, site_key, site_url).solve_captcha())
except Exception as e:
    print('False')

#captcha_key = os.popen(f'python solve.py {site_key} {site_url} {proxy}').read().strip()