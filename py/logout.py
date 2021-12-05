#!/bin/pysh
def logout(args:list = []):
	Utility().check_args(args)
	global account
	username = account.username
	account = None
	return f'User {username} has been logged out.'
