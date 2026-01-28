# import these modules if you need them:
from datetime import datetime, timezone
import math
      
def time_until_take_off(from_time: str, take_off_time: str) -> int:
  def clean(date):
    return date.replace("@"," ").replace("|",":").replace(" NP","")
  dateTimeStampFromTime = datetime.strptime(clean(from_time), "%Y*%m*%d %H:%M:%S")
  dateTimeStampTakeOff = datetime.strptime(clean(take_off_time), "%Y*%m*%d %H:%M:%S")
  secondsForTakeOff = (dateTimeStampTakeOff - dateTimeStampFromTime).total_seconds()
  return math.floor(secondsForTakeOff)

takeoff = '2025*12*25@00|00|00 NP'
time_until_take_off('2025*12*24@23|59|30 NP', takeoff)