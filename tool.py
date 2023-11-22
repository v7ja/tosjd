import requests,sys,os,json,random 
from rich import print as SS
from rich.panel import Panel as g
from rich.console import Console
from user_agent import generate_user_agent
Ss = Console()
ok,tok,bad=0,0,0
AB_KH='\033[37m'
AH_T='\033[91m'
AKH_T='\033[92m'
AS_F='\033[93m'
print(AH_T)
rr="By : aBooD YaBh"                           
print(rr)
id=input(f'{AB_KH}   ID  „:')
token=input('   TOKIN  „:')
os.system('clear')
print(rr)
def us():
	saa="1234567890qwertyuiopasdfghjklzxcvbnm"
	see="._"
	while True:
	       s = str(''.join((random.choice(saa) for i in range(1))))
	       ss = str(''.join((random.choice(saa) for i in range(1))))
	       sss = str(''.join((random.choice(saa) for i in range(1))))
	       ee = str(''.join((random.choice(see) for i in range(1))))
	       e = str(''.join((random.choice(saa) for i in range(1))))
	       h = (ss+ee+s+ee+sss)
	       hh = (sss+e+s+sss+sss)
	       j= (h, hh)
	       user = random.choice(j)
	       sgg(user)
def sgg(user):
    gd = str(generate_user_agent())
    global ok,tok,bad
    sys.stdout.write(f'\r   {AKH_T}OK {ok}{AB_KH} - {AH_T}BAD {bad} {AB_KH}- {AS_F}TOKEN {tok} {AKH_T}'),
    sys.stdout.flush()
    headers = {'Host':'www.instagram.com','content-length':'85','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'81f3a3c9dfe2','content-type': 'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':f'{gd}','x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9','cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL','cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425','cookie':'ig_nrcb=1'
	}
    data= f'email=sgahahfdggsdfs%40gmail.com&username={user}&first_name=&opt_into_one_tap=false'
    res = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/', headers=headers, data=data).text
#    res_dict = json.loads(res)
    if "status" in res and "fail" in res:
    	bad+=1
    elif '"errors": {"username":' in res or '"code": "username_is_taken"' in res:
    	tok+=1
    else:
    	ok+=1
    	print('\n')
    	print('   '*10)
    	gg = f'         [green] \nUSER • {user} '
    	SS(g(gg))
    	tle = f"  New UserName : {user}\n By : @c_7c7"
    	requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={tle}')
#us()
import threading
for i in range(20):
at=threading.Thread(target=us,args=())
 a.start()
