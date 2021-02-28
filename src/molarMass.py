from engine import *
from formulaGenerator import *
from periodicTable import *
from Element import *
from FormulaElement import *

def main():
	print('holi')
	print('------------------')
	formula = generateFormula()
	print('given that: '+formula +' calculate its molar mass')
	print('------------------')
	e = getFormulaElementsFromList(getListFromString(formula,' '))
	for i in e:
		for j in i:
			print(j.__dict__)
	print('------------------')
	print('Molar Mass: '+"{:.2f}".format(getMolarMass(e)))
	print('------------------')
	print('byeeee')

def getMolarMass(lista):
	molarMass = 0
	for fElement in lista:
		tmp = 0
		for element in fElement:
			symbol = element.symbol
			subindex = element.subindex
			weight = periodicTable[element.symbol].weight
			if subindex == '':
				subindex = 1
			tmp = float(subindex) * float(weight)
			print('[{}][{}][{}] = {:.2f}'.format(symbol,subindex,weight,tmp))
			molarMass += tmp
	return molarMass


if __name__ == '__main__':
	main()