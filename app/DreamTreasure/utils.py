from datetime import *
import pytz

def getCurrentTime():
  tz = pytz.timezone('Asia/Calcutta')
  return datetime.now(tz)