formula='NaClH2O'

def main():
	print('holi')
	print('-----------------------------')
	print('getting elemets from string')
	getStringFormulaElements(formula)
	print('-----------------------------')
	print('byeee')

def getStringFormulaElements(formula):
	elements = []
	stringLength = len(formula)
	index = 0;
	while(index<stringLength):
		element = ''
		char = formula[index]
		nextChar=''
		if index+1<stringLength:
			nextChar=formula[index+1]
			if char.isupper():
				if nextChar.islower():
					element=char+nextChar
					index+=1
		print(str(index)+'\t',end='')
		if element!='':
			print(element)
			elements.append(element)
		else:
			print(char)
		index+=1
	
	return elements


if __name__ == '__main__':
	main()