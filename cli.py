#!/usr/bin/env python3

from dataclasses import dataclass # For internal storage sorting
@dataclass
class User:
	username: str
	flags: list
	password: str = None

import os, sys

shell = 'PySH'
bin = '/'.join(sys.argv[0].split('/')[:-1]) + '/py/'
if sys.argv[0].count('/') < 1:
	bin = './py/'
if not os.path.isdir(bin):
	# Currently only supports darwin, will add case system when install.sh is updated
	bin = '/usr/local/share/pysh/'
	if not os.path.isdir(bin):
		print("Failed to get resources")
		quit()
accounts = []
account = None
flags = []
hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed:
	os.environ['PYTHONHASHSEED'] = '0'
	os.execv(sys.executable, [sys.executable] + sys.argv)

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
				test = User(args[0],args[1].split(','),int(args[2]))
				accounts.append(test)
	def add_login(self,account:User,path:str = bin+'users'):
		with open(path,'a') as i:
			i.write(f'{account.username}|{",".join(account.flags)}|{account.password}\n')

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
				except IndexError as e:
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

if __name__ == "__main__":
	main()
