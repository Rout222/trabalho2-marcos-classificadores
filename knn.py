import math
import sys

class KNN(object):

	def __init__(self, x, y):
		super(KNN, self).__init__()
		self.x = x
		self.y = y
		self.yteste = []

	def calcularDistancia(self, x1, x2):
		resultado = 0
		for i in range(0, len(x1)):
			if type(x1[i]) is str:
				resultado += 0 if x1[i] == x2[i] else 2 #se for classe
			else:
				resultado += math.pow(x1[i]-x2[i], 2)
		return math.sqrt(resultado)
		
	def classificar(self, xteste, k):
		self.yteste = []
		respostaFinal = []
		for xi1, x1 in enumerate(xteste):
			respostas = []
			for xi2, x2 in enumerate(self.x):
				respostas.append([self.calcularDistancia(x1,x2), self.y[xi2]])
			respostaX = sorted(respostas, key=lambda x: x[0], reverse=False)[0:k]
			resposta = [sys.maxsize, sys.maxsize]
			aux = []
			for element in respostaX:
				aux.append(element[1])
			respostaFinal.append(max(set(aux), key=aux.count))
		self.yteste = respostaFinal

	def efetividade(self, yteste):
		acertos = 0
		for yi, y in enumerate(yteste):
			if(y == self.yteste[yi]):
				acertos += 1
		return acertos/len(self.yteste)
