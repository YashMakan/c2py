from multiverse.C.c2py.c2py_help_functions import *

def dec1(from_name,to_name):
    return baap(True,[from_name,to_name])

def dec2(old):
    return baap(False,[old])


def baap(file,text):
    if file == True:
        from_name=text[0]
        to_name=text[1]
        with open(from_name,'r') as f:
            old=f.read()
    else:
        old=text[0]
    float_list=['f','l','L','e','E','g','G','.']
    int_list=['i','d','h','u']
    str_list=['s']
    var_list=['int ','char ','float ','double ','long ','bool ']
    imports=[]
    consClassBool=False
    consClass=''
    const_ls=[]
    final_ls=[]
    new_ls=[]
    classes=[]
    defines=[]

    code=old
    code = code.replace(r'\n', '')
    code=code.replace('auto ','').replace(' unsigned ','').replace('unsigned ','').replace('register ','').replace('extern ','').replace('static ','').replace(' volatile ','').replace('volatile ','').replace(' signed ','').replace('signed ','').replace(' short ','').replace('short ','').replace('%lf','%l').replace('union ','struct ').replace('->','.')
    code=code.splitlines()
    tq=[]
    hashes=[]
    enums=[]

    for i in range(len(code)):
        if '#define' not in code[i] and '#' in code[i]:
            hashes.append(code[i])

        if '#define' in code[i].replace(' ',''):
            la=code[i].replace('#define ','').split()
            defines.append('='.join(char for char in la))
            code[i]=''

        if '//' in code[i]:
            code[i]=code[i]+';'
        if "*/" in code[i]:
            code[i]=code[i]+';'
        if "case" in code[i] and ':' in code[i]:
            code[i]=code[i].replace(':','')+'{'
            lsaz='\n'.join(char for char in code[i:])
            bw_dw=lsaz[:lsaz.find('break')]
            jhas=len(bw_dw.splitlines())-1
            bw_w=lsaz[lsaz.find('break'):].split('\n')[0]
            code[i+jhas]=''
            bw_w=bw_w+'}'
            code[i+jhas]=bw_w

        if "default" in code[i] and ':' in code[i]:
            code[i]=code[i].replace(':','')+'{'
            lsaz='\n'.join(char for char in code[i:])
            bw_dw=lsaz[:lsaz.find('break')]
            jhas=len(bw_dw.splitlines())-1
            bw_w=lsaz[lsaz.find('break'):].split('\n')[0]
            code[i+jhas]=''
            bw_w=bw_w+'}'
            code[i+jhas]=bw_w

        if 'if(' in code[i].replace(' ','') and '{' not in code[i] and '{' not in code[i+1] and '//' not in code[i] :
            code[i]=code[i]+'{'
            code[i+1]=code[i+1]+'}'
        if 'else'== code[i].replace(' ','').strip() and '//' not in code[i] :
            code[i]=code[i]+'{'
            code[i+1]=code[i+1]+'}'
        code[i]=code[i].strip()
        tq.append(code[i])
        
    code=[char for char in tq]
    code=''.join(char for char in code)
    code=braces_to_indent(code)
    code=code.replace('puts','printf')
    code=code.splitlines()
    for i in range(len(code)):
        if code[i].count(';') == 1 and 'elseif(' in code[i].replace(' ',''):
            nTabs=len(code[i].split('\t'))-1
            newsa='\t'*nTabs+';'.join(char for char in code[i].split(';')[1:]).strip()
            code[i]='\t'*nTabs+code[i].split(';')[0].strip()+';'
            code.insert(i+1,newsa)
            i+=1

        if code[i].count(';') > 2 and 'for(' in code[i].replace(' ',''):
            nTabs=len(code[i].split('\t'))-1
            newsa='\t'*nTabs+';'.join(char for char in code[i].split(';')[1:]).strip()
            code[i]='\t'*nTabs+code[i].split(';')[0].strip()+';'
            code.insert(i+1,newsa)
            i+=1

        if code[i].count(';') == 1 and 'if(' in code[i].replace(' ',''):
            nTabs=len(code[i].split('\t'))-1
            newsa='\t'*nTabs+';'.join(char for char in code[i].split(';')[1:]).strip()
            code[i]='\t'*nTabs+code[i].split(';')[0].strip()+';'
            code.insert(i+1,newsa)
            i+=1

    for i in range(len(code)):
        nTabs=len(code[i].split('\t'))-1
        if nTabs == 0 and 'int ' in code[i] and ':' in code[i]:
            tls=code[i].split()
            tls[0]='def'
            code[i]=' '.join(char for char in tls)
            code[i]=code[i].replace('int ','')
            code[i]='\n# Initializing Function named {}()\n'.format(code[i].split('def')[1].split('(')[0].strip()) +code[i]
        elif nTabs == 0 and 'int ' in code[i] and ':' not in code[i]:
            code[i]=''
        elif nTabs == 0 and 'void ' in code[i] and ':' in code[i]:
            tls=code[i].split()
            tls[0]='def'
            code[i]=' '.join(char for char in tls)
            code[i]=code[i].replace('void ','')
            code[i]='# Initializing Function named {}()\n'.format(code[i].split('def')[1].split('(')[0].strip()) +code[i]
        elif nTabs == 0 and 'void' in code[i] and ':' not in code[i]:
            code[i]=''
    for i in range(len(code)):
        if code[i].strip()=='':
            code[i]=''
        #if 'for ' not in code[i] and 'for(' not in code[i]:
         #   code[i]=code[i].replace(';','')
    
    code=remove_items(code,'')
    code='\n'.join(char for char in code)
    code_ls=code.splitlines()
    if '' in code_ls:
        code_ls=remove_items(code_ls,'')
    k=get('return',code_ls)
    if k != -1:
        code_ls.remove(code_ls[k])
    code='\n'.join(char for char in code_ls)
    code=code.replace('printf','print')
    code=code.replace('scanf','input')
    code_ls=code.splitlines()


    for i in range(len(code_ls)):
        if "switch" in code_ls[i] and ':' in code_ls[i]:
            nTabs=code_ls[i].count('\t')
            lsaz='\n'.join(char for char in code_ls[i:])
            bw_w=lsaz[:lsaz.rfind('<SWITCH_END>')].split('\n')
            final='\n'.join(char for char in bw_w)
            new=switch_to_if(final,nTabs)
            new_ls.append(new)
            final_ls.append(final)

    code='\n'.join(char for char in code_ls)
    for i in range(len(new_ls)):
        code=code.replace(final_ls[i],new_ls[i])
    code_ls=code.splitlines()

    c={}
    I={}
    f={}
    b={}
    for j in range(len(code_ls)):
        if 'char ' in code_ls[j]:
            var=code_ls[j].split('char ')[1]
            if ',' in var:
                vl=var.split(',')
                for k in range(len(vl)):
                    if '=' in vl[k]:
                        c[vl[k].split('=')[0].split('[')[0].strip()]=vl[k].split('=')[1].replace("'","").replace('"',"").strip()
                    else:
                        c[vl[k].split('[')[0]]=None
            else:
                if '=' in var:
                    c[var.split('=')[0].split('[')[0].strip()]=var.split('=')[1].replace("'","").replace('"',"").strip()
                else:
                    c[var.split('[')[0].strip()]=None
        elif 'int ' in code_ls[j]:
            var=code_ls[j].split('int ')[1]
            if ',' in var:
                vl=var.split(',')
                for k in range(len(vl)):
                    if '=' in vl[k]:
                        I[vl[k].split('=')[0].split('[')[0].strip()]=vl[k].split('=')[1].replace("'","").replace('"',"").strip()
                    else:
                        I[vl[k].split('[')[0].strip()]=None
            else:
                if '=' in var:
                    I[var.split('=')[0].split('[')[0].strip()]=var.split('=')[1].replace("'","").replace('"',"").strip()
                else:
                    I[var.split('[')[0].strip()]=None

        elif 'float ' in code_ls[j] or 'double ' in code_ls[j] or 'long ' in code_ls[j]:
            code_ls[j]=code_ls[j].replace('double','float')
            code_ls[j]=code_ls[j].replace('long','float')
            var=code_ls[j].split('float ')[1]
            if ',' in var:
                vl=var.split(',')
                for k in range(len(vl)):
                    if '=' in vl[k]:
                        f[vl[k].split('=')[0].split('[')[0].strip()]=vl[k].split('=')[1].replace("'","").replace('"',"").strip()
                    else:
                        f[vl[k].split('[')[0].strip()]=None
            else:
                if '=' in var:
                    f[var.split('=')[0].split('[')[0].strip()]=var.split('=')[1].replace("'","").replace('"',"").strip()
                else:
                    f[var.split('[')[0].strip()]=None

        elif 'bool ' in code_ls[j]:
            var=code_ls[j].split('bool ')[1]
            if ',' in var:
                vl=var.split(',')
                for k in range(len(vl)):
                    if '=' in vl[k]:
                        b[vl[k].split('=')[0].split('[')[0].strip()]=vl[k].split('=')[1].replace("'","").replace('"',"").strip()
                    else:
                        b[vl[k].split('[')[0].strip()]=None
            else:
                if '=' in var:
                    b[var.split('=')[0].split('[')[0].strip()]=var.split('=')[1].replace("'","").replace('"',"").strip()
                else:
                    b[var.split('[')[0].strip()]=None
        

    # for k in code_ls[:]:
    #     if 'char ' in k or 'int ' in k or 'double ' in k or 'float ' in k or 'bool ' in k or 'clrscr' in k or 'getch' in k or 'long' in k:
    #         code_ls.remove(k)
    c_ls=list(c.keys())
    # tx=[]
    # for l in range(len(c_ls)):
    #     tx.append(c_ls[l]+'='+str(c[c_ls[l]]))
    # ctx='\n'.join(char.strip() for char in tx)+'\n'
    # code='\n'.join(char for char in code_ls)
    # code=ctx+'\n'+code
    # code_ls=code.splitlines()
    i_ls=list(I.keys())
    i_ls=[char.strip() for char in i_ls]
    # tx=[]
    # for l in range(len(i_ls)):
    #     tx.append(i_ls[l]+'='+str(I[i_ls[l]]))
    # ctx='\n'.join(char.strip() for char in tx)+'\n'
    # code='\n'.join(char for char in code_ls)
    # code=ctx+'\n'+code
    
    # code_ls=code.splitlines()
    f_ls=list(f.keys())
    f_ls=[char.strip() for char in f_ls]
    # tx=[]
    # for l in range(len(f_ls)):
    #     tx.append(f_ls[l]+'='+str(f[f_ls[l]]))
    # ctx='\n'.join(char.strip() for char in tx)+'\n'
    # code='\n'.join(char for char in code_ls)
    # code=ctx+'\n'+code
    # print(ctx)
    # code_ls=code.splitlines()
    b_ls=list(b.keys())
    b_ls=[char.strip() for char in b_ls]
    # tx=[]
    # for l in range(len(b_ls)):
    #     tx.append(b_ls[l]+'='+str(b[b_ls[l]]))
    # ctx='\n'.join(char.strip() for char in tx)+'\n'
    # code='\n'.join(char for char in code_ls)
    # code=ctx+'\n'+code
    #code_ls=code.splitlines()
    for i in range(len(code_ls)):
        if code_ls[i].strip().startswith("/*"):
            nTabs=len(code_ls[i].split('\t'))-1
            code_ls[i]='\t'*nTabs+code_ls[i].strip()

        if '&' in code_ls[i] and 'if' not in code_ls[i]:
            code_ls[i]=code_ls[i].replace('&','')

        if '*' in code_ls[i] and '/*' not in code_ls[i]:
            code_ls[i]=code_ls[i].replace('*','')
        if 'print' in code_ls[i]:
            if '",' in code_ls[i].strip():
                prefix=code_ls[i].find('%')+1
                prefix=code_ls[i][prefix]
                var_used=code_ls[i].split('",')[1].split(')')[0]
                code_ls[i]=code_ls[i].split('",')[0]+'".format('+var_used.strip()+'))'

            elif "'," in code_ls[i].strip():
                prefix=code_ls[i].find('%')+1
                prefix=code_ls[i][prefix]
                var_used=code_ls[i].split("',")[1].split(')')[0]
                code_ls[i]=code_ls[i].split("',")[0]+'".format('+var_used.strip()+'))'

            code_ls[i]=code_ls[i].replace('%s','{}').replace('%d','{}').replace('%f','{}').replace('%c','{}').replace('%lld','{}').replace('%e','{}').replace('%E','{}').replace('%g','{}').replace('%G','{}').replace('%hi','{}').replace('%hu','{}').replace('%i','{}').replace('%l','{}').replace('%ld','{}').replace('%li','{}').replace('%lf','{}').replace('%Lf','{}').replace('%lu','{}').replace('%lli','{}').replace('%lld','{}').replace('%llu','{}').replace('%o','{}').replace('%p','{}').replace('%u','{}').replace('%x','{}').replace('%X','{}')
            if '%.' in code_ls[i]:
                nqa='%.'+code_ls[i].split('%.')[1].split('f')[0]+'f'
                code_ls[i]=code_ls[i].replace(nqa,'{}')
        if 'input' in code_ls[i]:
            if '",' in code_ls[i].strip():
                nTabs=len(code_ls[i].split('\t'))-1
                prefix=code_ls[i].find('%')+1
                prefix=code_ls[i][prefix]
                new=code_ls[i].replace(' ','').split('("')[1].split('",')[0]
                mul=False
                if ',' in code_ls[i].split('",')[1].split(')')[0]:
                    code_ls[i]=code_ls[i]+'.split()'
                    prefixes=code_ls[i].split('("')[1].split('"')[0].split()
                    prefixes=[char.replace('%','') for char in prefixes]
                    prefix=max(prefixes)
                    mul=True
                code_ls[i]=code_ls[i].replace(new,'').strip()
                if mul:
                    if any(x in prefix for x in int_list):
                        var_used=code_ls[i].split('",')[1].split(')')[0].strip().replace('&','')
                        code_ls[i]='\t'*nTabs+var_used+'='+'map(int,'+code_ls[i]+')'
                    elif any(x in prefix for x in str_list):
                        var_used=code_ls[i].split('",')[1].split(')')[0].strip().replace('&','')
                        code_ls[i]='\t'*nTabs+var_used+'='+'map(str,'+code_ls[i]+')'
                    elif prefix == 'c':
                        var_used=code_ls[i].split('",')[1].split(')')[0].strip().replace('&','')
                        code_ls[i]='\t'*nTabs+var_used+'='+'map(str,'+code_ls[i]+')'
                    elif any(x in prefix for x in float_list):
                        var_used=code_ls[i].split('",')[1].split(')')[0].strip().replace('&','')
                        code_ls[i]='\t'*nTabs+var_used+'='+'map(float,'+code_ls[i]+')'

                elif any(x in prefix for x in int_list):
                    var_used=code_ls[i].split('",')[1].split(')')[0].strip().replace('&','')
                    code_ls[i]='\t'*nTabs+var_used+'='+'int('+code_ls[i]+')'
                elif any(x in prefix for x in str_list):
                    var_used=code_ls[i].split('",')[1].split(')')[0].strip().replace('&','')
                    code_ls[i]='\t'*nTabs+var_used+'='+'str('+code_ls[i]+')'
                elif prefix == 'c':
                    var_used=code_ls[i].split('",')[1].split(')')[0].strip().replace('&','')
                    code_ls[i]='\t'*nTabs+var_used+'='+'str('+code_ls[i]+')[0]'
                elif any(x in prefix for x in float_list):
                    var_used=code_ls[i].split('",')[1].split(')')[0].strip().replace('&','')
                    code_ls[i]='\t'*nTabs+var_used+'='+'float('+code_ls[i]+')'
                yt=code_ls[i].split('input(')[1].split(')')[0]
                code_ls[i]=code_ls[i].replace(yt,'')

            elif "'," in code_ls[i].strip():
                '''scanf("%d %d", &number1, &number2);'''
                nTabs=len(code_ls[i].split('\t'))-1
                prefix=code_ls[i].find('%')+1
                prefix=code_ls[i][prefix]
                new=code_ls[i].replace(' ','').split('("')[1].split("',")[0]
                mul=False
                if ',' in code_ls[i].split("',")[1].split(')')[0]:
                    code_ls[i]=code_ls[i]+'.split()'
                    prefixes=code_ls[i].split('("')[1].split('"')[0].split()
                    prefixes=[char.replace('%','') for char in prefixes]
                    prefix=max(prefixes)
                    mul=True
                code_ls[i]=code_ls[i].replace(new,'').strip()
                if mul:
                    if any(x in prefix for x in int_list):
                        var_used=code_ls[i].split("',")[1].split(')')[0].strip().replace('&','')
                        code_ls[i]='\t'*nTabs+var_used+'='+'map(int,'+code_ls[i]+')'
                    elif any(x in prefix for x in str_list):
                        var_used=code_ls[i].split("',")[1].split(')')[0].strip().replace('&','')
                        code_ls[i]='\t'*nTabs+var_used+'='+'map(str,'+code_ls[i]+')'
                    elif prefix == 'c':
                        var_used=code_ls[i].split("',")[1].split(')')[0].strip().replace('&','')
                        code_ls[i]='\t'*nTabs+var_used+'='+'map(str,'+code_ls[i]+')'
                    elif any(x in prefix for x in float_list):
                        var_used=code_ls[i].split("',")[1].split(')')[0].strip().replace('&','')
                        code_ls[i]='\t'*nTabs+var_used+'='+'map(float,'+code_ls[i]+')'

                elif any(x in prefix for x in int_list):
                    var_used=code_ls[i].split("',")[1].split(')')[0].strip().replace('&','')
                    code_ls[i]='\t'*nTabs+var_used+'='+'int('+code_ls[i]+')'
                elif any(x in prefix for x in str_list):
                    var_used=code_ls[i].split("',")[1].split(')')[0].strip().replace('&','')
                    code_ls[i]='\t'*nTabs+var_used+'='+'str('+code_ls[i]+')'
                elif prefix == 'c':
                    var_used=code_ls[i].split("',")[1].split(')')[0].strip().replace('&','')
                    code_ls[i]='\t'*nTabs+var_used+'='+'str('+code_ls[i]+')[0]'
                elif any(x in prefix for x in float_list):
                    var_used=code_ls[i].split('",')[1].split(')')[0].strip().replace('&','')
                    code_ls[i]='\t'*nTabs+var_used+'='+'float('+code_ls[i]+')'
                yt=code_ls[i].split('input(')[1].split(')')[0]
                code_ls[i]=code_ls[i].replace(yt,'')

        if 'else:' in code_ls[i].replace(' ','') and '//' not in code_ls[i]:
            code_ls[i]=code_ls[i].replace(' ','')
        if 'if(' in code_ls[i].replace(' ','') and '//' not in code_ls[i]:
            code_ls[i]=code_ls[i].replace('||',' or ').replace('&&',' and ')
        if('for ' in code_ls[i] or 'for(' in code_ls[i]) and '//' not in code_ls[i] :
            code_ls[i]=code_ls[i].replace(' ','')
            nTabs=len(code_ls[i].split('\t'))-1
            code_ls[i]=code_ls[i].replace('int','').replace(" ","")
            spl=code_ls[i].split('(')[1].split(')')[0].split(';')
            s=spl[0].split('=')[0]
            s_val=spl[0].split('=')[1]
            if s not in i_ls:
                I[str(s)]=str(s_val)
                i_ls.append(s)
            if '<' in code_ls[i]:
                l=spl[1].replace('=','').split('<')[1]
            elif '>' in code_ls[i]:
                l=spl[1].replace('=','').split('>')[1]
            else:
                l=spl[1].replace(s,'').replace('=','').replace('+','')
            inc=spl[2]
            if '++' in inc:
                inc=1
            elif '+=' in inc:
                inc=int(inc.replace(s,'').replace('+=',''))
            elif '--' in inc:
                inc=int(-1)
            elif '-=' in inc:
                inc=int('-'+inc.replace(s,'').replace('-=',''))
            elif '--' in inc:
                inc=-1
            else:
                if '+' in inc:
                    inc=int(inc.replace(s,'').replace('+','').replace('=',''))
                else:
                    inc=int('-'+inc.replace(s,'').replace('+','').replace('=',''))
            code_ls[i]='\t'*nTabs+'for {0} in range({1},{2},{3}):'.format(s,s_val,l,inc)
        if '//' in code_ls[i]:
            nTabs=len(code_ls[i].split('\t'))-1
            code_ls[i]=code_ls[i].replace('//','#')
        if '++' in code_ls[i] and 'for(' not in code_ls[i]:
            code_ls[i]=code_ls[i].replace('++','')
            code_ls[i]=code_ls[i]+'+=1'
        
        if any(x in code_ls[i] for x in var_list) and ';' in code_ls[i] and 'input' not in code_ls[i] and 'print' not in code_ls[i]:
            nTabs=code_ls[i].count('\t')
            code_ls[i]=code_ls[i].replace('int ','').replace('char ','').replace('float ','').replace('double ','').replace('long ','').replace('bool ','')
            semi=code_ls[i].count(',')
            if semi==0:
                if '=' not in code_ls[i]:
                    code_ls[i]='\t'*nTabs+code_ls[i].strip().split('[')[0].replace(';','')+' = None'
                else:
                    try:
                        code_ls[i]='\t'*nTabs+code_ls[i].strip().replace(';','').split('[')[0]+code_ls[i].strip().replace(';','').split(']')[1].strip()
                    except:
                        code_ls[i]='\t'*nTabs+code_ls[i].strip().replace(';','').split('[')[0].strip()
            else:
                semi_vals=code_ls[i].split(',')
                yi=[]
                for j in range(len(semi_vals)):
                    if '=' not in semi_vals[j]:
                        semi_vals[j]='\t'*nTabs+semi_vals[j].strip().replace(';','').split('[')[0]+' = None'
                        yi.append(semi_vals[j])
                if len(yi) == len(semi_vals):
                    code_ls[i]='\n'.join(char.replace(';','') for char in yi)
                else:
                    print(semi_vals)
                    code_ls[i]='\n'.join('\t'*nTabs+char.replace(';','').strip() for char in semi_vals)
            code_ls[i]=code_ls[i].replace('*','')

        if 'gets ' in code_ls[i]:
            nTabs=code_ls[i].count('\t')
            var=code_ls[i].split('(')[1].split(')')[0]
            code_ls[i]='\t'*nTabs+var.strip()+' = '+code_ls[i].strip().split('(')[0]+'('+code_ls[i].strip().split(')')[1]+')'
            code_ls[i]=code_ls[i].replace('gets','input')

        if 'const ' in code_ls[i]:
            code_ls[i]=code_ls[i].replace(' const ','').replace('const ','')
            consClassBool=True
            consClass=code_ls[i].strip().replace(';','')
            const_ls.append(code_ls[i].replace(';','').split('=')[0].strip())
            code_ls[i]=''
            imports.append('from multiverse import Multiverse')

        if 'do:' == code_ls[i].strip().replace(' ',''):
            nTabs=code_ls[i].count('\t')
            lsaz='\n'.join(char for char in code_ls[i:])
            bw_dw='\t'*nTabs+lsaz[:lsaz.find('while')].strip()
            jhas=len(bw_dw.splitlines())
            bw_w=lsaz[lsaz.find('while'):].split('\n')[0]
            bw_w='\t'*(nTabs+1)+'if(not '+bw_w.split('(')[1].split(')')[0].replace(' ','')+'):\n'+'\t'*(nTabs+2)+'break'
            code_ls[i+jhas]=bw_w
            code_ls[i]=code_ls[i].replace('do','while True')

        ################################################## <SYS> #######################################################################

        if 'sizeof(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('sizeof','sys.getsizeof')
            code_ls[i]=code_ls[i]+')'
            imports.append('import sys')
        ################################################## </SYS> #######################################################################

        ################################################## <MATH> #######################################################################


        if 'floor(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('floor','math.floor')
            imports.append('import math')

        if 'round(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('round','math.round')
            imports.append('import math')

        if 'ceil(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('ceil','math.ceil')
            imports.append('import math')

        if 'sin(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('sin','math.sin')
            imports.append('import math')

        if 'asin(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('asin','math.asin')
            imports.append('import math')

        if 'cos(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('cos','math.cos')
            imports.append('import math')

        if 'acos(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('acos','math.acos')
            imports.append('import math')

        if 'cosh(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('cosh','math.cosh')
            imports.append('import math')

        if 'exp(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('exp','math.exp')
            imports.append('import math')

        if 'tan(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('tan','math.tan')
            imports.append('import math')

        if 'tanh(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('tanh','math.tanh')
            imports.append('import math')

        if 'sinh(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('sinh','math.sinh')
            imports.append('import math')

        if 'log(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('log','math.log')
            imports.append('import math')

        if 'log10(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('log10','math.log10')
            imports.append('import math')

        if 'sqrt(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('sqrt','math.sqrt')
            imports.append('import math')

        if 'pow(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('pow','math.pow')
            imports.append('import math')

        if 'trunc(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('trunc','math.trunc')
            imports.append('import math')

        if 'fabs(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('fabs','math.fabs')
            imports.append('import math')

        if 'fmod(' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('fmod','math.fmod')
            imports.append('import math')

        if 'modf(' in code_ls[i]:
            #fractpart = modf(x, &intpart);
            nTabs=code_ls[i].count('\t')
            integral=code_ls[i].split(',')[1].split(')')[0].replace('&','').strip()
            fractpart=code_ls[i].split('=')[0].strip()
            code_ls[i]=code_ls[i].split(',')[0]+')'+code_ls[i].split(')')[1]
            code_ls[i]='\t'*nTabs+integral+','+fractpart+' = '+code_ls[i].split('=')[1]
            code_ls[i]=code_ls[i].replace('modf','math.modf')
            imports.append('import math')

        ################################################## </MATH> #######################################################################

        ################################################## <STRING> ######################################################################
        if  'strlen(' in code_ls[i]:
            pass

        if  'strnlen(' in code_ls[i]:
            pass

        if  'strcmp(' in code_ls[i]:
            pass

        if  'strncmp(' in code_ls[i]:
            pass

        if  'strncmpi(' in code_ls[i]:
            pass

        if  'strcat(' in code_ls[i]:
            nTabs=code_ls[i].count('\t')
            var=code_ls[i].split('strcat(')[1].split(',')[0].strip()
            code_ls[i]='\t'*nTabs+var+'='+code_ls[i].strip()

        if  'strncat(' in code_ls[i]:
            nTabs=code_ls[i].count('\t')
            var=code_ls[i].split('strncat(')[1].split(',')[0].strip()
            code_ls[i]='\t'*nTabs+var+'='+code_ls[i].strip()

        if  'strcpy(' in code_ls[i]:
            nTabs=code_ls[i].count('\t')
            var=code_ls[i].split('strcpy(')[1].split(',')[0].strip()
            code_ls[i]='\t'*nTabs+var+'='+code_ls[i].strip()

        if  'strncpy(' in code_ls[i]:
            nTabs=code_ls[i].count('\t')
            var=code_ls[i].split('strncpy(')[1].split(',')[0].strip()
            code_ls[i]='\t'*nTabs+var+'='+code_ls[i].strip()

        if  'strchr' in code_ls[i]:
            pass

        if  'strrchr' in code_ls[i]:
            pass

        if  'strstr' in code_ls[i]:
            pass

        if  'strrstr' in code_ls[i]:
            pass

        if  'strdup' in code_ls[i]:
            pass

        if  'strlwr' in code_ls[i]:
            pass

        if  'strupr' in code_ls[i]:
            pass

        if  'strrev' in code_ls[i]:
            pass

        if  'strset' in code_ls[i]:
            pass

        if 'strtok' in code_ls[i]:
            pass

        if 'getdate(' in code_ls[i]:
            nTabs=len(code_ls[i].split('\t'))-1
            var=code_ls[i].split('getdate(')[1].split(')')[0].strip()
            code_ls[i]=code_ls[i].replace(' ','')
            code_ls[i]=code_ls[i].replace('getdate('+var,var+'.getdate(')

        if 'setdate(' in code_ls[i]:
            nTabs=len(code_ls[i].split('\t'))-1
            var=code_ls[i].split('setdate(')[1].split(')')[0].strip()
            code_ls[i]=code_ls[i].replace(' ','')
            code_ls[i]=code_ls[i].replace('setdate('+var,var+'.setdate(')

        if 'gettime(' in code_ls[i]:
            nTabs=len(code_ls[i].split('\t'))-1
            var=code_ls[i].split('gettime(')[1].split(')')[0].strip()
            code_ls[i]=code_ls[i].replace(' ','')
            code_ls[i]=code_ls[i].replace('gettime('+var,var+'.gettime(')

        if 'enum ' in code_ls[i] and ':' in code_ls[i]:
            var=code_ls[i].split('enum ')[1].split(':')[0].strip().replace(' ','')
            enums.append(var)
            code_ls[i]='class '+var+'(Enum, start=0):'
            code_ls[i+1]=code_ls[i+1].replace(' ','').replace(',','\n\t')
            ka=code_ls[i+1].count('\n')
            imports.append('from aenum import Enum')

        if 'enum ' in code_ls[i] and ':' not in code_ls[i] and '#' not in code_ls[i]: # must be is en_NAME form <SWITCHEND> <STRUCTEND>
            lasqw=code_ls[i].split()[1:]
            c=code_ls[i].split()[1].replace(';','')
            var=lasqw[0].strip()
            bw_code=''.join(char for char in lasqw[1:])
            if '=' in bw_code:
                nTabs=len(code_ls[i].split('\t'))-1
                v=bw_code.split('=')[1].strip().replace(';','')
                c_name=bw_code.split('=')[0].strip().replace(';','')
                print(c,v,c_name)
                code_ls[i]='\t'*nTabs+c_name+'='+c+'.'+v+'.value'
            else:
                c_name=bw_code.split('=')[0].strip().replace(';','')
                code_ls[i]='\t'*nTabs+c_name+'='+c

        if 'e_' in code_ls[i] and '=' in code_ls[i] and not any(x in code_ls[i] for x in enums):
            nTabs=len(code_ls[i].split('\t'))-1
            var=code_ls[i].split('=')[0].strip()
            val=code_ls[i].split('=')[1].strip()
            code_ls[i]='\t'*nTabs+var+'='+var+'.'+val+'.value'

        ################################################## </STRING> #######################################################################


    if any('#include<ctype.h>' in x.replace(' ','') for x in hashes):
        imports.append('from multiverse.C.c2py.Cmodules.Ctype import *')

        
    if any('#include<string.h>' in x.replace(' ','') for x in hashes):
        imports.append('from multiverse.C.c2py.Cmodules.Cstring import *')

    if any('#include<dos.h>' in x.replace(' ','') for x in hashes):
        imports.append('from multiverse.C.c2py.Cmodules.Cdos import *')

    code_ls=remove_items(code_ls,'')
    for i in range(len(code_ls)):
        if 'for ' not in code_ls[i] and 'for(' not in code_ls[i]:
           code_ls[i]=code_ls[i].replace(';','')
        if '--' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('--','')
            code_ls[i]=code_ls[i]+'-=1'
        if '++' in code_ls[i]:
            code_ls[i]=code_ls[i].replace('++','')
            code_ls[i]=code_ls[i]+'+=1'

        if 'struct' in code_ls[i] and ':' in code_ls[i]:
            nTabs=len(code_ls[i].split('\t'))-1
            code_ls[i]=code_ls[i].replace('struct','class')
            classes.append(code_ls[i].replace('class','').replace(':','').strip())
            lsaz='\n'.join(char for char in code_ls[i:]).split('\n')[1:]
            lsaz='\n'.join(char for char in lsaz)
            bw_code=lsaz.split('<STRUCT_END>')[0]
            bw_code_ls=bw_code.split('\n')
            if '\t' in bw_code_ls:
                bw_code_ls.remove('\t')
            lines=len(bw_code_ls)
            bw_code_ls=['\t\tself.'+char.strip() for char in bw_code_ls]
            bw_code='\n'.join(char for char in bw_code_ls)
            code_ls[i+1]='\t'*(nTabs+1)+'def __init__(self):\n'+'\t'*(nTabs)+bw_code
            for j in range(1,lines+1):
                code_ls[i+1+j]=''

        if 'struct' in code_ls[i] and ':' not in code_ls[i]:
            nTabs=code_ls[i].count('\t')
            code_ls[i]=code_ls[i].replace('struct ','')
            className=code_ls[i].split(' ')[0].strip()
            code_ls[i]=' '.join(char for char in code_ls[i].split(' ')[1:])
            semi=code_ls[i].count(',')
            if semi==0:
                if '=' not in code_ls[i]:
                    code_ls[i]='\t'*nTabs+code_ls[i].strip().split('[')[0].replace(';','')+' = '+className+'()'
                else:
                    try:
                        code_ls[i]='\t'*nTabs+code_ls[i].strip().replace(';','').split('[')[0]+code_ls[i].strip().replace(';','').split(']')[1].strip()
                    except:
                        code_ls[i]='\t'*nTabs+code_ls[i].strip().replace(';','').split('[')[0].strip()
            else:
                semi_vals=code_ls[i].split(',')
                yi=[]
                for j in range(len(semi_vals)):
                    if '=' not in semi_vals[j]:
                        semi_vals[j]='\t'*nTabs+semi_vals[j].strip().replace(';','').split('[')[0]+' = '+className+'()'
                        yi.append(semi_vals[j])
                if len(yi) == len(semi_vals):
                    code_ls[i]='\n'.join(char.replace(';','') for char in yi)
                else:
                    print(semi_vals)
                    code_ls[i]='\n'.join('\t'*nTabs+char.replace(';','').strip() for char in semi_vals)
            code_ls[i]=code_ls[i].replace('*','')


        for j in range(len(const_ls)):
            if const_ls[j]+'=' in code_ls[i].replace(' ',''):
                code_ls[i]=code_ls[i].replace(const_ls[j]+'=','const.'+const_ls[j]+'=')
            elif const_ls[j]+',' in code_ls[i].replace(' ',''):
                code_ls[i]=code_ls[i].replace(const_ls[j]+',','const.'+const_ls[j]+',')
            elif const_ls[j]+')' in code_ls[i].replace(' ',''):
                code_ls[i]=code_ls[i].replace(const_ls[j]+')','const.'+const_ls[j]+')')

    code_ls=remove_items(code_ls,'')
    code='\n'.join(char for char  in code_ls)+'\n# Calling the main Function\nmain()'
    code=code.replace('/*',"'''").replace('*/',"'''").replace('true','True').replace('false','False').replace('else if','elif').replace('elseif','elif').replace(';','').replace('\t<SWITCH_END>','').replace(';','').replace('NULL','None')
    if consClassBool:
        consClass='#Initializing the constant Multiverse class\nclass const(Multiverse.Constants):\n\t{}\n'.format(consClass)
        code=consClass+code

    defines_str='\n'.join(char for char in list(defines))+'\n'
    if defines_str.strip()!='':
        imports_str='#Initializing DEFINE Variables\n'+defines_str
        code=imports_str+code

    imports_str='\n'.join(char for char in list(set(imports)))+'\n'
    if imports_str.strip()!='':
        imports_str='#Initializing import libraries\n'+imports_str
        code=imports_str+code
    if file == True:    
        with open(to_name,'w') as f:
            f.write(code)
        return 'Succesfully Saved to: '+to_name
    else:
        return code

