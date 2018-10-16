import math
import sys

class KNN(object):

	def __init__(self, x, y):
		super(KNN, self).__init__()
		self.x = x
		self.y = y

	def calcularDistancia(self, x1, x2):
		resultado = 0
		for i in range(0, len(x1)):
			if type(x1[i]) is str:
				resultado += 0 if x1[i] == x2[i] else 2 #se for classe
			else:
				resultado += math.pow(x1[i]-x2[i], 2)
		return math.sqrt(resultado)
		
	def classificar(self, k):
		respostaFinal = []
		for xi1, x1 in enumerate(self.x):
			respostas = []
			for xi2, x2 in enumerate(self.x):
				if(xi1 != xi2):
					respostas.append([self.calcularDistancia(x1,x2), y[xi2]])
			respostaX = sorted(respostas, key=lambda x: x[0], reverse=False)
			resposta = [sys.maxsize, sys.maxsize]
			for element in respostaX:
				if(element[0] < resposta[0]):
					resposta = element
			respostaFinal.append(resposta[1])
		return respostaFinal
x = [[1,2,3,4,5], [2,2,2,2,2], [3,3,3,3,3]]
y = [1,2,1]
K = KNN(x, y)
print(K.classificar(3))