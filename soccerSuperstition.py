validNumbers = []
allPositions = [[0, 0, 0]]
validPositions = []

def soccerSuperstition(n, k, t):
	findValidNumbers(k)
	#print(len(validNumbers))
	#print(validNumbers)

	findAllPositions(n)
	#print(len(allPositions))

	findValidPositions(n, t)
	#print(len(validPositions))
	#for pos in validPositions:
		#print(str(validNumbers[pos[0]]) + " " + str(validNumbers[pos[1]]) + " " + str(validNumbers[pos[2]]))
		
	return len(validPositions)

def findValidNumbers(k):
	for num in range(100):
		if abs(num / 10 - num % 10) < k:
			validNumbers.append(num)

def findAllPositions(n):
	for i in range(1, pow(len(validNumbers), n)):
		allPositions.append(list(allPositions[i-1]))

		for j in range(n):
			if allPositions[i-1][j] + 1 < len(validNumbers):
				allPositions[i][j] = allPositions[i-1][j] + 1
				break
			else:
				allPositions[i][j] = 0

def findValidPositions(n, t):
	for pos in allPositions:
		for i in range(len(pos)):
			if ((validNumbers[pos[i]] % 10) + int(validNumbers[pos[(i+1) % len(pos)]] / 10)) > t:
				if i == len(pos) - 1:
					validPositions.append(list(pos))
			else:
				break

def makeRotations(combo):
	rotations = []
	
	for i in range(len(combo)):
		temp = combo[i:]
		temp += combo[:i]
		rotations.append(temp)
	
	return rotations