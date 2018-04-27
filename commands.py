wordsArray = [
	'and','as', 'assert' ,'break' ,'class' ,
	'continue' ,'def' ,'del' ,'elif' ,'else' ,
	'except' ,'exec' ,'finally' ,'for' ,'from' ,
	'global' ,'if' ,'import' ,'in' ,'is' ,'lambda' ,
	'not' ,'or' ,'pass' ,'print' ,'raise' ,'return' ,
	'try' ,'while' ,'with' ,'yield'
]

wordsWithParenteses = [
	'print'	
]

wordsWithSemicolons = [
	'if', 'for', 'elif', 'for', 'else', 'while'
]

def Tab():
	return '\t'

def Line(line):
	return str(line) + '\n'

def Print(word):
	return 'print("' + str(word) + '"\n)'

def For(array):
	return 'for item in ' + str(array) + ':\n' + Tab()
	
def If(expr):
	return 'if ' + str(expr) + ':\n' + Tab()
	 
def IfEl(expr):
	return 'ifel ' + str(expr) + ':\n' + Tab()

def Else():
	return 'else:' + Tab()

def While(expr):
	return 'while ' + str(expt) + ':\n' + Tab()