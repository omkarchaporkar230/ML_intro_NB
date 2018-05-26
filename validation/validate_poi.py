#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
clf.fit(features,labels)
pred=clf.predict(features)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(pred,labels)

print accuracy

#Splitting the data into training/testing
from sklearn import model_selection

features_train,features_test,labels_train,labels_test=model_selection.train_test_split(features,labels,test_size=0.3,random_state=42)

clf_new=DecisionTreeClassifier()
clf_new.fit(features_train,labels_train)
pred_new=clf_new.predict(features_test)

accuracy_new=accuracy_score(pred_new,labels_test)
print accuracy_new


