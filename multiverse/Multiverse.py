import pathlib as _pathlib
import subprocess as _subprocess
from multiverse.C.c2py import _c2py
import os as _os
import inspect as _inspect

#-------------------------------------UNIVERSE-------------------------------------------------
class Universe:

	def __init__(self):
		self.C = self.C()
		#self.JavaScript = self.JavaScript()
		#self.Java = self.Java()
		#self.cPlus = self.cPlus()
		#self.Dart = self.Dart()
		#self.Golang = self.Golang()

	class C:
		#show cmd
		def execute(self,path,**kwargs):
			pat=_pathlib.Path().absolute()
			filename='foo'
			k=kwargs.keys()
			accepted_args=['saveAs']
			bad_args=[char for char in k if char not in accepted_args]
			if len(bad_args) != 0:
				raise Exception('Invalid Parameters Passed')
			else:
				if 'saveAs' in kwargs.keys():
					filename=str(kwargs.get('saveAs')).split('.')[0]

				if _os.path.exists(path):
					p = _subprocess.Popen("gcc "+path+" -o"+filename, shell=True)
					p.wait()
					_os.system('echo Result: & '+filename+' .echo & pause')
					if 'saveAs' not in kwargs.keys():
						_os.remove(filename+'.exe')
				else:
					return "Invalid Path given"

		#do not show cmd
		def get_output(self,text,**kwargs):

			pat=_pathlib.Path().absolute()
			k=kwargs.keys()
			accepted_args=['string','inputName','outputName','scanf']
			bad_args=[char for char in k if char not in accepted_args]
			
			if len(bad_args) != 0:
				raise Exception('Invalid Parameters Passed')
			
			else:
				for key, value in kwargs.items():

					if key == 'string' and value==False:
						if _os.path.exists(text):
							filename="foo.exe"
							if "inputName" in k:
								raise Exception("Error: Both inputName and path are given!")
							if "outputName" in k:
								filename=kwargs.get('outputName').split('.')[0]+'.exe'

							if 'scanf' in kwargs.keys():
								with open(text,'r') as f:
									code=f.read()

								if 'scanf("' in code:
									old=code.split('scanf("')[1].split('"')[0]
									new=old.replace("\n","\\n")
									code=code.replace(old,new)
								elif "scanf('" in code:
									old=code.split("scanf('")[1].split("'")[0]
									new=old.replace("\n","\\n")
									code=code.replace(old,new)

								inp=kwargs.get('scanf')
								if code.count('scanf') != len(inp):
									raise Exception("input parameter and the code scanf doesn't match")
									return None
								else:
									i = 1   #initial step
									while i < len(inp):
										inp.insert(i,'\n')
										i = i + 3 + 1 
									p = _subprocess.Popen("gcc "+text+" -o"+filename.split('.')[0], shell=True)
									p.wait()
									p1 = _subprocess.Popen([filename.split('.')[0]], stdout = _subprocess.PIPE, stdin = _subprocess.PIPE,encoding='utf8')
									out=p1.communicate(''.join(char for char in inp))[0]
									if 'outputName' not in kwargs.keys():
										_os.remove(filename+'.exe')
									return out

							_subprocess.call(["gcc", text, "-o"+filename.split('.')[0]],shell=True)
							return str(_subprocess.check_output([_os.path.join(pat,filename)])).strip()[2:-1]
						else:
							raise Exception("Invalid Path given")

					elif key == 'string' and value==True:
						iname='temp.c'
						oname='foo.exe'

						if "inputName" in k:
							iname=kwargs.get('inputName').split('.')[0]+'.c'
						if "outputName" in k:
							oname=kwargs.get('outputName').split('.')[0]+'.exe'

						if 'scanf("' in text:
							old=text.split('scanf("')[1].split('"')[0]
							new=old.replace("\n","\\n")
							text=text.replace(old,new)
						elif "scanf('" in text:
							old=text.split("scanf('")[1].split("'")[0]
							new=old.replace("\n","\\n")
							text=text.replace(old,new)

						with open(_os.path.join(pat,iname),'w') as f:
							f.write(text)

						if 'scanf' in kwargs.keys():
							with open(iname,'r') as f:
								code=f.read()
							inp=kwargs.get('scanf')
							if code.count('scanf') != len(inp):
								raise Exception("input parameter and the code scanf doesn't match")
								return None
							else:
								i = 1   #initial step
								while i < len(inp):
									inp.insert(i,'\n')
									i = i + 3 + 1
								p = _subprocess.Popen("gcc "+iname+" -o"+oname.split('.')[0], shell=True)
								p.wait()
								p1 = _subprocess.Popen([oname.split('.')[0]], stdout = _subprocess.PIPE, stdin = _subprocess.PIPE,encoding='utf8')
								out=p1.communicate(''.join(char for char in inp))[0]
								if 'outputName' not in kwargs.keys():
									_os.remove(oname)
								if 'inputName' not in kwargs.keys():
									_os.remove(iname)
								return out

						_subprocess.call(["gcc", _os.path.join(pat,iname), "-o"+_os.path.join(pat,oname.split('.')[0])],shell=True)
						res=str(_subprocess.check_output([_os.path.join(pat,oname)])).strip()[2:-1]
						if "inputName" not in k:
							_os.remove(_os.path.join(pat,iname))
						if "outputName" not in k:
							_os.remove(_os.path.join(pat,oname))
						return res

				if _os.path.exists(text):
					filename="foo.exe"
					if "inputName" in k:
						raise Exception("Both inputName and path are cannot be given")
					if "outputName" in k:
						filename=kwargs.get('outputName').split('.')[0]+'.exe'

					if 'scanf' in k:
						with open(text,'r') as f:
							code=f.read()
						inp=kwargs.get('scanf')
						if code.count('scanf') != len(inp):
							raise Exception("input parameter and the code scanf doesn't match")
							return None
						else:
							i = 1   #initial step
							while i < len(inp):
								inp.insert(i,'\n')
								i = i + 3 + 1 
							p = _subprocess.Popen("gcc "+text+" -o"+filename.split('.')[0], shell=True)
							p.wait()
							p1 = _subprocess.Popen([filename], stdout = _subprocess.PIPE, stdin = _subprocess.PIPE,encoding='utf8')
							out=str(p1.communicate(''.join(char for char in inp))[0])
							if 'outputName' not in kwargs.keys():
								_os.remove(filename)
							return out

					_subprocess.call(["gcc", text, "-o"+filename.split('.')[0]],shell=True)
					res=str(_subprocess.check_output([_os.path.join(pat,filename)])).strip()[2:-1]
					_os.remove(filename)
					return res
				else:
					raise Exception("Invalid Path given")

		def c2py(self,**kwargs):
			k=kwargs.keys()
			accepted_args=['from_file','to_file','file','code']
			bad_args=[char for char in k if char not in accepted_args]
			
			if len(bad_args) != 0:
				raise Exception('Invalid Parameters Passed')
			
			else:
				for key, value in kwargs.items():
					if key == 'file' and value == True:
						if 'from_file' in k and 'to_file' in k:
							_c2py.dec1(kwargs['from_file'],kwargs['to_file'])
							return 'Successfully saved to '+kwargs['to_file']
						else:
							raise Exception('Argument from_file or to_file not given')
					elif key == 'file' and value == False:
						if 'code' in k:
							resq=_c2py.dec2(kwargs['code'])
							return resq
						else:
							raise Exception('Argument code not given as file=False')


		def help(self,*args):
			if len(args)==0:
				print(_alls)
				return 
			if len(args)!=1:
				raise Exception('Pass only one module name or pass * to get complete guide')
			if args[0]=='c2py':
				print(_a)
				return 
			elif args[0]=='execute':
				print(_b)
				return 
			elif args[0]=='get_output':
				print(_c)
				return 
			elif args[0]=='*':
				print(_alls)
				return 
			else:
				raise Exception('argument passed is Invalid')
