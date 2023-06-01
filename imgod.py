Time=(0)
auth=["",""]#اوث لیست
from arsein import Messenger
from time import  sleep
from TyroBot import Bot
Z = '\033[1;31m' #قرمز
X = '\033[1;33m' #زرد
F = '\033[2;32m' #سبز
guid=input(f"{X}guid:{F}")
text= input(f"{X}text send:{F}")
num =0
while 1:
	for u in auth:
		try:
			bot=Messenger(u)
			bott=Bot(u)
			name= bott.get_me()['first_name']
			sleep(Time)
			bot.sendMessage(guid,text)
			num +=1
			print(f'''☆☆☆☆☆☆☆☆☆☆☆☆☆☆\n{X}send{F}{num}\n{X}acc name:{Z}☆{F}{name}{Z}☆\n{X}Time send:{Z}{Time}''')
		except:
			pass