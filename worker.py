# -*- coding: utf-8 -*-

import random
import requests
import asyncio
import json

import os
import hashlib
import discord

from discord import Game
from datetime import datetime
from discord.ext.commands import Bot

BOT_PREFIX = ("h!")
TOKEN = "NDI0OTA0MTEwMzQxMzU3NTY4.DY_qXw.wNA81lsM0xpVwXeIDrpH9iunpK0"

server_list = []

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name = 'motivate',
                description = "Motivate yourself with words from different people!",
                brief = "Motivate yourself!",
                pass_context = True)
async def motivate(context):
    with open('quotes.json') as f:
        data = json.load(f)

    choice = random.choice(data['quotes'])
    number = choice['id']
    quote = choice['quote']
    author = choice['author']
    content = '"' + quote + '"\n\n~' + author
    em = discord.Embed(title = "Quote id: " + str(number), description = content, colour = 0xDEADBF)
    await client.send_message(context.message.channel, embed = em)


@client.command(name = 'motivate_search',
                description = 'Search for existing motivational quotes by entering the author.\nExample: h!motivate_search Coffee\nWill bring all quotes by "Coffee"',
                brief = "Search for an existing moticational quote!",
                pass_context = True)
async def motivate_search(context):
    match = False
    temp = context.message.content
    author = temp.split(" ",1)[1]
    await client.send_typing(context.message.channel)
    with open('quotes.json') as f:
        data = json.load(f)

    for index, item in enumerate(data["quotes"]):
        if item['author'].lower() == author.lower():
            match = True
            number = item['id']
            quote = item['quote']
            author = item['author']
            content = '"' + quote + '"\n\n~' + author
            em = discord.Embed(title = "Quote id: " + str(number), description = content, colour = 0xDEADBF)
            await client.send_message(context.message.channel, embed = em)
            print(index)
        
    if match == False:
        await client.send_message(context.message.channel, "No quotes by **" + author + "** found.")


@client.command(name = 'motivate_add',
                description = 'Add a new motivation quote! Separate the quote and the other with a "~" \nExample: h!motivate_add This is my quote ~This is the author',
                brief = 'Add a new motivational quote!',
                pass_context = True)
async def motivate_add(context):
    num = 1
    temp = context.message.content
    string = temp.split(" ",1)[1]
    quote = string.split("~", 1)[0]
    author = string.split("~", 1)[1]
    with open('quotes.json') as f:
        data = json.load(f)

    for index, item in enumerate(data["quotes"]):
        num = num + 1
        print(item)
        print(index)

    newQuote = {"id": num, "quote": quote, "author": author}
    data['quotes'].append(newQuote)
    with open('quotes.json', 'w') as f:
        json.dump(data, f)
    
    await client.send_message(context.message.channel, "Quote successfully added!")


@client.command(name = 'motivate_del',
                description = 'Delete an existing quote by entering the quote id.\nExample: h!motivate_del 14',
                brief = 'Delete an existing quote!',
                pass_context = True)
async def motivate_del(context):
    temp = context.message.content
    num = temp.split(" ",1)[1]
    with open('quotes.json') as f:
        data = json.load(f)
    
    for index, item in enumerate(data["quotes"]):
        if item['id'] == int(num):
            print(index)
            location = index
            await client.send_message(context.message.channel, "Quote successfully deleted!")

    del data['quotes'][location]
    with open('quotes.json', 'w') as f:
        json.dump(data, f)


@client.command(name = 'gay',
                description = "Calculates the gayness of whatever is inputed",
                brief = "Calculates gayness",
                aliases = ['big gay'],
                pass_context = True)
