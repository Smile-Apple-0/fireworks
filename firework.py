#Auto Loop
# -*- coding: utf-8 -*-
import discord
import requests
from discord.ext import commands
from bs4 import BeautifulSoup
import lxml
import datetime
import asyncio
import discord
import logging
import random
import math
import functools
import itertools
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL
import youtube_dl.utils
import city
import urllib.parse, urllib.request, re
from gtts import gTTS #tts 기능
import ffmpeg
import openpyxl
import sys
import urllib.request
import json
from datetime import datetime
import time
from matplotlib import pyplot as plt
import os
import wmi
import psutil
import platform
from datetime import datetime
import time
import cpuinfo
import traceback
import dbkrpy


bot = commands.Bot(command_prefix = '-')

DBKR_token = ""
token = '' 
dbkrpy.UpdateGuild(bot,DBKR_token)

@bot.remove_command('help')



@bot.event
async def on_ready():
    print("I'm ready") 
    game = discord.Game(".도움말 | {}개의 서버에 가입되어 있습니다.".format(str(len(bot.guilds))))
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=game)
@bot.command('날씨')
async def weather_output(context, city):
    api_address = "http://api.weatherstack.com/current?access_key=96b61cb41acaad6fe3b5d8b31465a586&query="
    api_url = api_address + city
    json_data = requests.get(api_url).json()

    city_name = json_data["location"]["name"]
    temperature = json_data["current"]["temperature"]
    weather_description = json_data["current"]["weather_descriptions"][0]

    embed=discord.Embed(title="날씨 정보", description="날씨정보를 보여줍니다.", color=0x00ffff)
    embed.add_field(name=(f'\n도시: {city_name} \n온도는 {temperature} 입니다. \n날씨는 {weather_description}'), value=("아직 영어밖에 안됩니다."), inline=False)
    await context.send(embed=embed)

@bot.command('코로나')
async def corona(ctx):
    address = "http://ncov.mohw.go.kr"

    response = requests.get(address)
    soup = BeautifulSoup(response.text,'lxml')
    확진자 = soup.select('div.liveboard_layout div.liveNum span.num')
    await ctx.send('``차례대로 확진환자, 완치, 치료 중, 사망 순입니다.``')
    for b in 확진자:
        # embed=discord.Embed(title="코로나", description="차례대로 확진환자, 완치, 치료 중, 사망 순입니다.", color=0xffff80)
        # embed.add_field(name=("멍청한 스플이가 만들었습니다."), value=(b.text), inline=True)
        await ctx.send('``'+b.text+'명``')

@bot.command('현재시각')
async def now_time(ctx):
    datetime_object = datetime.datetime.now()
    await ctx.send(f'``현재 시각은 {datetime_object} 입니다.``')

@bot.command()
async def 스플봇(ctx):
    await ctx.send('저를 만든 개발자중 스플봇을 만든사람도 포함되어있다고 들었어요') 

@bot.command()
async def api핑(ctx):
    latency = bot.latency
    await ctx.send(f'현재핑은 ``{round(latency * 1000)}``ms 입니다.')

@bot.command('따라해')
async def echo(ctx, *, content: str):
    await ctx.send(content)

# @bot.event
# async def on_command_error(ctx: commands.Context, error: Exception):
#     if isinstance(error, (commands.CommandNotFound)):
        

@bot.event
async def on_command_error(ctx: commands.Context, error: Exception):
    try: 
        if isinstance(error, (commands.CommandNotFound)):
            userid = ctx.message.author.id
            channel = ctx.author.voice.channel
            language = 'ko'
            output = gTTS(text="제가 잘이해한건지 모르겠네요.",lang=language,slow=False)
            output.save("idk.mp3")
            #if not connected
            if ctx.voice_client is None:
                vc = await channel.connect()
                await ctx.send(f'<@!{userid}> 제가 잘이해한건지 모르겠네요.')
                vc.play(discord.FFmpegPCMAudio('idk.mp3'))
                return
            else:
                await ctx.send(f'<@!{userid}> 제가 잘이해한건지 모르겠네요.')
                ctx.voice_client.play(discord.FFmpegPCMAudio('idk.mp3'))
                return
    except :
        userid = ctx.message.author.id
        await ctx.send(f"<@!{userid}> 제가 잘이해한건지 모르겠네요.")

