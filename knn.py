class KNN(object):
	"""docstring for KNN"""
	def __init__(self, x, y):
		super(KNN, self).__init__()
		self.x = x
		self.y = y

	def classificar(self, k):
		for xi1, x1 in enumerate(self.x):
			for xi2, x2 in enumerate(self.x):
				if(xi1 != xi2):
					print(x1)

x = [[1,2,3,4,5], [2,2,2,2,2], [3,3,3,3,3]]
y = [1,0,0]
K = KNN(x, y)
K.classificar(3)
		