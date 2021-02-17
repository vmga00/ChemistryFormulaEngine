from FormulaElement import *

originalFromula = '2NaClH5O8'
formula = []

def main():
	print('holi')
	print('-----------------------------')
	print('getting elemets from string: '+originalFromula)
	formula = getFormulaArray(originalFromula)
	formula = getFormulaElements(formula)
	for i in formula:
		print(i.__dict__)
	print('-----------------------------')
	print('-----------------------------')
	print('-----------------------------')
	print('-----------------------------')
	print('-----------------------------')
	print('byeee')

def getFormulaArray(formula):
	return list(formula)

def getFormulaCoeficient(formula):
	if isinstance(formula,list):
		if formula[0].isdigit():
			return formula[0]		

def getFormulaElements(formula):
	if isinstance(formula,list):
		elements = []
		formulaLength = len(formula)
		index = 1
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
		print('Check inputs for getElements')

if __name__ == '__main__':
	main()