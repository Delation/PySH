def cd(location:str = None):
	if location:
		os.chdir(location)
	else:
		os.chdir(home_cwd)
	return
