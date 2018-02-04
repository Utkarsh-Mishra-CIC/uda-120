#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#print enron_data['GLISAN JR BEN F']
#print len(enron_data.keys())+10
count = 0
tot = 0
for key in enron_data.keys():
	if enron_data[key]['poi']:
		tot = tot + 1
		if enron_data[key]['total_payments']=='NaN':
			count = count+1
print tot+10, count + 10
#print enron_data['SKILLING JEFFREY K']['total_payments']
#print enron_data['FASTOW ANDREW S']['total_payments']
#print enron_data['LAY KENNETH L']['total_payments']
#print (100*count)/tot