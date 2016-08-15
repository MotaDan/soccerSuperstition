validNumbers = []
allPositions = [[0, 0, 0]]
validPositions = []

# https://codefights.com/challenge/RRFe66MNdgwokujxD/main
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

# Finds all valid numbers. A number ab is valid if the difference between a and b is less than k.
def findValidNumbers(k):
	for num in range(100):
		if abs(num / 10 - num % 10) < k:
			validNumbers.append(num)

# finds all the combinations of the valid numbers. Stores them as positions in the valid numbers list.
def findAllPositions(n):
	for i in range(1, pow(len(validNumbers), n)):
		allPositions.append(list(allPositions[i-1]))

		for j in range(n):
			if allPositions[i-1][j] + 1 < len(validNumbers):
				allPositions[i][j] = allPositions[i-1][j] + 1
				break
			else:
				allPositions[i][j] = 0

# Checks that with two adjacent numbers ab cd the sum of b and c are greater than t.
def findValidPositions(n, t):
	for pos in allPositions:
		for i in range(len(pos)):
			if ((validNumbers[pos[i]] % 10) + int(validNumbers[pos[(i+1) % len(pos)]] / 10)) > t:
				if i == len(pos) - 1:
					validPositions.append(list(pos))
			else:
				break

# Takes in a list of numbers and returns a list of all the rotations of the list.
def makeRotations(combo):
	rotations = []
	
	for i in range(len(combo)):
		temp = combo[i:]
		temp += combo[:i]
		rotations.append(temp)
	
	return rotations

import unittest

# Testing class
class TestSoccerSuperstition(unittest.TestCase):
	def test_makeRotations(self):
		testList = [1, 2, 3]
		self.assertEqual(makeRotations(testList), [[1, 2, 3], [2, 3, 1], [3, 1, 2]])
	
	def test_soccerSuperstition(self):
		self.assertEqual(soccerSuperstition(3, 2, 16), 27)
		
if __name__ == '__main__':
	runner = unittest.TextTestRunner(verbosity = 2)
	unittest.main(testRunner = runner)