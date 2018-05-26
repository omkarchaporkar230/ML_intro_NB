#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)
salary_old = 0
bonus_old = 0

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    if (salary>1000000 and bonus>5000000):
	salary_old=salary
	bonus_old = bonus
    else:
	pass
print ('highest salary : '+str(salary_old)+' bonus : '+str(bonus_old))

for data in data_dict:
    if (data_dict[data]['salary']!='NaN' and data_dict[data]['bonus']!='NaN'):
    	if(int(data_dict[data]['salary'])>int(1000000) and int(data_dict[data]['bonus'])>int(5000000)):
        	print data

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()





