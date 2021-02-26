class Element:
	def __init__(self, symbol, weight):
		self.symbol = symbol
		self.weight = weight

	def serialize(self):
		return { 
		'symbol' : self.symbol,
		'weight' : self.weight
		}

	def getSymbol():
		return self.symbol

	def getWeight():
		return self.weight