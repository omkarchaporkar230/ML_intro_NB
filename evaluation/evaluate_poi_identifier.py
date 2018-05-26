#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score

features_train,features_test,labels_train,labels_test=model_selection.train_test_split(features,labels,test_size=0.3,random_state=42)

clf_new=DecisionTreeClassifier()
clf_new.fit(features_train,labels_train)
pred_new=clf_new.predict(features_test)

accuracy_new=accuracy_score(pred_new,labels_test)
print accuracy_new
print len(labels_test)

print pred_new

#If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?
pr=[]
for i in range(29):
    pr.append(0.0)

acc=accuracy_score(pr,labels_test)
print acc

#Look at the predictions of your model and compare them to the true test labels. Do you get any #true positives? (In this case, we define a true positive as a case where both the actual label and #the predicted label are 1)
print pred_new
print labels_test

tp=0
for i in range(len(pred_new)):
    if(pred_new[i]==1.):
	if(labels_test[i]==1.0):
	    tp+=1

print tp


#As you may now see, having imbalanced classes like we have in the Enron dataset (many more non-#POIs than POIs) introduces some special challenges, namely that you can just guess the more common #class label for every point, not a very insightful strategy, and still get pretty good accuracy!
#Precision and recall can help illuminate your performance better. Use the precision_score and #recall_score available in sklearn.metrics to compute those quantities.
#What's the precision?

from sklearn.metrics import precision_score
print precision_score(labels_test,pred_new)

#What's the recall
from sklearn.metrics import recall_score
print recall_score(labels_test,pred_new)