#-------------------------------------UNIVERSE-------------------------------------------------

#-------------------------------------CONSTANTS------------------------------------------------
def _with_metaclass(meta, *bases):
    """
    Function from jinja2/_compat.py. License: BSD.

    Use it like this::
        
        class BaseForm(object):
            pass
        
        class FormType(type):
            pass
        
        class Form(with_metaclass(FormType, BaseForm)):
            pass

    This requires a bit of explanation: the basic idea is to make a
    dummy metaclass for one level of class instantiation that replaces
    itself with the actual metaclass.  Because of internal type checks
    we also need to make sure that we downgrade the custom metaclass
    for one level to something closer to type (that's why __call__ and
    __init__ comes back from type etc.).
    
    This has the advantage over six.with_metaclass of not introducing
    dummy classes into the final MRO.
    """
    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__
        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)
    return metaclass('temporary_class', None, {})

class _ConstantsMeta(type):
    __NamedTypes = {}

    @classmethod
    def NamedValue(cls, typ):
        """Returns a 'NamedTyp' class derived from the given 'typ'.
        The results are cached, i.e. given the same type, the same
        class will be returned in subsequent calls."""
        Const = cls.__NamedTypes.get(typ, None)
        
        if Const is None:
            def __new__(cls, name, value):
                res = typ.__new__(cls, value)
                res._name = name
                res._namespace = None
                return res

            def name(self):
                return self._name
            
            def __repr__(self):
                if self._namespace is None:
                    return self._name
                if self._namespace.__module__ in ('__main__', '__builtin__'):
                    namespace = self._namespace.__name__
                else:
                    namespace = "%s.%s" % (self._namespace.__module__,
                                           self._namespace.__name__)
                return "%s.%s" % (namespace, self._name)

            dct = dict(
                __doc__ = """
 Named, typed constant (subclassed from original type, cf. `Constants`
 class).  Sole purpose is pretty-printing, i.e. __repr__ returns the
 constant's name instead of the original string representations.
 The name is also available via a `name()` method.""".lstrip(),
                __new__ = __new__,
                name = name,
                #__str__ = name,
                __repr__ = __repr__)

            typName = typ.__name__
            name = 'Named' + typName[0].upper() + typName[1:]
            Const = type(name, (typ, ), dct)

            cls.__NamedTypes[typ] = Const

        return Const
    
    def __new__(cls, name, bases, dct):
        constants = {}

        # replace class contents with values wrapped in (typed) Const-class:
        for member in dct:
            value = dct[member]
            if member.startswith('_') or _inspect.isfunction(value) or _inspect.ismethoddescriptor(value):
                continue
            Const = cls.NamedValue(type(value))
            c = Const(member, value)
            constants[member] = c
            dct[member] = c

        dct['__constants__'] = constants
        dct['__reverse__'] = dict((value, value) for key, value in constants.items())
        dct['__sorted__'] = sorted(constants.values(), key = lambda x: (id(type(x)), x))

        result = type.__new__(cls, name, bases, dct)

        # support namespace prefix in __repr__ by connecting the namespace here:
        for c in constants.values():
            c._namespace = result

        return result

    def __len__(self):
        return len(self.__constants__)

    def __iter__(self):
        return iter(self.__sorted__)

    def __setattr__(self, _name, _value):
        raise TypeError('Constants are not supposed to be changed ex post')

    def __contains__(self, x):
        return self.has_key(x) or self.has_value(x)

    def has_key(self, key):
        return key in self.__constants__

    def has_value(self, value):
        return value in self.__reverse__

    def keys(self):
        for c in self.__sorted__:
            yield c.name()

    def values(self):
        return self.__sorted__

    def items(self):
        for c in self.__sorted__:
            yield c.name(), c