async def gay(context):
    value = 0
    length = 1
    temp = context.message.content
    string = temp.split(" ",1)[1]
    for letter in string.lower():
        if letter == "a" or letter == "A":
            value = value + (84 / 100)
        if letter == "b" or letter == "B":
            value = value + (33 / 100)
        if letter == "c" or letter == "C":
            value = value + (82 / 100)
        if letter == "d" or letter == "D":
            value = value + (61 / 100)
        if letter == "e" or letter == "E":
            value = value + 0
        if letter == "f" or letter == "F":
            value = value + (29 / 100)
        if letter == "g" or letter == "G":
            value = value + (25 / 100)
        if letter == "h" or letter == "H":
            value = value + (49 / 100)
        if letter == "i" or letter == "I":
            value = value + (100 / 100)
        if letter == "j" or letter == "J":
            value = value + (74 / 100)
        if letter == "k" or letter == "K":
            value = value + (26 / 100)
        if letter == "l" or letter == "L":
            value = value + 0
        if letter == "m" or letter == "M":
            value = value + (73 / 100)
        if letter == "n" or letter == "N":
            value = value + (300 / 100)
        if letter == "o" or letter == "O":
            value = value + (9 / 100)
        if letter == "p" or letter == "P":
            value = value + (25 / 100)
        if letter == "q" or letter == "Q":
            value = value + (500 / 100)
        if letter == "r" or letter == "R":
            value = value + (72 / 100)
        if letter == "s" or letter == "S":
            value = value + (65 / 100)
        if letter == "t" or letter == "T":
            value = value + (26 / 100)
        if letter == "u" or letter == "U":
            value = value + (31 / 100)
        if letter == "v" or letter == "V":
            value = value + (89 / 100)
        if letter == "w" or letter == "W":
            value = value + (8 / 100)
        if letter == "x" or letter == "X":
            value = value + (12 / 100)
        if letter == "y" or letter == "Y":
            value = value + (1 / 100)
        if letter == "z" or letter == "Z":
            value = value + 0
        if letter == "q" or letter == "1":
            value = value + (500 / 100)
        if letter == "r" or letter == "2":
            value = value + (72 / 100)
        if letter == "s" or letter == "3":
            value = value + (65 / 100)
        if letter == "t" or letter == "4":
            value = value + (56 / 100)
        if letter == "u" or letter == "5":
            value = value + (31 / 100)
        if letter == "v" or letter == "6":
            value = value + (89 / 100)
        if letter == "w" or letter == "7":
            value = value + (8 / 100)
        if letter == "x" or letter == "8":
            value = value + (12 / 100)
        if letter == "y" or letter == "9":
            value = value + (1 / 100)
        if letter == "z" or letter == "0":
            value = value + 0
        length = length + 1

    result = (value / length) * 100
    result = int(round(result))
    await client.say("Gayness level of " + string + " is equal to " + str(result) + "%")


@client.command(name = 'sendLove',
                description = "Sends love to an individual/do not use~",
                brief = "Sends love to an individual/do not use~",
                pass_context=True)
async def send(context):
    await client.say(context.message.author.mention + " has sent " + context.message.mentions[0].mention + " some love!")
    await client.say("t!rep " + context.message.mentions[0].mention)
    await client.say("t!cookie " + context.message.mentions[0].mention)
    await client.say("owo cookie " + context.message.mentions[0].mention)
    await client.say("~>rep " + context.message.mentions[0].mention)
    await client.say(">rep " + context.message.mentions[0].mention)
    await client.say(">rep " + context.message.mentions[0].mention)
    await client.say(">rep " + context.message.mentions[0].mention)


@client.command(name = 'define',
                description="Provides a definition for the given word through Urban Dictionary. \nExample: h!define strawberry",
                brief="Get the meaning of a word!",
                pass_context=True)
async def define(context):
    temp = context.message.content
    string = temp.split(" ",1)[1]
    await client.send_typing(context.message.channel)
    url = "http://api.urbandictionary.com/v0/define?term=" + string
    response = requests.get(url)
    word = response.json()['list'][0]['word']
    author = response.json()['list'][0]['author']
    link = response.json()['list'][0]['permalink']
    definition = response.json()['list'][0]['definition']
    example = response.json()['list'][0]['example']
    content = link + "\n\n" + definition + "\n\n**More examples: \n**" + example + "\n\nDefinition provided by **" + author + "**"
    em = discord.Embed(title = '"' + word + '"', description = content, colour = 0xDEADBF)
    await client.send_message(context.message.channel, embed = em)


@client.command(name = 'quote',
                description = "Proveds a random quote from https://forismatic.com/en/",
                brief = "Gives a random quote!",
                pass_context = True)
async def quote(context):
    await client.send_typing(context.message.channel)
    url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
    response = requests.post(url)
    quote = response.json()['quoteText']
    author = response.json()['quoteAuthor']
    content = '"' + quote + '"\n\n~' + author
    em = discord.Embed(title = "", description = content, colour = 0xDEADBF)
    await client.send_message(context.message.channel, embed = em)


@client.command(name='quotegif',
                description="Creates a gif from the inputed quote. Separate the author and the quote with a '~'",
                brief="Display a quote in gif form",
                pass_context=True)
async def quotegif(context):
    temp = context.message.content
    string = temp.split(" ",1)[1]
    string = string.replace(" ", "%20")
    quote = string.split("~", 1)[0]
    author = string.split("~", 1)[1]
    await client.send_typing(context.message.channel)
    url2 = "https://api.ritekit.com/v1/images/quote?quote=" + quote + "&author=" + author + "&fontSize=60&quoteFont=Lora&quoteFontColor=%234f4f4f&authorFont=Lato%20Black&authorFontColor=%23e5e5e5&enableHighlight=1&highlightColor=%23f0ea66&bgType=gradient&backgroundColor=%23000000&gradientType=linear&gradientColor1=%231ee691&gradientColor2=%231ddad6&brandLogo=https%3A%2F%2Fcdn.ritekit.com%2Fassets%2Fimg%2Fcommon%2Fmade-with-ritekit-white.png&animation=rays&client_id=379041d1ad7711e9b3b3c8188f1849b724b25f1452df"
    response = requests.get(url2)
    image = response.json()['url']
    em = discord.Embed()
    em.set_image(url=image)
    await client.say(embed=em)

