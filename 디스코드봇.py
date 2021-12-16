import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("이름")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("/퓨즈교체"):
        await message.channel.send("집에 들어가자 마자 있는 두꺼비집에서 퓨즈를 교체한다.")

#영업시간
    if message.content.startswith("/영업시간-상점"):
        await message.channel.send("월요일~토요일 오전10시~오후8시\n일요일 휴무")

    if message.content.startswith("/영업시간-펍"):
        await message.channel.send("월요일~토요일 오후8시~익일오전2시\n일요일 휴무")

    if message.content.startswith("/영업시간-차량등록소"):
        await message.channel.send("평일 오전8시~오후4시")

    if message.content.startswith("/영업시간-정비소") or message.content.startswith("정비소 언제염"):
        await message.channel.send("평일 오전8시~오후4시") 
        await message.channel.send(file=discord.File("정비소.png"))
    if message.content.startswith("/상점리필") or message.content.startswith("상점 언제 체워짐"):
        await message.channel.send("매주 목요일\n단, 게임시작 첫째주 제외")
    if message.content.startswith("/질문-타이어 탈거") or message.content.startswith("타이어 안빠짐"):
        await message.channel.send("작기로 차를 들어올리고 뺀다")
    if message.content.startswith("/질문-낄유 만들기") or message.content.startswith("낄유 만드는법"):
        await message.channel.send("통에 설탕 6팩과 이스트 하나를 넣고 물을 채우고 기다린다")
    if message.content.startswith("/질문-하요시코사라짐") or message.content.startswith("하요시코 없어짐"):
        await message.channel.send("키를 받은 상태에서 자고 일어나면 마을에있는 검사소 옆에 주차되어있다.")

access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)


#if message.content.startswith(""):
#        await message.channel.send("")
