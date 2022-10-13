import os
import sys

try:
	if os.environ['VIRTUAL_ENV'].split('/')[-1] == 'dgalactu':
		os.system('pip3 install bs4 PyTest')
		os.system('pip freeze')
		os.system('pip freeze > requirements.txt')
except KeyError:
    print('Please set the right environment')
    sys.exit(1) 
