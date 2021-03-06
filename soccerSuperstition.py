# https://codefights.com/challenge/RRFe66MNdgwokujxD/main
def soccerSuperstition(n, k, t):
	validNumbers = findValidNumbers(k)

	allPositions = findAllPositionsEnhanced(n, validNumbers)

	validPositions = findValidPositionsEnhanced(t, validNumbers, allPositions)

	# Prints the values of the returned validPositions.
	#for pos in validPositions:
		#print(str(validNumbers[pos[0]]) + " " + str(validNumbers[pos[1]]) + " " + str(validNumbers[pos[2]]))
		
	return len(validPositions)

# Finds all valid numbers. A number ab is valid if the difference between a and b is less than k.
def findValidNumbers(k):
	validNumbers = []
	
	for num in range(100):
		if abs(num / 10 - num % 10) < k:
			validNumbers.append(num)
		
	return validNumbers

# Finds all the combinations of the valid numbers. Stores them as positions in the valid numbers list.
def findAllPositions(n, validNumbers):
	allPositions = [[0 for x in range(n)]]
	
	for i in range(1, pow(len(validNumbers), n)):
		allPositions.append(list(allPositions[i-1]))

		for j in range(n):
			if allPositions[i-1][j] + 1 < len(validNumbers):
				allPositions[i][j] = allPositions[i-1][j] + 1
				break
			else:
				allPositions[i][j] = 0
			
	return allPositions

# Finds all the combinations of the valid numbers. Stores them as positions in the valid numbers list.
def findAllPositionsEnhanced(n, validNumbers):
	allPositions = [[0 for x in range(n)]]
	seenCombos = {}
	uniquePositions = []

	for i in range(1, pow(len(validNumbers), n)):
		allPositions.append(list(allPositions[i-1]))

		for j in range(n):
			if allPositions[i-1][j] + 1 < len(validNumbers):
				allPositions[i][j] = allPositions[i-1][j] + 1

				if not hasComboBeenSeen(seenCombos, allPositions[i]):
					uniquePositions.append(allPositions[i])

				break
			else:
				allPositions[i][j] = 0

				if not hasComboBeenSeen(seenCombos, allPositions[i]):
					uniquePositions.append(allPositions[i])

	return uniquePositions

# Checks that with two adjacent numbers ab cd the sum of b and c are greater than t.
def findValidPositions(t, validNumbers, allPositions):
	validPositions = []
	
	for pos in allPositions:
		for i in range(len(pos)):
			if ((validNumbers[pos[i]] % 10) + int(validNumbers[pos[(i+1) % len(pos)]] / 10)) > t:
				if i == len(pos) - 1:
					validPositions.append(list(pos))
			else:
				break
			
	return validPositions

# Checks that with two adjacent numbers ab cd the sum of b and c are greater than t.
def findValidPositionsEnhanced(t, validNumbers, allPositions):
	validPositions = []

	for pos in allPositions:
		for i in range(len(pos)):
			if ((validNumbers[pos[i]] % 10) + int(validNumbers[pos[(i+1) % len(pos)]] / 10)) > t:
				if i == len(pos) - 1:
					validPositions.extend(makeRotations(pos))
			else:
				break

	return validPositions

# Takes in a list of numbers and returns a list of all the rotations of the list.
def makeRotations(combo):
	rotations = []
	
	# Checking that the combo is not the same value repeated in all positions.
	if len(set(combo)) > 1:
		for i in range(len(combo)):
			temp = combo[i:]
			temp += combo[:i]
			rotations.append(temp)
	else:
		rotations.append(combo)
		return rotations
	
	return rotations

# Checks if a list of numbers has been seen before. seenCombos is a dictionary with a frozenset key and list of list data.
def hasComboBeenSeen(seenCombos, combo):
	if frozenset(combo) in seenCombos:
		if combo not in seenCombos[frozenset(combo)]:
			seenCombos[frozenset(combo)].extend(makeRotations(combo))
			return False
		else:
			return True
	else:
		seenCombos[frozenset(combo)] = makeRotations(combo)
		return False

# Testing class
import unittest
import time

