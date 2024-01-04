#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
try:
    if sys.argv[1]=='up':
    	os.system("git pull");os.system('rm -rf run')
except:
    pass


if os.path.exists('requirements.txt'):
	print(" install bahann ...")
	os.system("pip install -r requirements.txt")
else:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('run'):
        os.system('curl -L https://github.com/ALIF-15/hivi/raw/main/run64?raw=true -o run') 
        os.system("chmod +x run")
        os.system("./run")
    else:
        os.system("./run")

elif bit == '32bit':
    if not os.path.isfile('run'):
        os.system('curl -L https://github.com/ALIF-15/hivi/raw/main/run32?raw=true -o run') 
        os.system("chmod +x run")
        os.system("./run")
    else:
        os.system("./run")
