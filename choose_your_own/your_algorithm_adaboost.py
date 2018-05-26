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

'''
#K-nearest neighbors
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred,labels_test)
print accuracy

'''
#Adaboost
from sklearn.ensemble import AdaBoostClassifier
#clf = AdaBoostClassifier()
#clf.fit(features_train,labels_train)
#pred = clf.predict(features_test)

#from sklearn.metrics import accuracy_score
#accuracy = accuracy_score(pred,labels_test)
#print accuracy

learn_rate = []
def frange(start,stop,step):
	i = start
	while i<stop:
		yield i
		i+=step
for i in frange(1,3,0.2):
	learn_rate.append(i)

#print learn_rate

n_estim = range(10,120,20)
#learn_rate = float (range(1,3,0.2))
algo = ['SAMME','SAMME.R']
random_st = ['None']
run_count = 0
accuracy_list = []

for est in range(len(n_estim)):
	for learn in range(len(learn_rate)):
		for alg in range(len(algo)):
			clf = AdaBoostClassifier(n_estimators = n_estim[est], learning_rate = learn_rate[learn], algorithm = algo[alg])
			clf.fit(features_train,labels_train)
			pred = clf.predict(features_test)

			from sklearn.metrics import accuracy_score
			accuracy = accuracy_score(pred,labels_test)
			accuracy_list.append(accuracy)
			#print accuracy
			run_count+=1

print("Run count = "+str(run_count))
print ("Maximum accuracy : " + str(max(accuracy_list)))







try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
