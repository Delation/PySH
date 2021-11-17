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

import os, inspect

shell = 'PySH'
accounts = []
	
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
	def cd(self,args):
		if len(args) > 1:
			raise IndexError('too many arguments')
		try: path = args[0]
		except: path = ''
		os.chdir(path)
		return
	def ls(self,args):
		return ' '.join(os.listdir(os.getcwd()))
	def clear(self,args):
		if len(args) != 0:
			raise IndexError('too many arguments')
		os.system('clear') # REWRITE IN PURE PYTHON
		return
	def sys(self,args):
		return os.system(' '.join(args))
	def python(self,args):
		# AYO, WHY AIN'T THIS IMPLEMENTED YET!
		return
	def exit(self,args):
		if len(args) != 0:
			raise IndexError('too many arguments')
		quit()

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
	
	commands = [o for o in inspect.getmembers(PySH)if inspect.isfunction(o[1])]
	while log:
		location = os.getcwd()
		work = False
		cmd = input(f'{account.username} % {os.path.dirname(location)} >>> ').split(' ')
		for i in commands:
			if cmd[0] == i[0]:
				try:
					cmd.pop(0)
					output = i[1](PySH(),cmd)
					if output:
						print(output)
				except IndexError as e:
					print(f'{shell}: {i[0]}: {e}')
				except Exception as e:
					print(e)
				work = True
				break
		if not work:
			print('Unknown command')
	main()
	return	
	
if __name__ == "__main__":
	main()
