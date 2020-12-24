from time import sleep as _sleep
import datetime as _datetime
import platform as _platform
from winsound import Beep as _Beep
import cytypes as _ctypes
import sys as _sys

def _is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def delay(n):
	n=n/1000
	_sleep(n)
	return None

def sleep(n):
	_sleep(n)
	return None

def sound(freq):
	if _platform.system() == "Windows":
		_Beep(freq,1000)
		return None
	else:
		raise Exception("sound() not available for your os")

class date:
	def __init__(self):
		self.da_day=None
		self.da_mon=None
		self.da_year=None
	def getdate(self):
		dt = _datetime.datetime.today()
		self.da_day=dt.day
		self.da_mon=dt.month
		self.da_year=dt.year
	def setdate(self):
		dt=_datetime.datetime.now()
		time_tuple = (self.da_year,self.da_mon,self.da_day,dt.hour,dt.minute,dt.second,0) # Year, Month, Day, Hour, Min, sec, millisec
		if is_admin():
        	dayOfWeek = datetime(*time_tuple).isocalendar()[2]
        	t = time_tuple[:2] + (dayOfWeek,) + time_tuple[2:]
        	win32api.SetSystemTime(*t)
    	else:
        	# Re-run the program with admin rights
        	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        	raise Exception('Permission denied to change the date time')


class time:
	def __init__(self):
		self.ti_hour=None
		self.ti_min=None
		self.ti_sec=None
	def gettime(self):
		dt=_datetime.datetime.now()
		self.ti_hour=dt.hour
		self.ti_min=dt.minute
		self.ti_sec=dt.second