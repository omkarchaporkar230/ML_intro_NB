#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    age = []
    net_worth = []
    error = []
    err = []
    tupl = []
    tup_81 = []
    index_81 = []
    value_81 = []
    

    ### your code goes here
    for i in range(90):
    	err.append(net_worths[i]-predictions[i])
	tupl.append([i,float (err[i])])
	
    tupl = sorted(tupl, key = lambda x: float(abs(x[1])), reverse = False)
	
    #print tupl

    for j in range(81):
	tup_81.append(tupl[j])

    for x in tup_81:
	index_81.append(x[0])

    for y in tup_81:
	value_81.append(y[1])

    for k in range(81):
	age.append(ages[index_81[k]])
	net_worth.append(net_worths[index_81[k]])
	error.append(value_81[k])

    #print tup_81
    #for l in range(81):
    cleaned_data = zip(age,net_worth,error)

    print cleaned_data
    
    return cleaned_data

