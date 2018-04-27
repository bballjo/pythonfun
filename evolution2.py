print("Evolution v1")

sodoku = [[1,1,3],[3,2,1],[2,3,1]]

#print("Sodoku Puzzle:")
#print(sodoku[0])
#print(sodoku[1])
#print(sodoku[2])

#print(sodoku[0][1])
correctArray = [1,2,3]

score = 0
i=0
while i < len(sodoku[0]):
	x=0
	while x < len(correctArray):
		#print(sodoku[0])
		#print(correctArray)
		if correctArray[x] == sodoku[0][i]:
			print("match")
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
print("SCORE:")
print(score)
print(correctArray)