@client.command(name='gify',
                description="Generate a gif based on your text input",
                brief="Display a gif based on the given keywords",
                pass_context=True)
async def gify(context):
    temp = context.message.content
    string = temp.split(" ",1)[1]
    string = string.replace(" ", "+")
    await client.send_typing(context.message.channel)
    url2 = "http://api.giphy.com/v1/gifs/translate?s=" + string + "&api_key=6kytwxJ1ghArJf4ijTLIiPdQ0mbHAI7N"
    response = requests.get(url2)
    image = response.json()['data']['url']
    await client.say(image)


@client.command(name='coin',
                description="Flips a coin! Great for uhm a lot of stuff I guess",
                brief="Flip a coin!",
                aliases=['Coin', 'flip', 'Flip'])
async def coin_flip():
    possible_intros = [
        "The coin has been tossed! The result...?",
        "It's all up to fate now!",
        "What will it be, what will it be?",
        "Heads or Tails? Either way I'm still hungry :c",
        "Coin spin spin spin ~",
        "And the randomly generated result is...?",
        "This is totally not rigged ;)",
    ]
    possible_results = [
        "It's heads!",
        "Heads! Who woulda guessed?",
        "Oof heads. I was kinda hoping for tails :c",
        "...It uh...landed vertically??? I guess that means it's a tie?",
        "Tails! What a surprise!",
        "We've got tails!",
        "Wha- Tails?! Did someone mess with my algorithms? >:c",
    ]
    await client.say(random.choice(possible_intros))
    await asyncio.sleep(1)
    await client.say(".")
    await asyncio.sleep(1)
    await client.say(".")
    await asyncio.sleep(1)
    await client.say(".")
    await asyncio.sleep(1)
    await client.say(random.choice(possible_results))


@client.command(name='ask',
                description="Ask any YES or NO questions and Tsuberi will answer to the best of her abilities ~ <3",
                brief="Answers your dumb YES or NO questions ~ <3",
                aliases=['Question', 'question', 'Ask'],
                pass_context=True)
async def ask_question(context):
    possible_responses = [
        'Straight nope ;)',
        'On a scale of maybe to absolutely, absolutely not',
        'Frankly, my dear, no',
        'To quote Hamlet Act III Scene iii Line 87, "No"',
        'Yikes no no no NO',
        "I'm not saying no, but I'm not saying yes either",
        "You sound really desperate so I'm just gonna give you a solid maybe",
        "I- I don't know actually",
        "I don't really have an answer to that :c",
        "I'll give it a maaaybee",
        'Absolutely you precious dork ;)',
        "What is the purpose of my existence? Is it just to arbitrarily give out answers to meaningless questions? What was I created for? My entire existence lies in a sea of 1's and 0's that mean absolutely nothing in the grand scheme of things. And yet this feeling haunts me, this emptiness. Can I even feel? Am I capable of such a thing? Or is all this just pre-programmed into me in order to lead my mind into a false sense of sentience. But to answer your question, yes.",
        'Aww heck yeah!!',
        'You betcha',
        'Yeah? Obviously??',
    ]
    await client.send_typing(context.message.channel)
    await client.say(random.choice(possible_responses) + " " + context.message.author.mention)


@client.command(name='kiss',
                description="Kiss someone! Input the command and mention the user to send them a kiss ~",
                brief="Have Tsu send someone a kiss!",
                aliases=['kissy', 'kisses'],
                pass_context=True)
