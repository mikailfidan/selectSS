#!/usr/bin/env python3
import requests,subprocess, os
from bs4 import BeautifulSoup


def sendmessage(title, message):
    subprocess.Popen(['notify-send', title, message])
    return


def searchW(word):

    try:
        contenturl = requests.get('http://seslisozluk.net/' + word + '-nedir-ne-demek/').content
    except:

        sendmessage("ERROR !", "Check Connection")

    soup = BeautifulSoup(contenturl, "html.parser")


    findall = soup.find_all("dd", {"class": "ordered-list"})
    selected = ""
    total=0

    for result in findall[0:3]:
        words = result.find_all("a")
        ornek = result.find_all("q")
        total=total+1
        for a in words:
            selected = selected + a.string + '\n'

    if total == 0:
        sendmessage(word,"Not found in the directory")
    else:
        sendmessage(word, selected)


xclip = os.popen("xclip -o").read()
xclip = xclip.strip()

searchW(xclip)
