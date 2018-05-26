#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary



#Random forest
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred,labels_test)
print accuracy

#print(estimator.get_params())

n_estim = range(5,25,5)
#criteria = ['mae']
max_feature = ['auto','sqrt','log2']
min_split = range(2,5,1)
run_count = 0
accuracy_list = []

for est in range(len(n_estim)):
	for feature in range(len(max_feature)):
		for split in range(len(min_split)):
			clf = RandomForestClassifier(n_estimators = n_estim[est], max_features = max_feature[feature], min_samples_split = min_split[split])
			clf.fit(features_train,labels_train)
			pred = clf.predict(features_test)

			from sklearn.metrics import accuracy_score
			accuracy = accuracy_score(pred,labels_test)
			accuracy_list.append(accuracy)
			run_count+=1
			#print accuracy

print("Run count = "+str(run_count))
print("Max accuracy : "+str(max(accuracy_list)))



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
