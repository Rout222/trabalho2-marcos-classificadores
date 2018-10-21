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
print(type(xtraining[0][0]))