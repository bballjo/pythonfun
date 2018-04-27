


def loadSodoku( file):
	sodoku = [["B","B","B"],["B","B","B"],["B","B","B"]]
	f=open(file,"r")
	a = 0
	x = 0
	while a < len(sodoku[0]):
		sodoku[x][a] = f.readline().strip('\n')
		a += 1
		if a == len(sodoku[0]):
			a = 0
			x += 1
		if x == len(sodoku[0]):
			a = len(sodoku[0])
			x = len(sodoku[0])
	return sodoku;
print(loadSodoku("sodoku.txt"))	
sodoku = loadSodoku("sodoku.txt")	
	

def scoreSodoku( toScore):
	sodoku = toScore
	score = 0
	m = 0
	correctArray = [1,2,3] #arrangement doesnt matter
	while m < len(sodoku[0]):
		i=0
		while i < len(sodoku[m]):
			x=0
			while x < len(correctArray):
				#print(sodoku[0])
				#print(correctArray)
				if correctArray[x] == sodoku[m][i]:
					#print("match")
					correctArray[x] = 0
				x += 1
			i += 1
		n = 0
		while n < len(correctArray):
			if correctArray[n] == 0:
				n += 1
			else:
				score += 1
				n += 1
		correctArray = [1,2,3]
		m += 1


	return score;
	
print(scoreSodoku(loadSodoku("sodoku.txt")))