'''#######################################################################################
                                         TO DO TASK  
1. sizeof -- sys.getsizeof()-----> done
2. Switch case default-----------> done
3. goto
4. volatile----------------------> done
5. signed unsigned short---------> done
6. const-------------------------> done
7. do----------------------------> done
8. math module-------------------> done
9. string module-----------------> done
10.enum--------------------------> done
11.struct------------------------> done
12.ctype module------------------> done
13.time module
14 dos module--------------------> done
15.#define-----------------------> done
16.union-------------------------> done
                                         Left reserved words
1. typedef     O
2. goto        O
.
                                         All reserved words in c
auto    double  int struct
break   else    long    switch
case    enum    register    typedef
char    extern  return  union
continue    for signed  void
do  if  static  while
default goto    sizeof  volatile
const   float   short   unsigned
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
setdate
getdate
clock
time
difftime
strftime
mktime
localtime
gmtime
ctime
asctime

from aenum import Enum
class day(Enum, start=0):

    sunday = 1
    monday
    tuesday = 5
    wednesday
    thursday = 10
    friday
    saturday
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if 'isalpha(' in code_ls[i].replace(' ',''):
            nTabs=code_ls[i].count('\t')
            var=code_ls[i].split('isalpha(')[1].split(')')[0].strip()
            begin=code_ls[i].split('isalpha(')[0]
            code_ls[i]=code_ls[i].replace(var,'').replace(begin,'')
            code_ls[i]='\t'*nTabs+begin.strip()+var+'.'+code_ls[i].strip()
#######################################################################################'''