class Constants(_with_metaclass(_ConstantsMeta)):
    """Base class for constant namespaces."""
    __slots__ = ()

    def __new__(cls, x):
        if cls.has_value(x):
            return cls.__reverse__[x]
        if cls.has_key(x):
            return cls.__constants__[x]
        raise ValueError('%s has no key or value %r' % (cls.__name__, x))
#-------------------------------------CONSTANTS------------------------------------------------

#############################################################################################################################
_alls='''
.______       _______     _______.  ______  __    __   _______    .___________. __  .___  ___.  _______ 
|   _  \     |   ____|   /       | /      ||  |  |  | |   ____|   |           ||  | |   \/   | |   ____|
|  |_)  |    |  |__     |   (----`|  ,----'|  |  |  | |  |__      `---|  |----`|  | |  \  /  | |  |__   
|      /     |   __|     \   \    |  |     |  |  |  | |   __|         |  |     |  | |  |\/|  | |   __|  
|  |\  \----.|  |____.----)   |   |  `----.|  `--'  | |  |____        |  |     |  | |  |  |  | |  |____ 
| _| `._____||_______|_______/     \______| \______/  |_______|       |__|     |__| |__|  |__| |_______|
                                                                                                        

     .  . '    .
      '   .            . '            .                +
              `                          '    . '
        .                         ,'`.                         .
   .                  .."    _.-;'    `.              .
              _.-"`.##%"_.--" ,'        `.           "#"     ___,,od000
           ,'"-_ _.-.--"\   ,'            `-_       '%#%',,/////00000HH
         ,'     |_.'     )`/-     __..--""`-_`-._    J L/////00000HHHHM
 . +   ,'   _.-"        / /   _-""           `-._`-_/___\///0000HHHHMMM
     .'_.-""      '    :_/_.-'                 _,`-/__V__\ 000HHHHHMMMM
 . _-""                         .        '   _,////\  |  /000HHHHHMMMMM
_-"   .       '  +  .              .        ,//////0\ | /00HHHHHHHMMMMM
       `                                   ,//////000\|/00HHHHHHHMMMMMM
.             '       .  ' .   .       '  ,//////00000|00HHHHHHHHMMMMMM
     .             .    .    '           ,//////000000|00HHHHHHHMMMMMMM
                  .  '      .       .   ,///////000000|0HHHHHHHHMMMMMMM
  '             '        .    '         ///////000000000HHHHHHHHMMMMMMM
                    +  .  . '    .     ,///////000000000HHHHHHHMMMMMMMM
     '      .              '   .       ///////000000000HHHHHHHHMMMMMMMM
   '                  . '              ///////000000000HHHHHHHHMMMMMMMM
                           .   '      ,///////000000000HHHHHHHHMMMMMMMM
       +         .        '   .    .  ////////000000000HHHHHHHHMMMMMMhs

                 _       _                  
                | |     | |                 
 ____   ___   __| |_   _| | _____  ___    _ 
|    \ / _ \ / _  | | | | || ___ |/___)  (_)
| | | | |_| ( (_| | |_| | || ____|___ |   _ 
|_|_|_|\___/ \____|____/ \_)_____|___/   (_)
                                            

1) c2py :-
• DESCRIPTION :- This module lets you convert any c code to python code.
• ARGUMENTS {**kwargs} :- 
	a) from_file(str)		b) to_file(str)		c) file(bool)		d)code(str)
• IMPORTANT PONTS :- 
	a) If you want to convert code from a .c file then use 'file=True' and pass 'from_file(.c) and to_file(.py)'
	b) If you want to convert code from string then use 'file=False' and pass 'code="ALL C CODE"' argument as the c program

2) execute :-
• DESCRIPTION :- This module lets you execute any c code and get realtime hands on experience in  the command prompt
• ARGUMENTS {**kwargs} :-
	a) saveAs(str)
• IMPORTANT POINTS :-
	a) Pass saveAs as argument, this will save the exe(output) to the given path
	b) if saveAs argument is not there then it will automatically remove the output from the pc

3) get_output :- 
• DESCRIPTION :- This module lets you only get the output without running the whole program(.c)
• ARGUMENTS {**kwargs} :- 
	a) string(bool)		b) inputName(str)		c) outputName(str)		d)scanf(list)
• IMPORTANT POINTS :-
	a) get_output take c code or path of a c file
	b) set string to True if you want to pass code to the function
	c) if you set string to False then you have to pass the path of the c file
	d) can also save the code by setting the inputName
	e) can also set outputName if you want to store the exe(output) to specific path
	f) scanf argument lets you pass arguments whch have to be input'''
