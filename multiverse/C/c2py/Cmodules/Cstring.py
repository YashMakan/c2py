def strlen(text):
	return len(text)

def strnlen(text,max_v):
	if len(text) > max_v:
		return max_v
	else:
		return len(text)

def strcmp(s1,s2):
	if s1==s2:
		return 0
	elif s1.find(s2) == 0:
		return -1

	elif s2.find(s1) == 0:
		return 1

	else:
		return -100

def strncmp(s1,s2,n):
	s1=s1[:n]
	s2=s2[:n]
	if s1==s2:
		return 0
	elif s1.find(s2) == 0:
		return -1

	elif s2.find(s1) == 0:
		return 1

	else:
		return -100

def strcmpi(s1,s2):
	s1=s1.lower()
	s2=s2.lower()
	if s1==s2:
		return 0
	elif s1.find(s2) == 0:
		return -1

	elif s2.find(s1) == 0:
		return 1

	else:
		return -100
		
def strcat(s1,s2):
	return s1+s2

def strncat(s1,s2,n):
	return s1+s2[:n]

def strcpy(s1,s2):
	return s2

def strncpy(s1,s2,n):
	return s2[:n]

def strchr(s1,s2):
	return s1[s1.find(s2):]

def strrchr(s1,s2):
	return s1[s1.rfind(s2):]

def strstr(s1,s2):
	return s1[s1.find(s2):]

def strrstr(s1,s2):
	return s1[s1.rfind(s2):]

def strdup(s1):
	return s1

def strndup(s1,n):
	return s1[:n]

def strlwr(s1):
	return s1.lower()

def strupr(s1):
	return s1.upper()

def strrev(s1):
	return s1[::-1]

def strset(s1,s2):
	return s2*len(s1)

def strtok(s1,s2):
	d=s2[0]
	ls=[]
	for char in s1:
		if char in s2:
			ls.append(d)
		else:
			ls.append(char)

	print(''.join(char for char in ls).split(sep=d))
