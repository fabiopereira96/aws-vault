import os
from datetime import datetime

command = 
current_hour = None

while 1:
    if(datetime.now().hour != current_hour):
       	p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
       	print(p)
       	current_hour = datetime.now().hour