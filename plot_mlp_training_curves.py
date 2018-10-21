import csv
import sys
from knn import KNN
base     = "poker"
training = "./bases/" + base + "-training.csv"
test   = "./bases/" + base + "-test.csv"

with open(training, newline='') as f:
  xtraining = []
  ytraining = []
  reader = csv.reader(f)
  for row in reader:
      xtraining.append(row[:-1])
      ytraining.append(row[-1])

for xi, x in enumerate(xtraining):
  if base == "poker":
    xtraining[xi] = [int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6]), int(x[7]), int(x[8]), int(x[9])]
    ytraining[xi] = int(ytraining[xi])
  elif base == "velha":
    xtraining[xi] = [int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6]), int(x[7]), int(x[8])]
    ytraining[xi] = int(ytraining[xi])

with open(test, newline='') as f:
  xtest = []
  ytest = []
  reader = csv.reader(f)
  for row in reader:
      xtest.append(row[:-1])
      ytest.append(row[-1])

for xi, x in enumerate(xtest):
  if base == "poker":
    xtest[xi] = [int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6]), int(x[7]), int(x[8]), int(x[9])]
    ytest[xi] = int(ytest[xi])
  elif base == "velha":
    xtest[xi] = [int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6]), int(x[7]), int(x[8])]
    ytest[xi] = int(ytest[xi])

from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
nb = [GaussianNB(), MultinomialNB(), BernoulliNB()]
for x in nb:
  y_pred = x.fit(xtraining, ytraining).predict(xtest)

  print((ytest != y_pred).sum()/len(ytest))