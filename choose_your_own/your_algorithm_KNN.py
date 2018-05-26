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

#K-nearest neighbors
from sklearn.neighbors import KNeighborsClassifier
#clf = KNeighborsClassifier()
#clf.fit(features_train,labels_train)
#pred = clf.predict(features_test)

#from sklearn.metrics import accuracy_score
#accuracy = accuracy_score(pred,labels_test)
#print accuracy

#Finding max accuracy possible by checking each and every hyperparameter combination
neighbors = range(1,11)
wts = ['uniform','distance']
algo = ['auto','ball_tree','kd_tree','brute']
leaf = range(20,50,10)
run_count = 0
accuracy_list = []
accuracy_max = 0

for neighbrs in range(len(neighbors)):
	for weits in range(len(wts)):
		for alg in range(len(algo)):
			for size in range(len(leaf)):

				clf = KNeighborsClassifier(n_neighbors = neighbors[neighbrs], weights = wts[weits], algorithm = algo[alg], leaf_size = leaf[size])
				clf.fit(features_train,labels_train)
				pred = clf.predict(features_test)
				from sklearn.metrics import accuracy_score
				accuracy = accuracy_score(pred,labels_test)
				accuracy_list.append(accuracy)
				if(accuracy_max < accuracy):
					accuracy_max = accuracy
					#print('Max accuracy run count : '+str(run_count)) 
				#print (str(accuracy)+'\n')
				run_count+=1

print('Run count = '+str(run_count))
print('Max accuracy is : '+str(max(accuracy_list)))

for i in range(run_count):
	if (accuracy_list[i] == max(accuracy_list)):
		print('max accuracy for the run count : '+str(i))

	else:
		pass






try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
