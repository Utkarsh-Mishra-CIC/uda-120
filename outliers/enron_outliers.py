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
data_dict.pop('LAVORATO JOHN J',0)
data_dict.pop('LAY KENNETH L',0)
data = featureFormat(data_dict, features)

### your code below
li = []
li1= []
for point in data:
    salary = point[0]
    bonus = point[1]
    li1.append(point[0])
    li.append(point[1])
    matplotlib.pyplot.scatter( salary, bonus )
#print li1[40],li[40]
#print li.index(max(li))
for key in data_dict.keys():
	if data_dict[key]['salary']==li1[61]:
		if data_dict[key]['bonus']==li[61]:
			print key
			
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