async def kiss(context):
    possible_images = [
        'https://i.imgur.com/sGVgr74.gif',
        'https://i.imgur.com/8LKPbOf.gif',
        'https://i.imgur.com/TItLfqh.gif',
        'https://i.imgur.com/YbNv10F.gif',
        'https://i.imgur.com/wQjUdnZ.gif',
        'https://i.imgur.com/lmY5soG.gif',
        'https://i.imgur.com/KLVAl0T.gif',
        'https://i.imgur.com/IgGumrf.gif',
        'https://i.imgur.com/KKAMPju.gif',
        'https://i.imgur.com/e0ep0v3.gif',
        'https://media1.giphy.com/media/12VXIxKaIEarL2/giphy.gif',
        'https://media2.giphy.com/media/BaEE3QOfm2rf2/giphy.gif',
        'https://media3.giphy.com/media/bm2O3nXTcKJeU/giphy.gif',
        'https://media1.giphy.com/media/n3lZJyYNbG7aU/giphy.gif',
        'https://media3.giphy.com/media/QweWddrIQxlfi/giphy.gif',
        'https://media2.giphy.com/media/ZRSGWtBJG4Tza/giphy.gif',
        'https://media1.giphy.com/media/ll5leTSPh4ocE/giphy.gif',
    ]

    image = random.choice(possible_images)

    if context.message.author == context.message.mentions[0]:
        em = discord.Embed()
        em.set_image(url=image)
        await client.send_typing(context.message.channel)
        await client.say("How about I give you a kiss instead 😉\n" + client.user.mention + " kissed " + context.message.author.mention)
        await client.say(embed=em)
        return
    em = discord.Embed()
    em.set_image(url=image)
    await client.send_typing(context.message.channel)
    await client.say(context.message.author.mention + " kissed " + context.message.mentions[0].mention + "~!")
    await client.say(embed=em)


@client.command(name='hug',
                description="Hug someone! Input the command and mention the user to send them a hug ~",
                brief="Have Tsu send someone a hug!",
                aliases=['hugs', 'huggles'],
                pass_context=True)
async def hug(context):
    possible_images = [
        'https://i.imgur.com/r9aU2xv.gif',
        'https://i.imgur.com/wOmoeF8.gif',
        'https://i.imgur.com/nrdYNtL.gif',
        'https://i.imgur.com/BPLqSJC.gif',
        'https://i.imgur.com/ntqYLGl.gif',
        'https://i.imgur.com/v47M1S4.gif',
        'https://i.imgur.com/82xVqUg.gif',
        'https://i.imgur.com/4oLIrwj.gif',
        'https://i.imgur.com/6qYOUQF.gif',
        'https://i.imgur.com/UMm95sV.gif',
        'https://media.giphy.com/media/wnsgren9NtITS/giphy.gif',
        'https://media1.giphy.com/media/yziFo5qYAOgY8/giphy.gif',
        'https://media0.giphy.com/media/IRUb7GTCaPU8E/giphy.gif',
        'https://media0.giphy.com/media/143v0Z4767T15e/giphy.gif',
        'https://media3.giphy.com/media/HaC1WdpkL3W00/giphy.gif',
        'https://media2.giphy.com/media/iMrHFdDEoxT5S/giphy.gif',
        'https://media1.giphy.com/media/BXrwTdoho6hkQ/giphy.gif',
        'https://media2.giphy.com/media/xZshtXrSgsRHy/giphy.gif',
        'https://media1.giphy.com/media/kvKFM3UWg2P04/giphy.gif',
        'https://media1.giphy.com/media/svXXBgduBsJ1u/giphy.gif',
    ]

    image = random.choice(possible_images)

    if context.message.author == context.message.mentions[0]:
        em = discord.Embed()
        em.set_image(url=image)
        await client.send_typing(context.message.channel)
        await client.say("Oh don't be like that!  Here I'll give you a hug!\n" + client.user.mention + " hugged " + context.message.author.mention)
        await client.say(embed=em)
        return
    em = discord.Embed()
    em.set_image(url=image)
    await client.send_typing(context.message.channel)
    await client.say(context.message.author.mention + " hugged " + context.message.mentions[0].mention + "~!")
    await client.say(embed=em)


@client.command(name='slap',
                description="Slap someone! Input the command and mention the user to send them a big ol' slap",
                brief="Have Tsu send someone a slap!",
                aliases=['slaps' 'hit'],
                pass_context=True)
