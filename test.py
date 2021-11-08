# Schedule Library imported
import schedule
import time
from datetime import datetime

if datetime.now().hour > 8 and (datetime.now().hour % 2)-1:
    print('s')
    print(datetime.now().hour % 2)