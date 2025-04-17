import smtplib,ssl
from email.message import EmailMessage
import random

nimi=["mikolkyle@gmail.com"]
salas=["admin123"]
sees=False
user=""

def saada_email(tema:str, sisu:str, user_email:str):
 smtp_server='smtp.gmail.com'
 smtp_port=587
 saatja_email="mikolkyle@gmail.com"
 salasõna=input("Sisesta oma e-posti salasõna: ")
 msg=EmailMessage()
 msg['Subject']=tema
 msg['From']=saatja_email
 msg['To']=user_email
 msg.set_content(sisu)
 try:
  with smtplib.SMTP(smtp_server,smtp_port) as server:
   server.starttls(context=ssl.create_default_context())
   server.login(saatja_email,salasõna)
   server.send_message(msg)
  print(f"Kinnitus e-kiri saadetud {user_email}")
 except Exception as e:
  print(f"E-kirja saatmine ebaõnnestus: {e}")


def kontroll(p:str)->bool:
 s=0
 n=0
 e=0
 for t in p:
  if t.isupper():
   s+=1
  if t.isdigit():
   n+=1
  if not t.isalpha()and not t.isdigit():
   e+=1
 if len(p)>=8 and s>=1 and e>=1:
  return True
 return False

def reg():
 n=input("Nimi: ")
 if n in nimi:
  print("Nimi on olemas")
  return
 v=input("Ise või genereerida (i/g)? ")
 if v=="i":
  p=input("Parool: ")
  if kontroll(p):
   nimi.append(n)
   salas.append(p)
   print("Registreeritud")
   saada_email("Registreeritud", "Tere tulemast!", n)
  else:
   print("Parool on nõrk")
 elif v=="g":
  p=""
  while not kontroll(p):
   s1=".,:;!_*-+()/#¤%&"
   s2="0123456789"
   s3="qwertyuiopasdfghjklzxcvbnm"
   s4=s3.upper()
   s5=s1+s2+s3+s4
   ls=list(s5)
   random.shuffle(ls)
   p=''.join([random.choice(ls)for x in range(12)])
  print("Sinu parool on",p)
  nimi.append(n)
  salas.append(p)
  print("Registreeritud")
  saada_email("Registreeritud", "Tere tulemast!", n)

def login():
 global sees,user
 n=input("Nimi: ")
 p=input("Parool: ")
 if n in nimi:
  i=nimi.index(n)
  if salas[i]==p:
   sees=True
   user=n
   print("Logitud")
  else:
   print("Vale parool")
 else:
  print("Kasutaja puudub")

def parool():
 if not sees:
  print("Logi sisse")
  return
 p=input("Uus parool: ")
 if kontroll(p):
  i=nimi.index(user)
  salas[i]=p
  print("Parool muudetud")
  saada_email("Parool muudetud", f"Sinu uus parool: {salas[i]}", user)
 else:
  print("Parool on nõrk")

def taasta():
 n=input("Nimi: ")
 if n in nimi:
  p=""
  while not kontroll(p):
   s1=".,:;!_*-+()/#¤%&"
   s2="0123456789"
   s3="qwertyuiopasdfghjklzxcvbnm"
   s4=s3.upper()
   s5=s1+s2+s3+s4
   ls=list(s5)
   random.shuffle(ls)
   p=''.join([random.choice(ls)for x in range(12)])
  print("Uus parool on",p)
  i=nimi.index(n)
  salas[i]=p
  saada_email("Parool taastatud", f"Sinu uus parool: {salas[i]}", n)
 else:
  print("Kasutaja puudub")

def logout():
 global sees,user
 if sees:
  sees=False
  user=""
  print("Välja logitud")
 else:
  print("Pole sisse logitud")
