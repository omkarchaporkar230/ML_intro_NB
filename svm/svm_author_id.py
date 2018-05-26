# -*- coding: cp1252 -*-
#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

   
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
clf = svm.SVC(C=10000.0, kernel='rbf')
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
clf.fit(features_train,labels_train)

pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(pred,labels_test)
print accuracy

ans10 = pred[50]
print ans10

#total 1700 test events
#How many are predicted to be in Chris or [1] class??

chris=0
var=0
for i in range(1758):
    var = pred[i]
    if (var == 1):
        chris+=1
    else:
        pass

print chris
#########################################################


