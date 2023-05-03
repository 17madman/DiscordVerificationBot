import discord
from subprocess import check_output
import io
import time
import asyncio
import json
import os
import requests
from datetime import date


def IDVerification(id):
    with open('userID.txt', 'w') as f:
        f.write(id)

    p = check_output(['node', 'discordVerification.js'])
    p = str(p)

    isStudent = False
    if ("false" in p):
        isStudent = False
    else:
        isStudent = True

    return isStudent

intents = discord.Intents.default()
intents.message_content = True 
intents.voice_states = True
intents.members = True
client = discord.Client(intents=intents)

global messageChannel


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Verifying Students'))




@client.event
async def on_message(message):
    if ("ticket" in message.channel.name) and (message.author.id != 1099412234154803211) and (message.author.id != 508391840525975553):
        studID = message.content
        isStudent = IDVerification(studID)
        userID = message.author.id

        logchannel = client.get_channel(882624153545506837)
        role = discord.utils.get(message.guild.roles,name="Members")
        target_member = message.guild.get_member(int(userID))

        if (isStudent == True):
                    
            await target_member.add_roles(role)
            await message.channel.send("You have been verified! This channel will be closed in a few seconds.")
            await logchannel.send(f"{studID}, verified")

            time.sleep(10)
            await message.channel.delete()
                    
        else:
            await message.channel.send("Invalid student ID! Try sending it again. It should look like: 'nss5405'. If you keep getting this error, wait and a staff member will be able to assist you within a few hours.")

        
        return


    #message.guild.get_member(255002520236064768)
    #print(message.channel.id)
    #if (message.channel.id != 729321259065802783) and (message.channel.id != 883157408136962088):
        #if message.author.id == 508391840525975553:
            #embed = message.embeds[0]
            #if embed.description == "Please enter your PSU User ID in order to be verified.":
                #messageChannel = message.channel.id
                #studID = embed.description
                #isStudent = IDVerification(studID)

                #userID = embed.footer.text.split(" | ")
                #theirID = userID[1].strip()

                #role = discord.utils.get(message.guild.roles,name="Members")
                #target_member = message.guild.get_member(int(theirID))
                
                #if (isStudent == True):
                    
                    #await target_member.add_roles(role)
                    #await message.channel.send("You have been verified! This channel will be closed in a few seconds.")

                    #time.sleep(10)
                    #await message.channel.send(f"=aclose {studID}, verified")
                    
                #else:
                    #await message.channel.send("Invalid student ID! Try sending it again. It should look like: 'nss5405'. If you keep getting this error, wait and a staff member will be able to assist you within a few hours.")

                #return
        



client.run('MTA5OTQxMjIzNDE1NDgwMzIxMQ.Ghy1Kd.bpR0zv1Zv0h3Td30F8xhex5h0x5Nj3eIjWWvos')