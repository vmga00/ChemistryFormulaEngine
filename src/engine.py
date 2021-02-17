originalFromula = '2NaClH2O'
formula = []

def main():
	print('holi')
	print('-----------------------------')
	print('getting elemets from string')
	formula = getFormulaArray(originalFromula)
	formula = getStringFormulaElements(formula)
	print('-----------------------------')
	print('adding elements subindex')
	#getElementsSubindex(formula)
	print('-----------------------------')
	print('-----------------------------')
	print('-----------------------------')
	print('-----------------------------')
	print('byeee')

def getFormulaArray(formula):
	return list(formula)

def getStringFormulaElements(formula):
	if isinstance(formula, list):
		elements = []
		stringLength = len(formula)
		index = 0
		while index<stringLength:
			element = ''
			char = formula[index]
			nextChar = ''
			if index+1<stringLength:
				 nextChar = formula[index+1]
				 if char.isupper():
				 	if nextChar.islower():
				 		element = char+nextChar
				 		index += 1
			if element!='':
				elements.append(element)
			index += 1
		return elements

if __name__ == '__main__':
	main()