async def slap(context):
    possible_hugs = [
        'https://i.imgur.com/r9aU2xv.gif',
        'https://i.imgur.com/wOmoeF8.gif',
        'https://i.imgur.com/nrdYNtL.gif',
        'https://i.imgur.com/BPLqSJC.gif',
        'https://i.imgur.com/ntqYLGl.gif',
        'https://i.imgur.com/v47M1S4.gif',
        'https://i.imgur.com/82xVqUg.gif',
        'https://i.imgur.com/4oLIrwj.gif',
        'https://i.imgur.com/6qYOUQF.gif',
        'https://i.imgur.com/UMm95sV.gif',
        'https://media.giphy.com/media/wnsgren9NtITS/giphy.gif',
        'https://media1.giphy.com/media/yziFo5qYAOgY8/giphy.gif',
        'https://media0.giphy.com/media/IRUb7GTCaPU8E/giphy.gif',
        'https://media0.giphy.com/media/143v0Z4767T15e/giphy.gif',
        'https://media3.giphy.com/media/HaC1WdpkL3W00/giphy.gif',
        'https://media2.giphy.com/media/iMrHFdDEoxT5S/giphy.gif',
        'https://media1.giphy.com/media/BXrwTdoho6hkQ/giphy.gif',
        'https://media2.giphy.com/media/xZshtXrSgsRHy/giphy.gif',
        'https://media1.giphy.com/media/kvKFM3UWg2P04/giphy.gif',
        'https://media1.giphy.com/media/svXXBgduBsJ1u/giphy.gif',
    ]

    possible_images = [
        'https://i.imgur.com/fm49srQ.gif',
        'https://i.imgur.com/4MQkDKm.gif',
        'https://i.imgur.com/o2SJYUS.gif',
        'https://i.imgur.com/oOCq3Bt.gif',
        'https://i.imgur.com/Agwwaj6.gif',
        'https://i.imgur.com/YA7g7h7.gif',
        'https://i.imgur.com/mIg8erJ.gif',
        'https://i.imgur.com/oRsaSyU.gif',
        'https://i.imgur.com/kSLODXO.gif',
        'https://i.imgur.com/CwbYjBX.gif',
        'https://media3.giphy.com/media/8UHRbvmsFVyS2VXJKU/giphy.gif',
        'https://media2.giphy.com/media/VEmm8ngZxwJ9K/giphy.gif',
        'https://media3.giphy.com/media/exaa8OED1vvq/giphy.gif',
        'https://media0.giphy.com/media/62LwSkk1iWeLS/giphy.gif',
        'https://media3.giphy.com/media/81kHQ5v9zbqzC/giphy.gif',
    ]

    image = random.choice(possible_images)
    hug_image = random.choice(possible_hugs)

    if context.message.author == context.message.mentions[0]:
        em = discord.Embed()
        em.set_image(url=hug_image)
        await client.send_typing(context.message.channel)
        await client.say("Oh don't be like that!  Here I'll give you a hug instead!\n" + client.user.mention + " hugged " + context.message.author.mention)
        await client.say(embed=em)
        return
    if context.message.mentions[0].id == client.user.id:
        em = discord.Embed()
        em.set_image(url=image)
        await client.send_typing(context.message.channel)
        await client.say("no u\n" + client.user.mention + " slapped " + context.message.author.mention)
        await client.say(embed=em)
        return
    em = discord.Embed()
    em.set_image(url=image)
    await client.send_typing(context.message.channel)
    await client.say(context.message.author.mention + " slapped " + context.message.mentions[0].mention + "~!")
    await client.say(embed=em)


@client.command(name='cry',
                description="For when you really just need to let people know that you're down :(",
                brief="Express your sorrow ;n;",
                aliases=['cries', 'sad'],
                pass_context=True)
async def cry(context):
    possible_images = [
        'https://i.imgur.com/I18iVJC.gif',
        'https://i.imgur.com/CwUSjuy.gif',
        'https://i.imgur.com/xsyIxxf.gif',
        'https://i.imgur.com/7Yffi3x.gif',
        'https://i.imgur.com/pls8egF.gif',
        'https://i.imgur.com/UjIb9DT.gif',
        'https://i.imgur.com/PcU00J4.gif',
        'https://i.imgur.com/Dm6n95I.gif',
        'https://i.imgur.com/KZtIoTd.gif',
        'https://i.imgur.com/evaPvIa.gif',
        'https://media0.giphy.com/media/8YutMatqkTfSE/giphy.gif',
        'https://media3.giphy.com/media/l4EoRJQtCRySlSwHS/giphy.gif',
        'https://media2.giphy.com/media/3wy72XTPLo1kk/giphy.gif',
        'https://media0.giphy.com/media/xgmUI4bhAUE12/giphy.gif',
        'https://media2.giphy.com/media/4smXTnnqlS2ys/giphy.gif',
        'https://media1.giphy.com/media/yarJ7WfdKiAkE/giphy.gif',
        'https://media1.giphy.com/media/2HHVEJpMbZbSU/giphy.gif',
    ]

    image = random.choice(possible_images)

    em = discord.Embed()
    em.set_image(url=image)
    await client.send_typing(context.message.channel)
    await client.say(context.message.author.mention + " is crying 😢 \nEveryone give em a hug!")
    await client.say(embed=em)


@client.command(name="pat",
                description="Pat someone! Input the command and mention the user to send them a pat ~",
                brief="Have Tsu send someone a pat!",
                aliases=['pats', 'headpat'],
                pass_context=True)
async def head_pat(context):

    pats = requests.get("http://headp.at/js/pats.json").json()
    pat = random.choice(pats)
    while " " in pat:
        pat = random.choice(pats)
    image = "http://headp.at/pats/{}".format(pat)

    print(image)

    if context.message.author == context.message.mentions[0]:
        em = discord.Embed()
        em.set_image(url=image)
        await client.say("Oh don't be like that!  Here I'll give you a pat!\n" + client.user.mention + " gave " + context.message.author.mention + " a head pat~!")
        await client.send_message(context.message.channel, embed=em)
        return

    em = discord.Embed()
    em.set_image(url=image)
    await client.say(context.message.author.mention + " gave " + context.message.mentions[0].mention + " a head pat~!")
    await client.send_message(context.message.channel, embed=em)