#############################################################################################################################
_a='''
1) c2py :-
• DESCRIPTION :- This module lets you convert any c code to python code.
• ARGUMENTS {**kwargs} :- 
	a) from_file(str)		b) to_file(str)		c) file(bool)		d)code(str)
• IMPORTANT PONTS :- 
	a) If you want to convert code from a .c file then use 'file=True' and pass 'from_file(.c) and to_file(.py)'
	b) If you want to convert code from string then use 'file=False' and pass 'code="ALL C CODE"' argument as the c program'''
#############################################################################################################################
_b='''
2) execute :-
• DESCRIPTION :- This module lets you execute any c code and get realtime hands on experience in  the command prompt
• ARGUMENTS {**kwargs} :-
	a) saveAs(str)
• IMPORTANT POINTS :-
	a) Pass saveAs as argument, this will save the exe(output) to the given path
	b) if saveAs argument is not there then it will automatically remove the output from the pc'''
#############################################################################################################################
_c='''
3) get_output :- 
• DESCRIPTION :- This module lets you only get the output without running the whole program(.c)
• ARGUMENTS {**kwargs} :- 
	a) string(bool)		b) inputName(str)		c) outputName(str)		d)scanf(list)
• IMPORTANT POINTS :-
	a) get_output take c code or path of a c file
	b) set string to True if you want to pass code to the function
	c) if you set string to False then you have to pass the path of the c file
	d) can also save the code by setting the inputName
	e) can also set outputName if you want to store the exe(output) to specific path
	f) scanf argument lets you pass arguments whch have to be input'''
#############################################################################################################################