@bot.command()
async def 유저정보(ctx, member: discord.Member):
    embed=discord.Embed(title="유저 정보", description="유저정보를 불러옵니다.", color=0x00ffff)
    embed.add_field(name=("멍청한 스플이가 만들었습니다."), value=(f'유저 이름: {member.name}, 아이디: {member.id}'), inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def 내정보(ctx):
    member = ctx.message.author
    embed=discord.Embed(title="유저 정보", description="유저정보를 불러옵니다.", color=0x00ffff)
    embed.add_field(name=("멍청한 스플이가 만들었습니다."), value=(f'유저 이름: {member.name}, 아이디: {member.id}'), inline=True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def 주사위(ctx):
    dice = random.randint(1, 6)
    if dice == 1:
        await ctx.send("1이 나왔습니다.")
    if dice == 2:
        await ctx.send("2가 나왔습니다.")
    if dice == 3:
        await ctx.send("3가 나왔습니다.")
    if dice == 4:
        await ctx.send("4가 나왔습니다.")
    if dice == 5:
        await ctx.send("5가 나왔습니다.")    
    if dice == 6:
        await ctx.send("6이 나왔습니다.")

@bot.command()
async def 도움말(ctx):
    embed=discord.Embed(title="도움말", description="도움말을 표시합니다.", color=0x00ffff)
    embed.add_field(name=("개발자: Heu_Ani#6974, Hunter815#8653, Smile Apple#0001"), value=("도움말입니다. 명령어: .날씨 [도시 이름 영어로 (예: Seoul)], .코로나, .현재시각, .[가위, 바위, 보 중 아무거나], .따라해 (할말), .스플봇, .유저정보 (@언급 필수), .내정보, .팀가입, .주사위, .tts접속, .tts접속해제, 음성말해 en 또는 ko [할말] (보이스채널 접속하신후 tts접속을 입력해주시고 사용해주세요.), .뮤직도움말"), inline=False)
    embed.add_field(name=("tts 부분: Smile Apple#0001"), value=("명령어: .비트박스해줘, .tts로말해줘, .누가널만들었어, .너몇살이야, .넌어디에있어, .돈없어, .너가청소해줘, .농담해봐, .인공지능이란, .0나누기0, .야, .씨^발, .어그로끌어"), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 뮤직도움말(ctx):
    embed=discord.Embed(title="뮤직 도움말", description="뮤직 도움말을 표시합니다.", color=0x00ffff)
    embed.add_field(name=("뮤직 담당: Smile Apple#0001"), value=("명령어: .재생, .들어와, .나가, .볼륨, .정보, .일시중지, .다시재생, .멈춰, .스킵, .리스트, .섞어, .제거, .반복재생"), inline=True)
    await ctx.send(embed=embed)

@bot.command('나는스마일애플인가') #테스트 명령어, 지우지 말것.
async def whoissmileapple(ctx):
    if ctx.author.id == 608956812636454915:
        await ctx.send("당신은 스마일애플이 아니다. 당신은 흐아니??? 이다.")
        return
    elif ctx.author.id == 688222392186699779:
        await ctx.send("당신은 스마일애플이 아니다. 당신은 헌터이다.")
        return
    elif ctx.author.id == 584180794709508107:
        await ctx.send("당신은 스마일애플이 아니다. 4114이다.")
    elif ctx.author.id == 380625576014381060:
        await ctx.send("당신은 스마일애플이 맞다.")
    else:
        await ctx.send(f"당신은 스마일애플이 아니다.")

async def text2Speech(language,text,ctx,channel):
    myText = text
    language = language
    output = gTTS(text=myText,lang=language,slow=False)
    output.save("output.mp3")
    #if not connected
    if ctx.voice_client is None:
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('output.mp3'))
    else:
        ctx.voice_client.play(discord.FFmpegPCMAudio('output.mp3'))



@bot.command()
async def tts접속(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def tts접속해제(ctx):
    await ctx.voice_client.disconnect()

@bot.command(name='음성말해')
async def t2s(ctx,*argv):
    channel = ctx.author.voice.channel
    text = ""
    for i in range(1,len(argv)):
        text += argv[i]
    language = argv[0]
    await text2Speech(language,text,ctx,channel)
    #await ctx.send("Lang is {} and the sentence is:  {} ".format(arg1,arg2)

@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕하세요?")

@bot.command()
async def 너는누구야(ctx):
    await ctx.send("저는 팀 유니버스로부터 탄생한 Fireworks랍니다.")

@bot.command()
async def 꺼져(ctx):
    await ctx.send("정...원하신다면..")

@bot.command()
async def tts로말해줘(ctx):
    await ctx.send("저는 음성채널에만 말할 수 있어요. 어? 지금 제 목소리는 뭐죠?", tts=True)

@bot.command()
async def 가위(ctx):
    str1 = ['가위','바위','보']
    r=random.choice(str1)
    if r == '가위':
        embed = discord.Embed(title="가위 바위 보", description= r + "\n✌️ vs ✌️ 비겼습니다.", color=0x00ffff)
        await ctx.send(embed=embed)
    elif r == '바위':
        embed = discord.Embed(title="가위 바위 보", description= r + "\n✌️ vs 👊 당신이 졌습니다.", color=0x00ffff)
        await ctx.send(embed=embed)
    elif r == '보':
        embed = discord.Embed(title="가위 바위 보", description= r + "\n✌️ vs ✋ 당신이 이겼습니다.", color=0x00ffff)
        await ctx.send(embed=embed)

@bot.command()
async def 바위(ctx):
    str1 = ['가위','바위','보']
    r=random.choice(str1)
    if r == '가위':
        embed = discord.Embed(title="가위 바위 보", description= r + "\n👊 vs ✌️ 당신이 이겼습니다.", color=0x00ffff)
        await ctx.send(embed=embed)
    elif r == '바위':
        embed = discord.Embed(title="가위 바위 보", description= r + "\n👊 vs 👊 비겼습니다.", color=0x00ffff)
        await ctx.send(embed=embed)
    elif r == '보':
        embed = discord.Embed(title="가위 바위 보", description= r + "\n👊 vs ✋ 당신이 졌습니다.", color=0x00ffff)
        await ctx.send(embed=embed)

@bot.command()
async def 보(ctx):
    str1 = ['가위','바위','보']
    r=random.choice(str1)
    if r == '가위':
        embed = discord.Embed(title="가위 바위 보", description= r + "\n✋ vs ✌️ 당신이 졌습니다.", color=0x00ffff)
        await ctx.send(embed=embed)
    elif r == '바위':
        embed = discord.Embed(title="가위 바위 보", description= r + "\n✋ vs 👊당신이 이겼습니다.", color=0x00ffff)
        await ctx.send(embed=embed)
    elif r == '보':
        embed = discord.Embed(title="가위 바위 보", description= r + "\n✋ vs ✋비겼습니다.", color=0x00ffff)
        await ctx.send(embed=embed)



@bot.command(name='비트박스해줘')
async def beetbox(ctx):
    channel = ctx.author.voice.channel
    userid = ctx.message.author.id
    language = 'ko'
    output = gTTS(text="북치기 박치기 북치기, 빠르게는 못하겠네요.",lang=language,slow=False)
    output.save("beetbox.mp3")
    #if not connected
    if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 북치기 박치기 북치기, 빠르게는 못하겠네요.')
            vc.play(discord.FFmpegPCMAudio('beetbox.mp3'))
            return
    else:
        await ctx.send(f'<@!{userid}> 북치기 박치기 북치기, 빠르게는 못하겠네요.')
        ctx.voice_client.play(discord.FFmpegPCMAudio('beetbox.mp3'))
        return

@bot.command(name='너몇살이야')
async def ttsage(ctx):
    userid = ctx.message.author.id
    channel = ctx.author.voice.channel
    language = 'ko'
    output = gTTS(text="저는 마치 동쪽 바람만큼 늙었으며 새로 태어난 애벌레만큼 어리기도 합니다.",lang=language,slow=False)
    output.save("age.mp3")
    #if not connected
    if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 저는 마치 동쪽 바람만큼 늙었으며 새로 태어난 애벌레만큼 어리기도 합니다.')
            vc.play(discord.FFmpegPCMAudio('age.mp3'))
            return
    else:
        await ctx.send(f'<@!{userid}> 저는 마치 동쪽 바람만큼 늙었으며 새로 태어난 애벌레만큼 어리기도 합니다.')
        ctx.voice_client.play(discord.FFmpegPCMAudio('age.mp3'))
        return
@bot.command(name='넌어디에있어')
async def ttswhere(ctx):
    userid = ctx.message.author.id
    channel = ctx.author.voice.channel
    language = 'ko'
    output = gTTS(text="저는 디스코드에서 살고 있답니다. 제가 온라인일땐 언제나 찾아가드립니다.",lang=language,slow=False)
    output.save("where.mp3")
    #if not connected
    if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 저는 디스코드에서 살고 있답니다. 제가 온라인일땐 언제나 찾아가드립니다.')
            vc.play(discord.FFmpegPCMAudio('where.mp3'))
            return
    else:
        await ctx.send(f'<@!{userid}> 저는 디스코드에서 살고 있답니다. 제가 온라인일땐 언제나 찾아가드립니다.')
        ctx.voice_client.play(discord.FFmpegPCMAudio('where.mp3'))
        return
@bot.command('돈없어')
async def ttsnomoney(ctx):
    userid = ctx.message.author.id
    channel = ctx.author.voice.channel
    language = 'ko'
    output = gTTS(text="저는 디스코드 봇이라서 도와드리지 못하겠네요. 죄송합니다.",lang=language,slow=False)
    output.save("nomoney.mp3")
    #if not connected
    if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 저는 디스코드 봇이라서 도와드리지 못하겠네요. 죄송합니다.')
            vc.play(discord.FFmpegPCMAudio('nomoney.mp3'))
            return
    else:
        await ctx.send(f'<@!{userid}> 저는 디스코드 봇이라서 도와드리지 못하겠네요. 죄송합니다.')
        ctx.voice_client.play(discord.FFmpegPCMAudio('nomoney.mp3'))
        return
@bot.command('너가청소해줘')
async def ttsnomoney(ctx):
    userid = ctx.message.author.id
    channel = ctx.author.voice.channel
    language = 'ko'
    output = gTTS(text="누구요? 저요?",lang=language,slow=False)
    output.save("chungso.mp3")
    #if not connected
    if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 누구요? 저요?')
            vc.play(discord.FFmpegPCMAudio('chungso.mp3'))
            return
    else:
        await ctx.send(f'<@!{userid}> 누구요? 저요?')
        ctx.voice_client.play(discord.FFmpegPCMAudio('chungso.mp3'))
        return

@bot.command('농담해봐')
async def ttsjoke(ctx):
    rantts = random.randint(1,2)
    if rantts == 1:
        userid = ctx.message.author.id
        channel = ctx.author.voice.channel
        language = 'ko'
        output = gTTS(text="스플봇과 민기봇이... 아니에요 안 하는게 좋겠어요.",lang=language,slow=False)
        output.save("joke1.mp3")
        #if not connected
        if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 스플봇과 민기봇이... 아니에요 안 하는게 좋겠어요.')
            vc.play(discord.FFmpegPCMAudio('joke1.mp3'))
            return
        else:
            await ctx.send(f'<@!{userid}> 스플봇과 민기봇이... 아니에요 안 하는게 좋겠어요.')
            ctx.voice_client.play(discord.FFmpegPCMAudio('joke1.mp3'))
            return
    if rantts == 2:
        userid = ctx.message.author.id
        channel = ctx.author.voice.channel
        language = 'ko'
        output = gTTS(text="두 디스코드봇이 술집으로 들어가는데... 나머지는 잊어버렸어요.",lang=language,slow=False)
        output.save("joke2.mp3")
        #if not connected
        if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 두 디스코드봇이 술집으로 들어가는데... 나머지는 잊어버렸어요.')
            vc.play(discord.FFmpegPCMAudio('joke2.mp3'))
            return
        else:
            await ctx.send(f'<@!{userid}> 두 디스코드봇이 술집으로 들어가는데... 나머지는 잊어버렸어요.')
            ctx.voice_client.play(discord.FFmpegPCMAudio('joke2.mp3'))
            return
    
@bot.command('인공지능이란')
async def ttsnomoney(ctx):
    userid = ctx.message.author.id
    channel = ctx.author.voice.channel
    language = 'ko'
    output = gTTS(text="인공지능이 인간을 뛰어넘지 않았으면 좋겠네요.",lang=language,slow=False)
    output.save("thinkingaboutrobot.mp3")
    #if not connected
    if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 인공지능이 인간을 뛰어넘지 않았으면 좋겠네요.')
            vc.play(discord.FFmpegPCMAudio('thinkingaboutrobot.mp3'))
            return
    else:
        await ctx.send(f'<@!{userid}> 인공지능이 인간을 뛰어넘지 않았으면 좋겠네요.')
        ctx.voice_client.play(discord.FFmpegPCMAudio('thinkingaboutrobot.mp3'))
        return

@bot.command('0나누기0')
async def ttsnomoney(ctx):
    userid = ctx.message.author.id
    channel = ctx.author.voice.channel
    language = 'ko'
    output = gTTS(text="0개의 쿠키를 0명의 친구들과 나눠 먹는다고 가정할 때 각각의 친구들이 먹는 쿠키의 양은 얼마나 될까요? 이해가 가셨는지 모르겠어요. 암튼, 쿠키 몬스터는 쿠키가 없어서 슬펐고 주인님은 같이 나눠먹을 친구가 없어서 슬펐다는 얘기였습니다. 0 나누기 0은 부정소입니다.",lang=language,slow=False)
    output.save("00.mp3")
    #if not connected
    if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 0개의 쿠키를 0명의 친구들과 나눠 먹는다고 가정할 때 각각의 친구들이 먹는 쿠키의 양은 얼마나 될까요? 이해가 가셨는지 모르겠어요. 암튼, 쿠키 몬스터는 쿠키가 없어서 슬펐고 주인님은 같이 나눠먹을 친구가 없어서 슬펐다는 얘기였습니다. ```0 나누기 0은 부정소입니다.```')
            vc.play(discord.FFmpegPCMAudio('00.mp3'))
            return
    else:
        await ctx.send(f'<@!{userid}> 0개의 쿠키를 0명의 친구들과 나눠 먹는다고 가정할 때 각각의 친구들이 먹는 쿠키의 양은 얼마나 될까요? 이해가 가셨는지 모르겠어요. 암튼, 쿠키 몬스터는 쿠키가 없어서 슬펐고 주인님은 같이 나눠먹을 친구가 없어서 슬펐다는 얘기였습니다. ```0 나누기 0은 부정소입니다.```')
        ctx.voice_client.play(discord.FFmpegPCMAudio('00.mp3'))
        return

@bot.command('야')
async def ttsyanolja(ctx):
    rantts = random.randint(1,2)
    if rantts == 1:
        userid = ctx.message.author.id
        channel = ctx.author.voice.channel
        language = 'ko'
        output = gTTS(text="누구요? 저요?",lang=language,slow=False)
        output.save("ya.mp3")
        #if not connected
        if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 누구요? 저요?')
            vc.play(discord.FFmpegPCMAudio('ya.mp3'))
            return
        else:
            await ctx.send(f'<@!{userid}> 누구요? 저요?')
            ctx.voice_client.play(discord.FFmpegPCMAudio('ya.mp3'))
            return
    if rantts == 2:
        userid = ctx.message.author.id
        username = ctx.message.author.name
        channel = ctx.author.voice.channel
        language = 'ko'
        output = gTTS(text=f"네 {username}님?",lang=language,slow=False)
        output.save("ya2.mp3")
        #if not connected
        if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 네 {username}님?')
            vc.play(discord.FFmpegPCMAudio('ya2.mp3'))
            return
        else:
            await ctx.send(f'<@!{userid}> 네 {username}님?')
            ctx.voice_client.play(discord.FFmpegPCMAudio('ya2.mp3'))
            return
    
@bot.command('씨발')
async def ttsssibal(ctx):
    rantts = random.randint(1,2)
    if rantts == 1:
        userid = ctx.message.author.id
        channel = ctx.author.voice.channel
        language = 'ko'
        output = gTTS(text="그건 못 들은걸로 칠게요.",lang=language,slow=False)
        output.save("sibbal1.mp3")
        #if not connected
        if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 그건 못 들은걸로 칠게요')
            vc.play(discord.FFmpegPCMAudio('sibbal1.mp3'))
            return
        else:
            await ctx.send(f'<@!{userid}> 그건 못 들은걸로 칠게요')
            ctx.voice_client.play(discord.FFmpegPCMAudio('sibbal1.mp3'))
            return
    if rantts == 2:
        userid = ctx.message.author.id
        username = ctx.message.author.name
        channel = ctx.author.voice.channel
        language = 'ko'
        output = gTTS(text=f"혹시 스플봇이 그 메세지를 지우지는 않나요?",lang=language,slow=False)
        output.save("sibbal2.mp3")
        #if not connected
        if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 혹시 스플봇이 그 메세지를 지우지는 않나요?')
            vc.play(discord.FFmpegPCMAudio('sibbal2.mp3'))
            return
        else:
            await ctx.send(f'<@!{userid}> 혹시 스플봇이 그 메세지를 지우지는 않나요?')
            ctx.voice_client.play(discord.FFmpegPCMAudio('sibbal2.mp3'))
            return

@bot.command('어그로끌어')
async def ttsholyshit(ctx):
    userid = ctx.message.author.id
    channel = ctx.author.voice.channel
    language = 'ko'
    output = gTTS(text="미안하다 이거 보여주려고 어그로끌었다.. 나루토 사스케 싸움수준 ㄹㅇ실화냐? 진짜 세계관최강자들의 싸움이다.. 그찐따같던 나루토가 맞나? 진짜 나루토는 전설이다..진짜옛날에 맨날나루토봘는데 왕같은존재인 호카게 되서 세계최강 전설적인 영웅이된나루토보면 진짜내가다 감격스럽고 나루토 노래부터 명장면까지 가슴울리는장면들이 뇌리에 스치면서 가슴이 웅장해진다.. 그리고 극장판 에 카카시앞에 운석날라오는 거대한 걸 사스케가 갑자기 순식간에 나타나서 부숴버리곤 개간지나게 나루토가 없다면 마을을 지킬 자는 나밖에 없다 라며 바람처럼 사라진장면은 진짜 나루토처음부터 본사람이면 안울수가없더라 진짜 너무 감격스럽고 보루토를 최근에 알았는데 미안하다.. 지금20화보는데 진짜 나루토세대나와서 너무 감격스럽고 모두어엿하게 큰거보니 내가 다 뭔가 알수없는 추억이라해야되나 그런감정이 이상하게 얽혀있다.. 시노는 말이많아진거같다 좋은선생이고..그리고 보루토왜욕하냐 귀여운데 나루토를보는것같다 성격도 닮았어 그리고버루토에 나루토사스케 둘이싸워도 이기는 신같은존재 나온다는게 사실임?? 그리고인터닛에 쳐봣는디 이거 ㄹㅇㄹㅇ 진짜팩트냐?? 저적이 보루토에 나오는 신급괴물임?ㅡ 나루토사스케 합체한거봐라 진짜 ㅆㅂ 이거보고 개충격먹어가지고 와 소리 저절로 나오더라 ;; 진짜 저건 개오지는데.. 저게 ㄹㅇ이면 진짜 꼭봐야돼 진짜 세계도 파괴시키는거아니야 .. 와 진짜 나루토사스케가 저렇게 되다니 진짜 눈물나려고했다.. 버루토그라서 계속보는중인데 저거 ㄹㅇ이냐..? 하.. ㅆㅂ 사스케 보고싶다..  진짜언제 이렇게 신급 최강들이 되었을까 옛날생각나고 나 중딩때생각나고 뭔가 슬프기도하고 좋기도하고 감격도하고 여러가지감정이 복잡하네.. 아무튼 나루토는 진짜 애니중최거명작임..",lang=language,slow=False)
    output.save("holyshit.mp3")
    #if not connected
    if ctx.voice_client is None:
            vc = await channel.connect()
            await ctx.send(f'<@!{userid}> 미안하다 이거 보여주려고 어그로끌었다.. 나루토 사스케 싸움수준 ㄹㅇ실화냐? 진짜 세계관최강자들의 싸움이다.. 그찐따같던 나루토가 맞나? 진짜 나루토는 전설이다..진짜옛날에 맨날나루토봘는데 왕같은존재인 호카게 되서 세계최강 전설적인 영웅이된나루토보면 진짜내가다 감격스럽고 나루토 노래부터 명장면까지 가슴울리는장면들이 뇌리에 스치면서 가슴이 웅장해진다.. 그리고 극장판 에 카카시앞에 운석날라오는 거대한 걸 사스케가 갑자기 순식간에 나타나서 부숴버리곤 개간지나게 나루토가 없다면 마을을 지킬 자는 나밖에 없다 라며 바람처럼 사라진장면은 진짜 나루토처음부터 본사람이면 안울수가없더라 진짜 너무 감격스럽고 보루토를 최근에 알았는데 미안하다.. 지금20화보는데 진짜 나루토세대나와서 너무 감격스럽고 모두어엿하게 큰거보니 내가 다 뭔가 알수없는 추억이라해야되나 그런감정이 이상하게 얽혀있다.. 시노는 말이많아진거같다 좋은선생이고..그리고 보루토왜욕하냐 귀여운데 나루토를보는것같다 성격도 닮았어 그리고버루토에 나루토사스케 둘이싸워도 이기는 신같은존재 나온다는게 사실임?? 그리고인터닛에 쳐봣는디 이거 ㄹㅇㄹㅇ 진짜팩트냐?? 저적이 보루토에 나오는 신급괴물임?ㅡ 나루토사스케 합체한거봐라 진짜 ㅆㅂ 이거보고 개충격먹어가지고 와 소리 저절로 나오더라 ;; 진짜 저건 개오지는데.. 저게 ㄹㅇ이면 진짜 꼭봐야돼 진짜 세계도 파괴시키는거아니야 .. 와 진짜 나루토사스케가 저렇게 되다니 진짜 눈물나려고했다.. 버루토그라서 계속보는중인데 저거 ㄹㅇ이냐..? 하.. ㅆㅂ 사스케 보고싶다..  진짜언제 이렇게 신급 최강들이 되었을까 옛날생각나고 나 중딩때생각나고 뭔가 슬프기도하고 좋기도하고 감격도하고 여러가지감정이 복잡하네.. 아무튼 나루토는 진짜 애니중최거명작임..')
            vc.play(discord.FFmpegPCMAudio('holyshit.mp3'))
            return
    else:
        await ctx.send(f'<@!{userid}> 미안하다 이거 보여주려고 어그로끌었다.. 나루토 사스케 싸움수준 ㄹㅇ실화냐? 진짜 세계관최강자들의 싸움이다.. 그찐따같던 나루토가 맞나? 진짜 나루토는 전설이다..진짜옛날에 맨날나루토봘는데 왕같은존재인 호카게 되서 세계최강 전설적인 영웅이된나루토보면 진짜내가다 감격스럽고 나루토 노래부터 명장면까지 가슴울리는장면들이 뇌리에 스치면서 가슴이 웅장해진다.. 그리고 극장판 에 카카시앞에 운석날라오는 거대한 걸 사스케가 갑자기 순식간에 나타나서 부숴버리곤 개간지나게 나루토가 없다면 마을을 지킬 자는 나밖에 없다 라며 바람처럼 사라진장면은 진짜 나루토처음부터 본사람이면 안울수가없더라 진짜 너무 감격스럽고 보루토를 최근에 알았는데 미안하다.. 지금20화보는데 진짜 나루토세대나와서 너무 감격스럽고 모두어엿하게 큰거보니 내가 다 뭔가 알수없는 추억이라해야되나 그런감정이 이상하게 얽혀있다.. 시노는 말이많아진거같다 좋은선생이고..그리고 보루토왜욕하냐 귀여운데 나루토를보는것같다 성격도 닮았어 그리고버루토에 나루토사스케 둘이싸워도 이기는 신같은존재 나온다는게 사실임?? 그리고인터닛에 쳐봣는디 이거 ㄹㅇㄹㅇ 진짜팩트냐?? 저적이 보루토에 나오는 신급괴물임?ㅡ 나루토사스케 합체한거봐라 진짜 ㅆㅂ 이거보고 개충격먹어가지고 와 소리 저절로 나오더라 ;; 진짜 저건 개오지는데.. 저게 ㄹㅇ이면 진짜 꼭봐야돼 진짜 세계도 파괴시키는거아니야 .. 와 진짜 나루토사스케가 저렇게 되다니 진짜 눈물나려고했다.. 버루토그라서 계속보는중인데 저거 ㄹㅇ이냐..? 하.. ㅆㅂ 사스케 보고싶다..  진짜언제 이렇게 신급 최강들이 되었을까 옛날생각나고 나 중딩때생각나고 뭔가 슬프기도하고 좋기도하고 감격도하고 여러가지감정이 복잡하네.. 아무튼 나루토는 진짜 애니중최거명작임..')
        ctx.voice_client.play(discord.FFmpegPCMAudio('holyshit.mp3'))
        return


bot.run(token) 
