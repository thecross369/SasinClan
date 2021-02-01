# -*- coding: utf-8 -*- 


import asyncio
import discord
import datetime
import threading
from discord.ext import commands
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import re # Regex for youtube link
import warnings
import requests
import unicodedata
import json
import os
from discord.ext.commands import CommandNotFound
import logging
import itertools
import sys
import traceback
import random
import itertools
import math
from async_timeout import timeout
from functools import partial
import functools
from youtube_dl import YoutubeDL
import youtube_dl
from io import StringIO
import time
import urllib.request
from gtts import gTTS


acess_token = os.environ["BOT_TOKEN"]
token = "acess_token" # 아까 메모해 둔 토큰을 입력합니다
client = discord.Client() # discord.Client() 같은 긴 단어 대신 client를 사용하겠다는 선언입니다.






#import sys 
#reload(sys) 
#sys.setdefaultencoding('cp949')

#Naver Open API application ID
client_id = "mBna2Kov43vTNzOnGMgB"
#Naver Open API application token
client_secret = "m7s321zpUh"



basicSetting = []
bossData = []

bossNum = 0

bossTime = []
tmp_bossTime = []

bossTimeString = []
tmp_bossTimeString = []

bossFlag = []
bossMungFlag = []
bossMungCnt = []

client = discord.Client()

channel = ''

def init():
	global basicSetting
	global bossData

	global bossNum

	global bossTime
	global tmp_bossTime

	global bossTimeString
	global tmp_bossTimeString

	global bossFlag
	global bossMungFlag
	global bossMungCnt
	
	tmp_bossData = []
	f = []
	
	inidata = open('test_setting.ini','r', encoding = 'utf-8')

	inputData = inidata.readlines()

	for i in range(inputData.count('\n')):
		inputData.remove('\n')

	basicSetting.append(inputData[0][12:])
	basicSetting.append(inputData[1][15:])
	basicSetting.append(inputData[2][10:])

	for i in range(len(basicSetting)):
		basicSetting[i] = basicSetting[i].strip()
	
	#print (inputData, len(inputData))
	
	bossNum = int((len(inputData)-3)/5)
	
	#print (bossNum)
	
	for i in range(bossNum):
		tmp_bossData.append(inputData[i*5+3:i*5+8])
		
	#print (tmp_bossData)
		
	for j in range(bossNum):
		for i in range(len(tmp_bossData[j])):
			tmp_bossData[j][i] = tmp_bossData[j][i].strip()
	
	for j in range(bossNum):
		tmp_len = tmp_bossData[j][1].find(':')
		f.append(tmp_bossData[j][0][11:])
		f.append(tmp_bossData[j][1][10:tmp_len])
		f.append(tmp_bossData[j][2][13:])
		f.append(tmp_bossData[j][3][20:])
		f.append(tmp_bossData[j][4][13:])
		f.append(tmp_bossData[j][1][tmp_len+1:])
		bossData.append(f)
		f = []
	
	for i in range(bossNum):
		print (bossData[i][0], bossData[i][1], bossData[i][5], bossData[i][2], bossData[i][3], bossData[i][4])
		
	print ('보스젠알림시간 : ', basicSetting[1])
	print ('보스멍확인시간 : ', basicSetting[2])
	
	for i in range(bossNum):
		bossTime.append(datetime.datetime.now()+datetime.timedelta(days=365))
		tmp_bossTime.append(datetime.datetime.now()+datetime.timedelta(days=365))
		bossTimeString.append('99:99:99')
		tmp_bossTimeString.append('')
		bossFlag.append(False)
		bossMungFlag.append(False)
		bossMungCnt.append(0)

init()

nowTimeString = '1'
	
token = basicSetting[0]


