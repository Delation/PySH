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

import os, inspect, sys

shell = 'PySH'
accounts = []
hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed:
	os.environ['PYTHONHASHSEED'] = '0'
	os.execv(sys.executable, [sys.executable] + sys.argv)

class Login():
	def create_log_file(self,path:str = './user.txt'):
		with open(path,'a') as i:
			i.write('')
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
			i.write(f'{account.username}|{account.flags}|{account.password}\n')

class PySH():
	def cd(self,args:list = []):
		Utility().check_args(args,0,1)
		if args:
			path = args[0]
			os.chdir(path)
		return
	def ls(self,args:list = []):
		Utility().check_args(args,0,1)
		return ' '.join(os.listdir(os.getcwd()))
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
	def sys(self,args:list = []):
		Utility().check_args(args,1,999)
		return os.system(' '.join(args))
	def python(self,args:list = []):
		# AYO, WHY AIN'T THIS IMPLEMENTED YET!
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
	def get_size(self):
		try:
			return os.get_terminal_size().lines, os.get_terminal_size().columns
		except:
			try:return [ int(o) for o in os.popen('stty size', 'r').read().split() ]
			except:return 50, 100#raise Exception('cannot get console size')

def main():
	Login().create_log_file()
	Login().get_login()
	log = False
	account = User(input('Username: '),[])
	for i in accounts:
		if account.username == i.username:
			account.password = hash(input(f'Welcome back, {account.username}\nPlease enter your password: '))
			for i in accounts:
				if account.username == i.username and account.password == i.password:
					log = True
			break
	while not account.password:
		account.password = hash(input('This account isn\'t recognized.\nPlease enter a new password: '))
		if account.password:
			Login().add_login(account)
			log = True
	if not log:
		print('Failed login. Please try again')
		main()
		return

	PySH().clear()
	commands = [o for o in inspect.getmembers(PySH)if inspect.isfunction(o[1])]
	while log:
		location = os.getcwd()
		work = False
		cmd = input(f'{os.path.dirname(location)}:~ {account.username}$ ').split(' ')
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
