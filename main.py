import csv
import sys
from knn import KNN
base     = sys.argv[1]
algoritmo     = sys.argv[2]
training = "./bases/" + base + "-training.csv"
test	 = "./bases/" + base + "-test.csv"

print("Lendo os dados de treino")
with open(training, newline='') as f:
	xtraining = []
	ytraining = []
	reader = csv.reader(f)
	for row in reader:
	    xtraining.append(row[:-1])
	    ytraining.append(row[-1])
print("Arrumando os dados de treino")
for xi, x in enumerate(xtraining):
	if base == "poker":
		xtraining[xi] = [x[0], int(x[1]), x[2], int(x[3]), x[4], int(x[5]), x[6], int(x[7]), x[8], int(x[9])]
	elif base == "velha":
		xtraining[xi] = [int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6]), int(x[7]), int(x[8])]
print("lendo os dados de teste")
with open(test, newline='') as f:
	xtest = []
	ytest = []
	reader = csv.reader(f)
	for row in reader:
	    xtest.append(row[:-1])
	    ytest.append(row[-1])
print("Arrumando os dados de teste")
for xi, x in enumerate(xtest):
	if base == "poker":
		xtest[xi] = [x[0], int(x[1]), x[2], int(x[3]), x[4], int(x[5]), x[6], int(x[7]), x[8], int(x[9])]	 
	elif base == "velha":
		xtest[xi] = [int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6]), int(x[7]), int(x[8])]

print("Classificando com o algoritmo {}".format(algoritmo))
if algoritmo == "KNN":		   
	K = KNN(xtraining, ytraining)

	for x in range(0,25):
		K.classificar(xtest, 2*x + 1)
		print("{}, {}".format(2*x+1, K.efetividade(ytest)))

elif algoritmo == "MLP":
	from sklearn.neural_network import MLPClassifier
	clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
	clf.fit(xtest, ytest)
	MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto', 
	            	beta_1=0.9, beta_2=0.999, early_stopping=False, 
					epsilon=1e-08, hidden_layer_sizes=(5, 2), 
					learning_rate='constant', learning_rate_init=0.001, 
					max_iter=200, momentum=0.9, 
					nesterovs_momentum=True, power_t=0.5, random_state=1, 
					shuffle=True, solver='lbfgs', tol=0.0001, 
					validation_fraction=0.1, verbose=False, warm_start=False)