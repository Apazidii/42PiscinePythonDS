#!/bin/python3
import os


env = os.environ.get("VIRTUAL_ENV")
if env is not None:
	print(f'Your current virtual env is {os.environ.get("VIRTUAL_ENV")}')
else:
    print('Please set the righ environment')
