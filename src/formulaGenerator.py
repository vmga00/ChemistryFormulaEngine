from FormulaElement import *
from Element import *
from periodicTable import *
import random

def main():
	print('hoi')
	print('---------------------')
	print(generateFormula())
	print('---------------------')
	print('byee')
	
def getRandom(floor, ceil):
	return random.randrange(floor, ceil)

def getRandomElement():
	return random.choice(list(periodicTable.keys()))

def setElements():
	total = getRandom(2,6)
	elements = []
	counter=0
	while counter < total:
		element = getRandomElement()
		if element not in elements:
			elements.append(element)
			counter+=1
	return elements

def setSubindexes(elements):
	formula = ''
	total = len(elements)
	for index in elements:
		subindex = getRandom(1,5)
		if subindex != 1:
			formula += index + str(subindex)
		else:
			formula+=index
	return formula

def generateFormula():
	return setSubindexes(setElements())

if __name__ == '__main__':
	main()