class TestSoccerSuperstition(unittest.TestCase):
	def setUp(self):
		self.startTime = time.time()
	
	def tearDown(self):
		t = time.time() - self.startTime
		print "Ran in %.3fs " % (t),
	
	def test_makeRotations(self):
		testList = [1, 2, 3]
		self.assertEqual(makeRotations(testList), [[1, 2, 3], [2, 3, 1], [3, 1, 2]])
		
	def test_makeRotations2(self):
		testList = [1, 1, 1]
		self.assertEqual(makeRotations(testList), [[1, 1, 1]])

	def test_hasComboBeenSeen1(self):
		testList = [0, 0, 0]
		testSeenCombos = {frozenset([0, 0, 0]): [[0, 0, 0]]}
		self.assertTrue(hasComboBeenSeen(testSeenCombos, testList))
		self.assertEqual(testSeenCombos, {frozenset([0, 0, 0]): [[0, 0, 0]]})
		
	def test_hasComboBeenSeen2(self):
		testList = [0, 0, 0]
		testSeenCombos = {}
		self.assertFalse(hasComboBeenSeen(testSeenCombos, testList))
		self.assertEqual(testSeenCombos, {frozenset([0, 0, 0]): [[0, 0, 0]]})
		
	def test_hasComboBeenSeen3(self):
		testList = [0, 1, 2]
		testSeenCombos = {frozenset([0, 2, 1]): [[0, 2, 1], [2, 1, 0], [1, 0, 2]]}
		self.assertFalse(hasComboBeenSeen(testSeenCombos, testList))
		self.assertEqual(testSeenCombos, {frozenset([0, 1, 2]): [[0, 2, 1], [2, 1, 0], [1, 0, 2], [0, 1, 2], [1, 2, 0], [2, 0, 1]]})
	
	def test_findValidNumbers(self):
		self.assertEqual(findValidNumbers(2), [0, 1, 10, 11, 12, 21, 22, 23, 32, 33, 34, 43, 44, 45, 54, 55, 56, 65, 66, 67, 76, 77, 78, 87, 88, 89, 98, 99])
	
	def test_findAllPositions(self):
		validNumbers = findValidNumbers(2)
		validNumbersClean = validNumbers
		self.assertEqual(len(findAllPositions(3, validNumbers)), 21952)
		self.assertEqual(validNumbers, validNumbersClean)
	
	def test_findAllPositionsTime(self):
		validNumbers = validNumbersTime
		validNumbersClean = validNumbers
		allPositions = findAllPositions(3, validNumbers)
		self.assertEqual(len(allPositions), 1000000)
		self.assertEqual(validNumbers, validNumbersClean)
		
	def test_findAllPositionsEnhanced(self):
		validNumbers = findValidNumbers(2)
		validNumbersClean = validNumbers
		self.assertEqual(len(findAllPositionsEnhanced(3, validNumbers)), 7337)
		self.assertEqual(validNumbers, validNumbersClean)
	
	def test_findAllPositionsEnhancedTime(self):
		validNumbers = validNumbersTime
		validNumbersClean = validNumbers
		allPositionsEnhanced = findAllPositionsEnhanced(3, validNumbers)
		self.assertEqual(len(allPositionsEnhanced), 333401)
		self.assertEqual(validNumbers, validNumbersClean)

	def test_findValidPositions(self):
		validNumbers = findValidNumbers(2)
		validNumbersClean = validNumbers
		allPositions = findAllPositions(3, validNumbers)
		allPositionsClean = allPositions
		validPositions = findValidPositions(16, validNumbers, allPositions)
		self.assertEqual(len(validPositions), 27)
		self.assertEqual(validPositions, [[27, 25, 24], [26, 27, 24], [27, 27, 24], [25, 25, 25], [27, 25, 25], [24, 27, 25], [25, 27, 25], [26, 27, 25], [27, 27, 25], [27, 24, 26], [27, 25, 26], [26, 26, 26], [27, 26, 26], [26, 27, 26], [27, 27, 26], [25, 24, 27], [27, 24, 27], [25, 25, 27], [27, 25, 27], [24, 26, 27], [25, 26, 27], [26, 26, 27], [27, 26, 27], [24, 27, 27], [25, 27, 27], [26, 27, 27], [27, 27, 27]])
		self.assertEqual(validNumbers, validNumbersClean)
		self.assertEqual(allPositions, allPositionsClean)
	
	def test_findValidPositionsTime(self):
		validNumbers = validNumbersTime
		validNumbersClean = validNumbers
		allPositions = allPositionsTime
		allPositionsClean = allPositions
		validPositions = findValidPositions(17, validNumbers, allPositions)
		self.assertEqual(len(validPositions), 1)
		self.assertEqual(validNumbers, validNumbersClean)
		self.assertEqual(allPositions, allPositionsClean)

	def test_findValidPositionsEnhanced(self):
		validNumbers = findValidNumbers(2)
		validNumbersClean = validNumbers
		allPositions = findAllPositionsEnhanced(3, validNumbers)
		allPositionsClean = allPositions
		validPositions = findValidPositionsEnhanced(16, validNumbers, allPositions)
		self.assertEqual(len(validPositions), 27)
		self.assertEqual(validPositions, [[27, 25, 24], [25, 24, 27], [24, 27, 25], [26, 27, 24], [27, 24, 26], [24, 26, 27], [27, 27, 24], [27, 24, 27], [24, 27, 27], [25, 25, 25], [27, 25, 25], [25, 25, 27], [25, 27, 25], [26, 27, 25], [27, 25, 26], [25, 26, 27], [27, 27, 25], [27, 25, 27], [25, 27, 27], [26, 26, 26], [27, 26, 26], [26, 26, 27], [26, 27, 26], [27, 27, 26], [27, 26, 27], [26, 27, 27], [27, 27, 27]])
		self.assertEqual(validNumbers, validNumbersClean)
		self.assertEqual(allPositions, allPositionsClean)
	
	def test_findValidPositionsEnhancedTime(self):
		validNumbers = validNumbersTime
		validNumbersClean = validNumbers
		allPositions = allPositionsEnhancedTime
		allPositionsClean = allPositions
		validPositions = findValidPositionsEnhanced(17, validNumbers, allPositions)
		self.assertEqual(len(validPositions), 1)
		self.assertEqual(validNumbers, validNumbersClean)
		self.assertEqual(allPositions, allPositionsClean)

	def test_soccerSuperstition01(self):
		self.assertEqual(soccerSuperstition(3, 2, 16), 27)

	def test_soccerSuperstition02(self):
		self.assertEqual(soccerSuperstition(3, 10, 17), 1)

	def test_soccerSuperstition03(self):
		self.assertEqual(soccerSuperstition(3, 1, 1), 921)
		
	def test_soccerSuperstition04(self):
		self.assertEqual(soccerSuperstition(3, 10, 10), 46656)
		
	def test_soccerSuperstition05(self):
		self.assertEqual(soccerSuperstition(3, 10, 12), 9261)
		
	def test_soccerSuperstition06(self):
		self.assertEqual(soccerSuperstition(3, 9, 15), 216)
		
	def test_soccerSuperstition07(self):
		self.assertEqual(soccerSuperstition(3, 5, 7), 119580)
	
	def test_soccerSuperstition08(self):
		self.assertEqual(soccerSuperstition(3, 1, 16), 4)
		
	def test_soccerSuperstition09(self):
		self.assertEqual(soccerSuperstition(3, 4, 17), 1)
		
	def test_soccerSuperstition10(self):
		self.assertEqual(soccerSuperstition(3, 8, 14), 1000)
		
	def test_soccerSuperstition11(self):
		self.assertEqual(soccerSuperstition(3, 3, 11), 6937)
		
	def test_soccerSuperstition12(self):
		self.assertEqual(soccerSuperstition(3, 2, 8), 6309)
	
	def test_soccerSuperstition13(self):
		self.assertEqual(soccerSuperstition(3, 7, 4), 456001)
		
	def test_soccerSuperstition14(self):
		self.assertEqual(soccerSuperstition(3, 8, 8), 154107)
		
	def test_soccerSuperstition15(self):
		self.assertEqual(soccerSuperstition(3, 7, 16), 27)

if __name__ == '__main__':
	print "Preparing tests..."
	validNumbersTime = findValidNumbers(10)
	allPositionsTime = findAllPositions(3, validNumbersTime)
	allPositionsEnhancedTime = findAllPositionsEnhanced(3, validNumbersTime)
	runner = unittest.TextTestRunner(verbosity = 2)
	unittest.main(testRunner = runner)