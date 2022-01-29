#! /PySH/cli
def grep(option:str, search_string:str, location:str):
	usage = Utility().require_opts([option,],['i','c','r'])
	if option == usage[0]:
		if not os.path.isfile(location):raise FileNotFoundError(f'file {location} not found')
		with open(location,'r') as file:
			return '\n'.join([ i for i in file.read().split('\n') if search_string.lower() in i.lower() ])
	elif option == usage[1]:
		if not os.path.isfile(location):raise FileNotFoundError(f'file {location} not found')
		with open(location,'r') as file:
			return str(len([ i for i in file.read().split('\n') if search_string in i ]))
	elif option == usage[2]:
		if os.path.isdir(location):
			list = []
			for p, s, f in os.walk(location):
				[ list.append(p + '/' + i) for i in f ]
			for i in list:
				try:open(i,'r',encoding='utf-8').read()
				except:list.remove(i)
			return '\n'.join([ i + ':' + ' '.join([ i for i in open(i,'r',encoding='utf-8',errors='replace').read().split('\n') if search_string in i ]) for i in list if search_string in open(i,'r',encoding='utf-8',errors='replace').read() ])
		elif os.path.isfile(location):
			with open(location,'r') as file:
				return '\n'.join([ i for i in file.read().split('\n') if search_string in i ])
		else:
			raise FileNotFoundError(f'directory {location} not found')
		return
	return
