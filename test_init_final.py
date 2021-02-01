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
client.run(acess_token) # 아까 메모해 둔 토큰을 입력합니다
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
