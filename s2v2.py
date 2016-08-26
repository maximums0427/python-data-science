from s2v1 import *

def num_of_records(data_sample):
	return len(data_sample)

number_of_ties = num_of_records(data_from_csv)

print 'There are {} ties.'.format(number_of_ties)