async def my_background_task():
	await client.wait_until_ready()

	global channel
	global nowTimeString
	
	global basicSetting
	global bossData

	global bossNum

	global bossTime
	global tmp_bossTime

	global bossTimeString
	global tmp_bossTimeString

	global bossFlag
	global bossMungFlag
	global bossMungCnt
	
	while not client.is_closed:
		now = datetime.datetime.now()
		priv = now+datetime.timedelta(minutes=int(basicSetting[1]))
		privTimeString = priv.strftime('%H:%M:%S')
		nowTimeString = now.strftime('%H:%M:%S')
		aftr = now+datetime.timedelta(minutes=int(0-int(basicSetting[2])))
		aftrTimeString = aftr.strftime('%H:%M:%S')
		#print('loop check ' + bossTime[0].strftime('%H:%M:%S') + ' ' + nowTimeString + ' ' + privTimeString, '	' + aftrTimeString)
		#print('loop check ' + str(bossTime[0]) + ' ' + str(now) + ' ' + str(priv), '	' + str(aftr))

		if channel != '':
			for i in range(bossNum):
				#print (bossData[i][0], bossTime[i])
				if bossTime[i] <= priv:
					if bossFlag[i] == False:
						bossFlag[i] = True
						await message.channel.send( bossData[i][0] + ' ' + basicSetting[1] + '분 전 ' + bossData[i][3], tts = True)
						
				if bossTime[i] <= now:
					#print ('if ', bossTime[i])
					'''
					if bossData[i][2] == '1':
						bossMungCnt[i] = 0
					'''
					bossMungFlag[i] = True
					tmp_bossTime[i] = bossTime[i]
					bossTimeString[i] = '99:99:99'
					bossTime[i] = now+datetime.timedelta(days=365)
					await message.channel.send( bossData[i][0] + '탐 ' + bossData[i][4], tts = True)
					
				if bossMungFlag[i] == True:
					if (bossTime[i]+datetime.timedelta(days=-365)) <= aftr:
						if bossData[i][2] == '0':
							await message.channel.send( bossData[i][0] + ' 미입력 됐습니다.')
							bossFlag[i] = False
							bossMungFlag[i] = False
							bossMungCnt[i] = bossMungCnt[i] + 1
							bossTime[i] = nextTime = now+datetime.timedelta(hours=int(bossData[i][1]), minutes=int(0-int(basicSetting[2])+int(bossData[i][5])))
							tmp_bossTimeString[i] = bossTimeString[i] = nextTime.strftime('%H:%M:%S')
							await message.channel.send(channel, '다음 ' + bossData[i][0] + ' ' + bossTimeString[i] + '입니다.')
						else :
							await message.channel.send( bossData[i][0] + ' 멍 입니다.')
							bossFlag[i] = False
							bossMungFlag[i] = False
							bossMungCnt[i] = bossMungCnt[i] + 1
							bossTime[i] = nextTime = now+datetime.timedelta(hours=int(bossData[i][1]), minutes=int(0-int(basicSetting[2])+int(bossData[i][5])))
							tmp_bossTimeString[i] = bossTimeString[i] = nextTime.strftime('%H:%M:%S')
							await client.send_message(channel, '다음 ' + bossData[i][0] + ' ' + bossTimeString[i] + '입니다.')
							
		await asyncio.sleep(1) # task runs every 60 seconds
		

async def joinVoiceChannel():
	channel = client.get_channel("일반")
	await client.join_voice_channel(channel)
	



	
# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
	if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
		return None #동작하지 않고 무시합니다.

	global channel
	global nowTimeString

	global basicSetting
	global bossData

	global bossNum

	global bossTime
	global tmp_bossTime

	global bossTimeString
	global tmp_bossTimeString

	global bossFlag
	global bossMungFlag
	global bossMungCnt
	
	id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
	channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.
	
	modify = ''
	
	hello = message.content
	
	chkpos = hello.find(':')
		
	if hello.find(':') != -1 :
		hours = hello[chkpos-2:chkpos]
		minutes = hello[chkpos+1:chkpos+3]
		now = datetime.datetime.now()
		#print ('oritime', now, 'h', hours, 'm', minutes)
		now = now.replace(hour=int(hours), minute=int(minutes))	
		#print (now)
	else:
		now = datetime.datetime.now()
		nowTimeString = now.strftime('%H:%M:%S')


	for i in range(bossNum):
		if message.content.startswith('!'+ bossData[i][0] +'젠'):
			bossFlag[i] = False
			bossMungFlag[i] = False
			bossMungCnt[i] = 0
			bossTime[i] = nextTime = now+datetime.timedelta(hours=int(bossData[i][1]), minutes= int(bossData[i][5]))
			tmp_bossTimeString[i] = bossTimeString[i] = nextTime.strftime('%H:%M:%S')
			await message.channel.send( '다음 '+ bossData[i][0] + ' ' + bossTimeString[i] + '입니다.')
			
		if message.content.startswith('!'+ bossData[i][0] +'삭제'):
			bossTime[i] = datetime.datetime.now()+datetime.timedelta(days=365)
			tmp_bossTime[i] =  datetime.datetime.now()+datetime.timedelta(days=365)
			bossTimeString[i] = '99:99:99'
			tmp_bossTimeString[i] = ''
			bossFlag[i] = (False)
			bossMungFlag[i] = (False)
			bossMungCnt[i] = 0
			await message.channel.send( '<' + bossData[i][0] + ' 삭제완료>')
			print ('<' + bossData[i][0] + ' 삭제완료>')
		
	#if message.content.startswith('!오빠'):
	#	await client.send_message(channel, '오빠달려려어어어어어어 ', tts=True)
		
	if message.content.startswith('!v') or message.content.startswith('!ㅍ'):
		tmp_sayMessage = message.content
		sayMessage = tmp_sayMessage[3:]
		await message.channel.send( "<@" +id+ ">님이 \"" + sayMessage + "\"", tts=True)
	if message.content.startswith('!명치'):
		client.logout()
		client.run(token)
		await message.channel.send( '<재접속 성공>')
		print ("<재접속 성공>")
		
	if message.content.startswith('!초기화'):
		basicSetting = []
		bossData = []

		bossTime = []
		tmp_bossTime = []

		bossTimeString = []
		tmp_bossTimeString = []

		bossFlag = []
		bossMungFlag = []
		bossMungCnt = []
		
		init()

		await message.channel.send( '<초기화 완료>')
		print ("<초기화 완료>")

	if message.content.startswith('!설정확인'):
		
		setting_val = '보스젠알림시간 : ' + basicSetting[1] + '\n' + '보스멍확인시간 : ' + basicSetting[2] + '\n'
		await message.channel.send( setting_val)
		print ('보스젠알림시간 : ', basicSetting[1])
		print ('보스멍확인시간 : ', basicSetting[2])


	if message.content.startswith('!불러오기'):
		try:
			file = open('my_bot.db', 'r')
			beforeBossData = file.readlines()
			
			for i in range(len(beforeBossData)-1):
				for j in range(bossNum):
					if beforeBossData[i+1].find(bossData[j][0]) != -1 :
						tmp_len = beforeBossData[i+1].find(':')

						hours = beforeBossData[i+1][tmp_len+2:tmp_len+4]
						minutes = beforeBossData[i+1][tmp_len+5:tmp_len+7]
						seconds = beforeBossData[i+1][tmp_len+8:tmp_len+10]

						now2 = datetime.datetime.now()

						tmp_now = datetime.datetime.now()
						tmp_now = now.replace(hour=int(hours), minute=int(minutes), second = int(seconds))

						if tmp_now < now2 : 
							deltaTime = datetime.timedelta(hours = int(bossData[j][1]))
							while now2 > tmp_now :
								tmp_now = tmp_now + deltaTime
							now2 = tmp_now
						else :
							now2 = now.replace(hour=int(hours), minute=int(minutes), second = int(seconds))
						bossTime[j] = now2
						bossTimeString[j] = bossTime[j].strftime('%H:%M:%S')
			file.close()
			await message.channel.send( '<불러오기 완료>')
			print ("<불러오기 완료>")
		except IOError:
			await message.channel.send( '<보스타임 정보가 없습니다.>')
			print ("보스타임 정보가 없습니다.")
	
	if message.content.startswith('!보스탐'):

		for i in range(bossNum):
			for j in range(bossNum):
				if bossTimeString[i] and bossTimeString[j] != '99:99:99':
					if bossTimeString[i] == bossTimeString[j] and i != j:
						tmp_time1 = bossTimeString[j][:6]
						tmp_time2 = (int(bossTimeString[j][6:]) + 1)%100
						#print ('i : ', i, ' ', bossTimeString[i], ' j : ', j, ' ', bossTimeString[j])
						if tmp_time2 < 10 :
							tmp_time22 = '0' + str(tmp_time2)
						elif tmp_time2 == 60 :
							tmp_time22 = '00'
						else :
							tmp_time22 = str(tmp_time2)
						bossTimeString[j] = tmp_time1 + tmp_time22
						#print (bossTimeString[j])

		datelist = bossTimeString
					
		information = '----- 보스탐 정보 -----\n'
		for timestring in sorted(datelist):
			for i in range(bossNum):
				if timestring == bossTimeString[i]:
					if bossTimeString[i] != '99:99:99':
						if bossData[i][2] == '0' :
							if bossMungCnt[i] == 0 :
								information += ' - ' + bossData[i][0] + '(' + bossData[i][1] + '.' + bossData[i][5] + ') : ' + bossTimeString[i] + '\n'
							else :
								information += ' - ' + bossData[i][0] + '(' + bossData[i][1] + '.' + bossData[i][5] + ') : ' + bossTimeString[i] + ' (미입력 ' + str(bossMungCnt[i]) + '회)' + '\n'
						else : 
							if bossMungCnt[i] == 0 :
								information += ' - ' + bossData[i][0] + '(' + bossData[i][1] + '.' + bossData[i][5] + ') : ' + bossTimeString[i] + '\n'
							else :
								information += ' - ' + bossData[i][0] + '(' + bossData[i][1] + '.' + bossData[i][5] + ') : ' + bossTimeString[i] + ' (멍 ' + str(bossMungCnt[i]) + '회)' + '\n'

		await message.channel.send( information)
		
		file = open("my_bot.db", 'w')
		file.write(information);
		file.close()
				
	if message.content.startswith('!현재시간'):
		await message.channel.send( datetime.datetime.now().strftime('%H:%M:%S'))


		

