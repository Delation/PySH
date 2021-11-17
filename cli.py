# Please don't rely on already existing shell commands for function usage
# -Delation

from enum import Enum # For operations
OS = Enum('Operating System', 'windows mac ?')

from dataclasses import dataclass # For internal storage sorting
@dataclass
class User:
	username: str
	flags: list
	password: str = None

import os, inspect, sys, platform

shell = 'PySH'
accounts = []
account = None
flags = []
hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed:
	os.environ['PYTHONHASHSEED'] = '0'
	os.execv(sys.executable, [sys.executable] + sys.argv)

class Login():
	def create_log_file(self,path:str = './user.txt'):
		if not os.path.isfile(path):
			with open(path,'a') as i:
				i.write('')
		else:
			return True
	def get_login(self,path:str = './user.txt'): # from file
		with open(path,'r',encoding='utf-8-sig') as i:
			for n in i.readlines():
				args = n.split('|')
				if len(args) < 3:
					break
				test = User(args[0],args[1].split(','),int(args[2]))
				accounts.append(test)
	def add_login(self,account:User,path:str = './user.txt'):
		with open(path,'a') as i:
			i.write(f'{account.username}|{",".join(account.flags)}|{account.password}\n')

class PySH():
	def cd(self,args:list = []):
		Utility().check_args(args,0,1)
		if args:
			path = args[0]
			os.chdir(path)
		return
	def ls(self,args:list = []):
		print('# Notice of usage - unfinised command')
		# Currently, since I'm a couch potato, this command simply just redirects into
		# the system's implementation of it
		# No regard for whether or not the command actually exists, might I add.
		Utility().check_args(args,0,1)
		return os.system(f'ls {" ".join(args)}')
		lines, columns = Utility().get_size()
		o = ' '.join(os.listdir(os.getcwd()))
		return '\n'.join(o[i:i+columns] for i in range(0, len(o), columns))
	def clear(self,args:list = []):
		Utility().check_args(args)
		print('\033[H\033[J', end='')
		return
	def cat(self,args:list = []):
		Utility().check_args(args,1,1)
		if not os.path.isfile(args[0]):
			raise FileNotFoundError('invalid file location')
		self.clear()
		lines, columns = Utility().get_size()
		with open(args[0],'r') as file:
			rows = file.read().split('\n')
		print(f'{args[0]}'+'-'*(columns-len(args[0])))
		for i in range(lines-3):
			try:print(rows[i][:columns])
			except:break
		if len(rows) > lines-3:
			print('-'*(columns-12)+'File cut off')
		else:
			print('-'*columns)
		return
	def test(self,args:list = []):
		return 'Working well!'
	def uname(self,args:list = []):
		Utility().check_args(args,0,1)
		usage = Utility().require_opts(args,['a','m','n','p','r','s','v'])
		if not args or args[0] == usage[0]:
			return ' '.join(os.uname())
		elif args[0] == usage[1]:
			return platform.machine()
		elif args[0] == usage[2]:
			return platform.node()
		elif args[0] == usage[3]:
			return platform.processor()
		elif args[0] == usage[4]:
			return platform.release()
		elif args[0] == usage[5]:
			return platform.system()
		elif args[0] == usage[6]:
			return platform.version()
	def groups(self,args:list = []):
		Utility().check_args(args,0,1)
		args.append(account.username)
		for i in accounts:
			if i.username == args[0]:
				return f'{i.username} ' + ' '.join(i.flags)
		raise ValueError('unknown account')
	def sys(self,args:list = []):
		Utility().check_args(args,1,999)
		return os.system(' '.join(args))
	def python(self,args:list = []):
		# AYO, WHY AIN'T THIS IMPLEMENTED YET!
		# Reminder: Use PyTAS's implementation of this feature
		return
	def exit(self,args:list = []):
		Utility().check_args(args)
		quit()

class Utility():
	def check_args(self,args:list,min:int = 0,max:int = 0):
		if len(args) < min:
			raise IndexError('not enough arguments')
		elif len(args) > max:
			raise IndexError('too many arguments')
		else:
			return True
	def require_opts(self,args:list,usage:list):
		e = f'illegal option %s\nusage: {inspect.stack()[1][3]} [-{"".join(usage)}]'
		for i in args:
			if not i.startswith('-'):
				raise ValueError(e % i)
			if i.replace('-','') not in usage:
				raise ValueError(e % i)
		return [ '-' + o for o in usage ]
	def get_size(self):
		try:
			return os.get_terminal_size().lines, os.get_terminal_size().columns
		except:
			try:return [ int(o) for o in os.popen('stty size', 'r').read().split() ]
			except:return 50, 100#raise Exception('cannot get console size')

def main():
	global account
	global accounts
	global flags
	if Login().create_log_file():
		Login().get_login()
	else:
		flags.append('administrator')
	log = False
	account = User(input('Username: '),flags)
	for i in accounts:
		if account.username == i.username:
			account.password = hash(input(f'Welcome back, {account.username}\nPlease enter your password: '))
			for i in accounts:
				if account.username == i.username and account.password == i.password:
					log = True
			break
	if flags:
		while not account.password:
			account.password = hash(input('This account isn\'t recognized.\nPlease enter a new password: '))
			if account.password:
				Login().add_login(account)
				log = True
				accounts.append(account)
	if not log:
		print('Failed login. Please try again')
		main()
		return

	PySH().clear()
	commands = [o for o in inspect.getmembers(PySH)if inspect.isfunction(o[1])]
	while log:
		location = os.getcwd()
		work = False
		cmd = input(f'{os.path.dirname(location)}:~ {account.username}$ ').lstrip().rstrip().split(' ')
		for i in commands:
			if cmd[0] == i[0]:
				try:
					cmd.pop(0)
					output = i[1](PySH(),cmd)
					if output:
						print(output)
				except Exception as e:
					print(f'{shell}: {i[0]}: {e}')
				work = True
				break
		if not work:
			print(f'{shell}: command not found: {cmd[0]}')
	main()
	return

if __name__ == "__main__":
	main()
