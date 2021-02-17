class FormulaElement:
	def __init__(self, symbol, subindex=None, coefficient=None):
		self.symbol = symbol
		self.subindex = subindex
		self.coefficient = coefficient

	def serialize(self):
		return {
			'symbol': self.symbol,
			'subindex': self.subindex,
			'coefficient': self.coefficient
		}
	def getSymbol(self):
		return self.symbol
	
	def getSubindex(self):
		return self.subindex
	
	def getCoefficient(self):
		return self.coefficient

	def setSubindex(self, subindex):
		self.subindex = subindex

	def setCofficient(self, coefficient):
		self.coefficient = coefficient
