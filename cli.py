#!/usr/bin/env python3

from dataclasses import dataclass # For internal storage sorting
@dataclass
class User:
	username: str
	flags: list
	password: str = None

import os, sys, hashlib

shell = 'PySH'
bin = '/'.join(sys.argv[0].split('/')[:-1]) + '/py/'
if sys.argv[0].count('/') < 1:
	bin = './py/'
platform = sys.platform
if not os.path.isdir(bin):
	if platform.startswith('darwin'):
		bin = '/usr/local/share/pysh/'
	elif platform.startswith('win'):
		bin = '/Windows/System32/PySH/py/'
	if not os.path.isdir(bin):
		quit('Failed to get resources')
accounts = []
account = None
flags = []

class Login():
	def create_log_file(self,path:str = bin+'users'):
		if not os.path.isfile(path):
			with open(path,'a') as i:
				i.write('')
		else:
			return True
	def get_login(self,path:str = bin+'users'): # from file
		with open(path,'r',encoding='utf-8-sig') as i:
			for n in i.readlines():
				args = n.split('|')
				if len(args) < 3:
					break
				h = User(args[0],args[1].split(','),args[2].strip())
				accounts.append(h)
	def add_login(self,account:User,path:str = bin+'users'):
		with open(path,'a') as i:
			i.write(f'{account.username}|{",".join(account.flags)}|{account.password}\n')

def main():
	global account, accounts, flags
	if Login().create_log_file():
		Login().get_login()
	else:
		flags.append('administrator')
	log = False
	account = User(input('Username: '), flags)
	for i in accounts:
		if account.username == i.username:
			account.password = hashlib.md5(input(f'Welcome back, {account.username}\nPlease enter your password: ').encode('utf-8',errors='replace')).hexdigest()
			for i in accounts:
				if account.username == i.username and account.password == i.password:
					log = True
			break
	if flags:
		while not account.password:
			account.password = hashlib.md5(input('This account isn\'t recognized.\nPlease enter a new password: ').encode('utf-8',errors='replace')).hexdigest()
			if account.password:
				Login().add_login(account)
				log = True
				accounts.append(account)
	if not log:
		print('Failed login. Please try again')
		main()
		return

	# Retrieve proper current account
	for i in accounts:
		if i.username == account.username:
			account = i
			break

	commands = {}

	i = []
	for (path, dirs, files) in os.walk(bin):
	    i.extend(files)
	    break
	for i in i:
		if not i.endswith('.py'):
			continue
		with open(bin + i,'r') as file:
			exec(file.read(), commands, None)
	commands['bin'] = bin
	commands['home_cwd'] = os.getcwd()
	commands['shell'] = shell
	commands['accounts'] = accounts
	commands['account'] = account
	if not len(sys.argv) > 1:
		commands['clear']()
	while log:
		if not commands['account']:
			log = False
			commands['clear']()
			main()
			return
		location = commands['os'].getcwd()
		work = False
		if len(sys.argv) > 1:
			cmd = sys.argv[2:]
			cmd.insert(0,os.path.splitext(sys.argv[1])[0][2:])
		else:
			cmd = input(f'{os.path.abspath(location)}:~ {account.username}$ ').lstrip().rstrip().split(' ')
		for i in commands:
			if i in ('__builtins__','system','os','inspect','platform') or not callable(commands[i]):
				continue
			if cmd[0] == i:
				try:
					cmd.pop(0)
					output = commands[i](*cmd)
					if output:
						print(output)
				except (IndexError, ValueError, FileNotFoundError, TypeError) as e:
					print(f'{shell}: {i}: {e}')
				except Exception as e:
					print(f'{shell}: {i}: {e}')
				work = True
				break
		if not work:
			print(f'{shell}: command not found: {cmd[0]}')
		if len(sys.argv) > 1:
			return
	main()
	return

if __name__ == '__main__':
	main()
