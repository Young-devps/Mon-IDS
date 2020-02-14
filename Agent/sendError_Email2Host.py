# coding: utf-8

import urllib3
import time

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from fabric.api import *

def send_error(t2, name):

    env.host_string = 'XXX.com'
    env.user = 'user'
    env.password = 'PASSWORD'

    # On récupère les connexions actives du serveur distant
    adresses_ip = run("netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n")
    
    msg = MIMEMultipart()
    msg['From'] = 'johnDoe@gmail.com'
    msg['To'] = 'johnDoe@gmail.com'
    msg['Subject'] = 'Temps de réponse: {0} {1}s'.format(name, t2) 
    message = 'Temps de réponse: {0} - {1}'.format(t2, adresses_ip)
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('jordiibayo@gmail.com', 'trillers')
    mailserver.sendmail('jordiibayo@gmail.com', 'jordiibayo@gmail.com', msg.as_string())
    mailserver.quit()

t1 = time.time()

try:
    response = urllib3.urlopen('http://XXX.com')
    html = response.read()
except:
    t2 = time.time() - t1
    send_error(t2, "EXCEPTION")

t2 = time.time() - t1

if t2 > 5:
    send_error(t2, "TIMEOUT")
