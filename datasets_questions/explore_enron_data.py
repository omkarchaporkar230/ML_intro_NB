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
count=0
poi=0
sal=0
slry=0
em=0
email=0

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print enron_data
enron = str(enron_data)
count = enron.count(': {')
poi = enron.count("'poi': True")


#for enron in enron_data:
#	if (str(enron) == ': {'):
#		count+=1

print count
print poi


#What is the total value of the stock belonging to James Prentice?
eso = (enron_data["PRENTICE JAMES"]["exercised_stock_options"])
rs = (enron_data["PRENTICE JAMES"]["restricted_stock"])
rsd = (enron_data["PRENTICE JAMES"]["restricted_stock_deferred"])

print(eso+rs)
print(rsd)

#How many email messages do we have from Wesley Colwell to persons of interest?
print (enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

#What is the value of stock options exercised by Jeffrey K Skilling?
print (enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

#Total payments
print (enron_data["SKILLING JEFFREY K"]["total_payments"])
print (enron_data["LAY KENNETH L"]["total_payments"])
print (enron_data["FASTOW ANDREW S"]["total_payments"])



#How many folks in this dataset have a quantified salary? What about a known email address?
sal = enron.count("'salary': 'NaN'")
slry = count - sal
print ('Number of people having quatified salary = '+str(slry))

em = enron.count("'email_address': 'NaN'")
email = count - em
print ('Number of people having quatified email = '+str(email))

#How many people in the E+F dataset (as it currently exists) have "NaN" for their total payments? What percentage of people in the dataset as a whole is this?
tp=0
count=0
count = enron.count(': {')
print count
percentage = float (0)
tp = enron.count("'total_payments': 'NaN'")
print("Total payments as NaN = "+str(tp))
percentage = float (float(tp)/float(count))*100
print("Percentage of people having NaN as total_payments = "+str(percentage)+"%")

#How many POIs in the E+F dataset have "NaN" for their total payments? What percentage of POI's as a whole is this? 
#poi_tp = enron.count("'total_payments': 'NaN'"&&"'poi': True")
#string = "'total_payments': 'NaN'"
#for string in enron_data:
#print poi_tp
poi_tp=0	
print ('####################################################################')
for enron in enron_data:
	print enron
	print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	#print enron_data[enron]["total_payments"]
	#if (str(enron_data[enron]["total_payments"])=='NaN'):
		
	if (str(enron_data[enron]["poi"])=='True'):
		poi_tp+=1

print poi_tp

#Finding max and min values of exercised stock options
ESO_max=0

for enron in enron_data:
    if(enron_data[enron]["exercised_stock_options"]!='NaN'):
        if(ESO_max<enron_data[enron]["exercised_stock_options"]):
	    ESO_max=enron_data[enron]["exercised_stock_options"]
ESO_min=ESO_max
for enron in enron_data:
    if(enron_data[enron]["exercised_stock_options"]!='NaN'):
        if(ESO_min>enron_data[enron]["exercised_stock_options"]):
	    ESO_min=enron_data[enron]["exercised_stock_options"]

print('max ESO = '+str(ESO_max))
print('min ESO = '+str(ESO_min))
