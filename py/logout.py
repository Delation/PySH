#! /PySH/cli
def logout():
	global account
	username = account.username
	account = None
	return f'User {username} has been logged out.'
