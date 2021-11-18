import os, inspect, sys as system, platform
shell = None

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
