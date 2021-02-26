from FormulaElement import *
from periodicTable import *

formula = []

def main():
	print('holi')
	'''
	print('-----------------------------')
	for element in periodicTable:
		print('{} {}'.format(periodicTable[element].symbol, periodicTable[element].weight))
	'''
	print('-----------------------------')
	equation = 'H2 + O -> H2O'
	print('equation: '+equation)
	print('-----------------------------')
	print('getting reactives and products')
	eq = getListFromString(equation,'->')
	reactives = eq[0]
	products = eq[1]
	print('\treactives: '+ reactives)
	print('\tproducts: ' + products)
	print('-----------------------------')
	print('get individual reactives')
	reactives = getListFromString(reactives,'+')
	for r in reactives:
		print(' ',end=r)
	print('\n\nget individual products')
	products = getListFromString(products,'+')
	for p in products:
		print(' ',end=p)
	print('\n-----------------------------')
	print('getting elements and indexes...')
	print('---reactives')
	reactives = getFormulaElementsFromList(reactives)
	for i in reactives:
		for j in i:
			print(j.__dict__)
	print('\n---products')
	products = getFormulaElementsFromList(products)
	for i in products:
		for j in i:
			print(j.__dict__)
	
	print('-----------------------------')
	print('-----------------------------')
	print('byeee')

def getFormulaArray(formula):
	return list(formula.replace(' ',''))

def getFormulaCoeficient(formula):
	if isinstance(formula,list):
		if formula[0].isdigit():
			return formula[0]		

def getFormulaElements(formula):
	if isinstance(formula,list):
		elements = []
		formulaLength = len(formula)
		index = 0
		while index < formulaLength:
			symbol = ''
			subindex = ''
			coefficient = ''
			# check IF position is UPPERCASE or we are at LAST_ITEM of array
			if formula[index].isupper() and index+1<formulaLength:
				#check IF the NEXT position is LOWERCASE or NUMBER
				if formula[index+1].islower() and index+2<formulaLength:
					#check IF position AFTER_NEXT is NUMBER
					if formula[index+2].isdigit():
						subindex = formula[index+2]
					symbol = formula[index] + formula[index+1]
				else:
					if formula[index+1].isdigit():
						symbol = formula[index]
						subindex = formula[index+1]
			else:
				if formula[index].isupper():
					symbol = formula[index]
			if symbol!='':
				elements.append(FormulaElement(symbol, subindex))
			index+=1
		return elements
	else:
		print('Check inputs for getFormulaElements')

def getListFromString(string,delimiter):
	temp = []
	temp = string.split(delimiter)
	return temp

def getFormulaElementsFromList(lista):
	temp = []
	for l in lista:
		sublist = []
		x = getFormulaElements(getFormulaArray(l))
		for j in x:
			sublist.append(j)
		temp.append(sublist)
	return temp

if __name__ == '__main__':
	main()