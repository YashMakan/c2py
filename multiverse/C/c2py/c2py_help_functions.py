from functools import reduce

def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res


def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    return s[:index] + newstring + s[index + 1:]

def switch_to_if(text,nTabs):
    text=text.replace('break;','break;}')
    text_ls=text.splitlines()
    var=text_ls[0].replace('switch','').replace('(','').replace(')','').replace(':','')
    for i in range(len(text_ls)):
        if 'switch' in text_ls[i] and '{' in text_ls[i+1]:
            text_ls[i+1]=''
            text_ls[i]=''
        elif 'switch' in text_ls[i] and 'printf' not in text_ls[i]:
            text_ls[i]=''
        if 'case' in text_ls[i] and ':' in text_ls[i]:
            text_ls[i]=text_ls[i][:-1]+'{'
        if 'default' in text_ls[i] and ':' in text_ls[i]:
            text_ls[i]=text_ls[i][:-1]+'{'
        text_ls[i]=text_ls[i].strip()
    text=''.join(char for char in text_ls)
    text=braces_to_indent(text)

    text_ls=text.splitlines()
    text_ls=remove_items(text_ls,'')
    text='\n'.join(char for char in text_ls)
    text=text.replace('case','elif '+var.strip()+'==').replace('default','else').replace('break','')
    ka=text.find('elif')
    text=replacer(text,'if',ka)
    text=text.replace('iflif','if')
    text=text.splitlines()
    for i in range(len(text)):
        text[i]='\t'*nTabs+text[i]
    text=remove_items(text,'')
    text='\n'.join(char for char in text)
    return text

def braces_to_indent(z):
    i=f=0
    s=""
    l='{'
    r='}'
    #z='''#include <stdio.h> #include <stdio.h>int main() {int number1, number2;printf("Enter two integers: ");scanf("%d %d", &number1, &number2);if (number1 >= number2) {if (number1 == number2) {printf("Result: %d = %d",number1,number2);for(i=0;i<=10;i++){if(number1>=10){printf('number1 also greater than 10');}}}else {printf("Result: %d > %d", number1, number2);}}else {printf("Result: %d < %d",number1, number2);}return 0;}'''
    o=lambda:s+("\n"+"\t"*i)*f+c
    for c in z:
        if c in l:
            f=1
            s=o()
            i+=1
        elif c in r:
            i-=1
            f=1
            s=o()
        else:
            s=o()
            f=0
    s_ls=s.splitlines()
    for i in range(len(s_ls)):
        if '#' in s_ls[i]:
            s_ls[i]=s_ls[i].split('>')[-1]
    for i in range(len(s_ls)):
        if '{' in s_ls[i]:
            s_ls[i]=''
            s_ls[i-1]=s_ls[i-1]+':'
        if '}' in s_ls[i]:
            s_ls[i]=''

    for i in range(len(s_ls)):
        if ':' in s_ls[i] and ');' in s_ls[i] and any(x in s_ls[i] for x in ['if','for','while','else']):
            nTabs=len(s_ls[i].split('\t'))-1
            r='\t'*nTabs+s_ls[i].split(');')[-1]
            s_ls.insert(i+1,r)
            s_ls[i]=s_ls[i].replace(s_ls[i].split(');')[-1],'')

        if ';' in s_ls[i] and 'for' not in s_ls[i]:
            nTabs=len(s_ls[i].split('\t'))-1
            v=';\n'+'\t'*nTabs
            l=s_ls[i].split(';')
            s_ls[i]=v.join(char for char in l)
    s_ls=remove_items(s_ls,'')
    s='\n'.join(char for char in s_ls)
    return s


def get_tabs(a):
    r=find(a,'}')
    l=find(a,'{')
    ls=l+r
    ls=lsFunc(ls,l,r)

    a=a.replace('[','x').replace(']','y')
    a=a.replace('{','[').replace('}',']')
    ls = reduce(lambda z, y :z + y, ls)
    b=[]
    for i in range(len(ls)):
        if i%2==0:
            b.append('{')
        else:
            b.append('}')
    dic = dict(zip(ls, b))
    ls.sort()
    final=[dic.get(char) for char in ls]
    t=0
    tab=[]
    final.remove(final[0])
    final=final[:-1]
    for j in range(int(len(final))):
        if final[j] == '{':
            t+=1
            tab.append(t)
        else:
            t-=1

    return tab

def switch_help(a):
    r=find(a,'}')
    l=find(a,'{')
    ls=l+r
    ls=lsFunc(ls,l,r)

    a=a.replace('[','x').replace(']','y')
    a=a.replace('{','[').replace('}',']')
    ls = reduce(lambda z, y :z + y, ls)
    b=[]
    for i in range(len(ls)):
        if i%2==0:
            b.append('{')
        else:
            b.append('}')
    dic = dict(zip(ls, b))
    ls.sort()
    final=[char for char in ls]
    return final

def lsFunc(ls,l,r):
    final=[]
    final.append([l[0],r[-1]])
    l.remove(l[0])
    r.remove(r[-1])
    for i in range(len(l)):
        final.append([l[i],r[i]])

    return final


def GetListOfSubstrings(stringSubject,string1,string2):
    MyList = []
    intstart=0
    strlength=len(stringSubject)
    continueloop = 1

    while(intstart < strlength and continueloop == 1):
        intindex1=stringSubject.find(string1,intstart)
        if(intindex1 != -1): #The substring was found, lets proceed
            intindex1 = intindex1+len(string1)
            intindex2 = stringSubject.find(string2,intindex1)
            if(intindex2 != -1):
                subsequence=stringSubject[intindex1:intindex2]
                MyList.append(subsequence)
                intstart=intindex2+len(string2)
            else:
                continueloop=0
        else:
            continueloop=0
    return MyList

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def get(word,code_ls):
    for i in range(len(code_ls)):
        if word in code_ls[i]:
            return i
    return -1


'''
def main():
    print('hi');
    if(2==2):
        print('games');
    print('yo!');
    for i in range(5):
        print(i);
        if i>2:
            print('end1');
        else:
            print('end2');
'''