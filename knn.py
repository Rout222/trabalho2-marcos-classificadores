import math
class KNN(object):
	"""docstring for KNN"""
	def __init__(self, x, y):
		super(KNN, self).__init__()
		self.x = x
		self.y = y

	def calcularDistancia(self, x1, x2):
		resultado = 0
		for x in x1:
			for y in x2:
				resultado += math.pow(x-y, 2)
		return math.sqrt(resultado)
	def classificar(self, k):
		for xi1, x1 in enumerate(self.x):
			respostas = []
			for xi2, x2 in enumerate(self.x):
				if(xi1 != xi2):
					respostas.append([self.calcularDistancia(x1,x2), y[xi2]])
			respostas = sorted(respostas, key=lambda x: x[0], reverse=False)
			respostas = [y[1] for y in respostas]
			respostas = (max(set(respostas), key = respostas.count))
			print(respostas)

x = [[1,2,3,4,5], [2,2,2,2,2], [3,3,3,3,3]]
y = [1,2,2]
K = KNN(x, y)
K.classificar(3)
x = sorted(x, key=lambda x: x[1], reverse=True)