#client = discord.Client()
@client.event # Use these decorator to register an event.
async def on_ready(): # on_ready() event : when the bot has finised logging in and setting things up
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!도움말 을 입력해보세요"))
    print("New log in as {0.user}".format(client))


@client.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.
    if message.author.bot: # 채팅을 친 사람이 봇일 경우
       return None # 반응하지 않고 구문을 종료합니다.

    print(message.content)

    #if message.contentstartswith("/도움말"):
    if message.content == "!도움말":
       embed = discord.Embed(title="도움말 목록", description="", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805528929565278262/805557539172515900/0a967a92698a2835.png") #썸네일 구역에 이미지 넣기
       embed.set_image(url="https://cdn.discordapp.com/attachments/805528929565278262/805557124892459070/mo.gif") # 메시지 구역에 이미지 넣기
       embed.add_field(name="!한영번역", value="!한영번역 한국어 입력하면 한국어가 영어로 출력", inline=False)
       embed.add_field(name="!영한번역", value="!영한번역 영어 입력하면 영어가 한국어로 출력", inline=False)        
       await message.channel.send("Melissia BOSS Time 명령어목록", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
    #To user who sent message
    #await message.author.send(msg)
    #print(message.content)
    #if message.author == client.user:
        #return


    '''
    #You can get id and secret key with registering in naver
    client_id = ""
    client_secret = ""

    #Text to translate
    entData = quote("")

    dataParmas = "source=en&target=id&text=" + entData
    baseurl = "https://openapi.naver.com/v1/papago/n2mt"

    #Make a Request Instance
    request = Request(baseurl)

    #add header to packet
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urlopen(request,data=dataParmas.encode("utf-8"))

    responsedCode = response.getcode()
    if(responsedCode==200):
        response_body = response.read()
        #response_body -> byte string : decode to utf-8
        api_callResult = response_body.decode('utf-8')

        #JSON Type data will be printed. So need to make it back to type JSON(like dictionary)
        stringConvertJSON = api_callResult.replace("'","\"")
        api_callResult = json.loads(stringConvertJSON)
        translatedText = api_callResult['message']['result']["translatedText"]
        print(translatedText)
    else:
        print("Error Code : " + responsedCode)
    '''







    if message.content.startswith("!한영번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        #띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                print(combineword)
                # Make Query String.
                dataParmas = "source=ko&target=en&text=" + combineword
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역 | Korean -> English", description="", color=0x5CD1E5)
                    embed.add_field(name="한국어", value=savedCombineword, inline=False)
                    embed.add_field(name="영어", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805528929565278262/805557124892459070/mo.gif")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://cdn.discordapp.com/attachments/805528929565278262/805557539172515900/0a967a92698a2835.png')
                    await message.channel.send("번역완료", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")


    if message.content.startswith("!영한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                dataParmas = "source=en&target=ko&text=" + combineword
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')

                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역 | English -> Korean", description="", color=0x5CD1E5)
                    embed.add_field(name="영어", value=savedCombineword, inline=False)
                    embed.add_field(name="한국어", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805528929565278262/805557124892459070/mo.gif")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://cdn.discordapp.com/attachments/805528929565278262/805557539172515900/0a967a92698a2835.png')
                    await message.channel.send("번역완료", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!한일번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                dataParmas = "source=ko&target=ja&text=" + combineword
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')

                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역 | Korean -> Japanese", description="", color=0x5CD1E5)
                    embed.add_field(name="한국어", value=savedCombineword, inline=False)
                    embed.add_field(name="일본어", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805528929565278262/805557124892459070/mo.gif")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://cdn.discordapp.com/attachments/805528929565278262/805557539172515900/0a967a92698a2835.png')
                    await message.channel.send("번역완료", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!일한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                dataParmas = "source=ja&target=ko&text=" + combineword
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')

                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역 | Japanese -> Korean", description="", color=0x5CD1E5)
                    embed.add_field(name="일본어", value=savedCombineword, inline=False)
                    embed.add_field(name="한국어", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805528929565278262/805557124892459070/mo.gif")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://cdn.discordapp.com/attachments/805528929565278262/805557539172515900/0a967a92698a2835.png')
                    await message.channel.send("번역완료", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!한중번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.

                #Simplified Chinese
                dataParmas = "source=ko&target=zh-CN&text=" + combineword

                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역 | Korean -> Chinese(Simplified Chinese)", description="", color=0x5CD1E5)
                    embed.add_field(name="한국", value=savedCombineword, inline=False)
                    embed.add_field(name="중국어(Simplified)", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805528929565278262/805557124892459070/mo.gif")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://cdn.discordapp.com/attachments/805528929565278262/805557539172515900/0a967a92698a2835.png')
                    await message.channel.send("번역완료", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!중한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                # Simplified Chinese
                dataParmas = "source=zh-CN&target=ko&text=" + combineword


                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역 | Chinese -> Korean", description="", color=0x5CD1E5)
                    embed.add_field(name="중국어", value=savedCombineword, inline=False)
                    embed.add_field(name="한국어", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805528929565278262/805557124892459070/mo.gif")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://cdn.discordapp.com/attachments/805528929565278262/805557539172515900/0a967a92698a2835.png')
                    await message.channel.send("번역완료", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")


    if message.content.startswith("!한러번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                # Simplified Chinese
                dataParmas = "source=ko&target=ru&text=" + combineword


                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역 | Korean -> Russian", description="", color=0x5CD1E5)
                    embed.add_field(name="한국어", value=savedCombineword, inline=False)
                    embed.add_field(name="러시아어", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805528929565278262/805557124892459070/mo.gif")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://cdn.discordapp.com/attachments/805528929565278262/805557539172515900/0a967a92698a2835.png')
                    await message.channel.send("번역완료", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")


    if message.content.startswith("!러한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                # Simplified Chinese
                dataParmas = "source=ru&target=ko&text=" + combineword


                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역 | Korean -> Russian", description="", color=0x5CD1E5)
                    embed.add_field(name="러시아어", value=savedCombineword, inline=False)
                    embed.add_field(name="한국어", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805528929565278262/805557124892459070/mo.gif")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://cdn.discordapp.com/attachments/805528929565278262/805557539172515900/0a967a92698a2835.png')
                    await message.channel.send("번역완료", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")


            
            
client.run(token)