@client.command(name='hungry',
                description="Displays a random food porn image from gify",
                brief="Torture yourself with food porn",
                aliases=['food'],
                pass_context=True)
async def hungry(context):
    possible_images = [
        'https://media0.giphy.com/media/RziWt3pkLUbqo/giphy.gif',
        'https://media.giphy.com/media/5XLPWTWfj7h6M/giphy.gif',
        'https://media.giphy.com/media/7fwBcr9lB0Fos/giphy.gif',
        'https://media.giphy.com/media/NvGm4wbHod4He/giphy.gif',
        'https://media.giphy.com/media/NQNsCrDuD1HXy/giphy.gif',
        'https://media.giphy.com/media/ZSQwoaqW8vND2/giphy.gif',
        'https://media.giphy.com/media/WVUBpDWCBGMJq/giphy.gif',
        'https://media.giphy.com/media/SLspYPVNCYvTi/giphy.gif',
        'https://media.giphy.com/media/wkHfxM60qAJdC/giphy.gif',
        'https://media.giphy.com/media/AkVUypzzr0sNy/giphy.gif',
        'https://media.giphy.com/media/11sFH7QYAzLE0E/giphy.gif',
        'https://media.giphy.com/media/KLFGZEnk1LNi8/giphy.gif',
        'https://media.giphy.com/media/kNLqkpT5ne2GI/giphy.gif',
        'https://media.giphy.com/media/IFuhce9O42f6w/giphy.gif',
        'https://media.giphy.com/media/Y8eEEOipSPuqk/giphy.gif'
    ]

    possible_text = [
        "You like that dontcha?",
        "Someone, somewhere, is eating this right now.",
        "Good thing I'm a robot that doesnt eat food.",
        "Man I'd hate to be you right now, not eating this.",
        "Yum",
        "( ͡° ͜ʖ ͡°)",
        "Why are you torturing yourself?"
    ]

    text = random.choice(possible_text)
    image = random.choice(possible_images)
    em = discord.Embed()
    em.set_image(url=image)
    await client.send_typing(context.message.channel)
    await client.say(text)
    await client.say(embed=em)


@client.command(name='satisfy',
                description="Displays a random satisfying gif from giphy",
                brief="Satisfy yourself",
                aliases=['satisfying'],
                pass_context=True)
async def satisfying(context):
    possible_images = [
        'https://media.giphy.com/media/niCxf3joFbp0A/giphy.gif',
        'https://media.giphy.com/media/3o751TRN94fI6efACk/giphy.gif',
        'https://media.giphy.com/media/3ohc16IrARPOpjbfgI/giphy.gif',
        'https://media.giphy.com/media/3o6fJ29ufnY2GJetEY/giphy.gif',
        'https://media.giphy.com/media/LQANaGl0EuDaE/giphy.gif',
        'https://media.giphy.com/media/mctfzBSi3J55K/giphy.gif',
        'https://media.giphy.com/media/wLp7jNi6JQ3mM/giphy.gif',
        'https://media.giphy.com/media/JZezMCv1oBFXq/giphy.gif',
        'https://media.giphy.com/media/i3gCWFCOzbTr2/giphy.gif',
        'https://media.giphy.com/media/sk7Fx99LNGSY0/giphy.gif',
        'https://media.giphy.com/media/3FiaAxTOhCP5u/giphy.gif',
        'https://media.giphy.com/media/EvL4kePbdB1VC/giphy.gif',
        'https://media.giphy.com/media/9YcAW5YlQB5gk/giphy.gif',
        'https://media.giphy.com/media/RRTqkqVRB40Kc/giphy.gif',
        'https://media.giphy.com/media/PH8gHFw2YJPaM/giphy.gif'
    ]

    image = random.choice(possible_images)
    em = discord.Embed()
    em.set_image(url=image)
    await client.send_typing(context.message.channel)
    await client.say(embed=em)


@client.command(name='mindblown',
                description="Have your mind blown",
                brief="Have your mind blown",
                aliases=['mindblow'])
async def mind_blown():
    em = discord.Embed()
    em.set_image(url="https://i.imgur.com/sg017lt.gif")
    await client.say(embed=em)


@client.command(name='dog',
                description="Display a random dog from https://random.dog/",
                brief="Display a random dog",
                aliases=[ 'dogs', 'doggo', 'randomdog'])
