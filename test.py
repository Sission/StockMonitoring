# Schedule Library imported
import schedule
import time
from datetime import datetime

if datetime.now().hour > 8 and ((datetime.now().hour + 1) % 2):
    print(1)
