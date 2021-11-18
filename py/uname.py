#!/bin/pysh
def uname(args:list = []):
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