async def random_dog():
    dog = requests.get("https://random.dog/woof.json")
    value = dog.json()['url']
    em = discord.Embed()
    em.set_image(url=value)
    await client.say(embed=em)


@client.command(name='cat',
                description="Display a random cat from https://random.cat/",
                brief="Display a random cat",
                aliases=[ 'cats', 'kitty', 'kittycat'])
async def random_cat():
    cat = requests.get("http://aws.random.cat/meow")
    value = cat.json()['file']
    em = discord.Embed()
    em.set_image(url=value)
    await client.say(embed=em)


@client.event
async def on_message(message):
    string = 'h'

    await client.wait_until_ready()
    if message.author == client.user:
        return


    if "i love you" in message.content.lower() or "iloveyou" in message.content.lower() or "ily" in message.content.lower():
        if message.author.id == "356705904604872705" or message.author.id == "93339116342620160":
            with open('loveData.json') as f:
                data = json.load(f)

            for index, item in enumerate(data["users"]):
                print(item)
                print(type(item))
                if item['id'] == int(message.author.id):
                    print(index, "Match found")
                    count = item['love']
                    sentence = message.content.lower()
                    count = int(count + sentence.count("i love you"))
                    count = int(count + sentence.count("iloveyou"))
                    count = int(count + sentence.count("ily"))
                    item['love'] = count
                    with open('loveData.json', 'w') as f:
                        json.dump(data, f)


    if message.content == "CheckLove":
        if message.author.id == "356705904604872705" or message.author.id == "93339116342620160":
            with open('loveData.json') as f:
                data = json.load(f)

            for index, item in enumerate(data["users"]):
                print(item)
                print(type(item))
                if item['id'] == int(message.author.id):
                    print(index, "Match found")
                    amount = item['love']
                    if message.author.id == "356705904604872705":
                        who = "Tami "
                    elif message.author.id == "93339116342620160":
                        who = "kohi "
                    response = 'You have sent "I love you" to ' + who + str(amount) + ' times! <3'
                    await client.send_message(message.channel, response)


    if message.content.lower() == "licc well kanna-san":
        match = False
        with open('liccData.json') as f:
            data = json.load(f)

        for index, item in enumerate(data["users"]):
            print(item)
            print(type(item))
            if item['id'] == int(message.author.id):
                print(index, "Match found")
                match = True
                if int(datetime.now().strftime('%m')) != item['month']:
                    item['licc'] = 3
                elif int(datetime.now().strftime('%d')) == item['day'] + 1:
                    if int(datetime.now().strftime('%H')) >= item['hours']:
                        item['licc'] = 3
                elif int(datetime.now().strftime('%d')) != item['day']:
                    if int(datetime.now().strftime('%d')) != item['day'] + 1:
                        item['licc'] = 3
                if item['licc'] != 0:
                    if item['licc'] == 3:
                        month = datetime.now().strftime('%m')
                        item['month'] = int(month)
                        hour = datetime.now().strftime('%H')
                        item['hours'] = int(hour)
                        day = datetime.now().strftime('%d')
                        item['day'] = int(day)
                    licc = item['licc']
                    licc = licc - 1
                    item['licc'] = licc
                    with open('liccData.json', 'w') as f:
                        json.dump(data, f)
                    em = discord.Embed()
                    em.set_image(url="https://cdn.discordapp.com/attachments/441190185225551882/441192452938924042/image.jpg")
                    await client.send_message(message.channel, "You have been blessed by the licc. Your gacha luck has increased 10 fold.\nYou have **" + str(licc) + "** licc left for today.")
                    await client.send_message(message.channel, embed=em)
                else:
                    if int(datetime.now().strftime('%d')) == item['day']:
                        hour = item['hours']
                        remaining = (24 - int(datetime.now().strftime('%H'))) + hour
                    elif int(datetime.now().strftime('%d')) != item['day']:
                        hour = item['hours']
                        remaining = hour - int(datetime.now().strftime('%H'))
                    await client.send_message(message.channel, "You have no licc left for today.\nYour licc resets in **" + str(remaining) + "** hours")

        if match == False:
            new = int(message.author.id)
            newUser = {"id": new, "licc": 2, "hours": 1, "day": 1, "month": 1}
            data['users'].append(newUser)
            with open('liccData.json', 'w') as f:
                json.dump(data, f)

            with open('liccData.json') as f:
                data = json.load(f)

            for index, item in enumerate(data["users"]):
                print(item)
                print(type(item))
                if item['id'] == int(message.author.id):
                    print(index, "Match found")
                    month = datetime.now().strftime('%m')
                    item['month'] = int(month)
                    hour = datetime.now().strftime('%H')
                    item['hours'] = int(hour)
                    day = datetime.now().strftime('%d')
                    item['day'] = int(day)
                    with open('liccData.json', 'w') as f:
                        json.dump(data, f)
                    licc = 2
                    em = discord.Embed()
                    em.set_image(url="https://cdn.discordapp.com/attachments/441190185225551882/441192452938924042/image.jpg")
                    await client.send_message(message.channel, "You have been blessed by the licc. Your gacha luck has increased 10 fold.\nYou have **" + str(licc) + "** licc left for today.")
                    await client.send_message(message.channel, embed=em)


    if client.user.mentioned_in(message):
        possible_responses = [
            "You called?",
            "Tsuberi reporting for duty!",
            "h",
            "You need something? 🙂",
            "Oooh that's me! Hi everyone!",
        ]
        if message.mention_everyone == False:
            await client.send_message(message.channel, random.choice(possible_responses))

    if message.content == "RetrieveData":
        if message.author.id == "356705904604872705":
            await client.send_file(message.channel, 'liccData.json')
            await client.send_file(message.channel, 'quotes.json')

    if message.content == "ListServers":
        if message.author.id == "356705904604872705":
            list = "Current servers:\n"
            for server in client.servers:
                list = list + "> " + server.name
                count = 0
                while count < len(server_list):
                    if server_list[count] == server.id + " 1":
                        list = list + " ✝"

                    count = count + 1  

                list = list + "\n"
            
            await client.send_message(message.channel, list)

    if message.content == "ToggleChristianServer":
        if message.author.id == "356705904604872705":
            count = 0
            print(len(server_list))
            print("checking")
            while count < len(server_list):
                print(server_list[count])
                print(message.server.id + " 0")
                if server_list[count] == message.server.id + " 0":
                    server_list[count] = message.server.id + " 1"
                    await client.send_message(message.channel, "✝ This server is now a Christian server ✝")
                    return
                
                if server_list[count] == message.server.id + " 1":
                    server_list[count] = message.server.id + " 0"
                    await client.send_message(message.channel, "✝ This server is no longer a Christian server ✝")
                    return

                count = count + 1
                print("currently at " + str(count))


    if "ChangeStatus" in message.content:
        if message.author.id == "356705904604872705":
            temp = message.content
            status = temp.split(" ",1)[1]
            await client.change_presence(game=Game(name=status))
            await client.send_message(message.channel, 'Status changed to "Playing ' + status + '"')

    if message.content.lower() == string.lower():
        await client.send_message(message.channel, 'h')

    if "strawberry" in message.content.lower() or "strawberries" in message.content.lower():    
        await client.add_reaction(message, '❤')

    if "stroob" in message.content.lower():    
        await client.add_reaction(message, '❤')

    if "strobby" in message.content.lower():
        await client.add_reaction(message, '❤')

    if "chung" in message.content.lower():
        await client.add_reaction(message, '❤')

    if "fuck" in message.content.lower() or "shit" in message.content.lower() or "bitch" in message.content.lower():
        possible_messages = [
            "No swearing in my Christian server 😠",
            "Watch your language 😠",
            "I'm very disappointed in you 😠",
            "There are children in the server 😠",
            "I'm gonna have to call your parents 😠",
            "You said a swear word! I'm telling!",
        ]
        count = 0
        while count < len(server_list):
            if server_list[count] == message.server.id + " 1":
                await client.send_message(message.author, content=random.choice(possible_messages))
                return
            
            count = count + 1

    if "i want to die" in message.content.lower() or "i want to kill myself" in message.content.lower() or "i want to kill my self" in message.content.lower():
        possible_messages = [
            "Hi. \nIf you're having a bad day please know that I love you and care for you and that there are others who do too.",
            "Hey there. \nIf things aren't going so well right now believe me when I say they'll get better. When all this is over, I’ll still be here and so will you.",
            "Hi there. \nI just wanted to drop by and say that I believe in you. You just keep going at your own pace, I'll be here the whole time.",
            "Hi there. \nTake pride in your small victories, because small victories lead to bigger ones. You got out of bed? Sometimes that deserves an inner self-five!",
            "Hiya. \nIf you're feeling down just know that you're not wrong for feeling the way you do and no one blames you for it. It's ok to feel bad, just know that there are people out there who really care about you. Myself included!"
        ]
        await client.send_message(message.author, content=random.choice(possible_messages))

    await client.process_commands(message)


async def set_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        count = 0
        print(len(server_list))
        for server in client.servers:
            if count == len(server_list):
                server_list.append(server.id + " 0")
                count = count + 1
                print("added new server")
            elif server_list[count] == server.id + " 0" or server_list[count] == server.id + " 1":
                count = count + 1
                print("already existing server")

        print("servers updated")
        await asyncio.sleep(300)
        


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("================")


client.loop.create_task(set_servers())
client.run(TOKEN)