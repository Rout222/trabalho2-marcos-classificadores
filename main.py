import csv
from knn import KNN
base     = "poker"
training = "./bases/" + base + "-training.csv"
test	 = "./bases/" + base + "-test.csv"

with open(training, newline='') as f:
	xtraining = []
	ytraining = []
	reader = csv.reader(f)
	for row in reader:
	    xtraining.append(row[:-1])
	    ytraining.append(row[-1])

if base == "poker":
	for xi, x in enumerate(xtraining):
		xtraining[xi] = [x[0], int(x[1]), x[2], int(x[3]), x[4], int(x[5]), x[6], int(x[7]), x[8], int(x[9])]

with open(test, newline='') as f:
	xtest = []
	ytest = []
	reader = csv.reader(f)
	for row in reader:
	    xtest.append(row[:-1])
	    ytest.append(row[-1])

if base == "poker":
	for xi, x in enumerate(xtest):
		xtest[xi] = [x[0], int(x[1]), x[2], int(x[3]), x[4], int(x[5]), x[6], int(x[7]), x[8], int(x[9])]	 
		   
K = KNN(xtraining, ytraining)

for x in range(0,25):
	K.classificar(xtest, 2*x + 1)
	print("{}, {}".format(2*x+1, K.efetividade(ytest)))