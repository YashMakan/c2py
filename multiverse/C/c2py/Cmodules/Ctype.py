import string
def isalpha(text):
	if text.isalpha() == True:
		return 1
	else:
		return 0
def isdigit(text):
	if text.isdigit() == True:
		return 1
	else:
		return 0
def isalnum(text):
	if text.isalnum() == True:
		return 1
	else:
		return 0
def isspace(text):
	if text.isspace() == True:
		return 1
	else:
		return 0
def islower(text):
	if text.islower() == True:
		return 1
	else:
		return 0
def isupper(text):
	if text.isupper() == True:
		return 1
	else:
		return 0
def isxdigit(text):
	hexs='0123456789abcdefABCDEF'
	t=[char for char in text]
	final=[]
	for val in t:
		if val in hexs:
			final='yes'
		else:
			final='no'
			break
	if final=='yes':
		return 1
	else:
		return 0
def iscntrl(text):
	if text.isprintable() == False:
		return 1
	else:
		return 0
def isprint(text):
	if text.isprintable() == True:
		return 1
	else:
		return 0
def ispunct(text):
	puncs=string.punctuation
	t=[char for char in text]
	final=[]
	for val in t:
		if val in puncs:
			final='yes'
		else:
			final='no'
			break
	if final=='yes':
		return 1
	else:
		return 0
def isgraph(text):
	graphs='''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''
	t=[char for char in text]
	final=[]
	for val in t:
		if val in graphs:
			final='yes'
		else:
			final='no'
			break
	if final=='yes':
		return 1
	else:
		return 0
def tolower(text):
	if text.tolower() == True:
		return 1
	else:
		return 0
def toupper(text):
	if text.toupper() == True:
		return 1
	else:
		return 0