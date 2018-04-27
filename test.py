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
	'if', 'for', 'elif', 'for', 'else'
]

def generateTab():
	return '\t'

def generateLine(str):
	return str + '\n'

def generatePrint(word):
	return 'print("' + word + '"\n)'
	return 
	

def generateIf(expr):
	return 'if ' + expr + ':\n'
	
