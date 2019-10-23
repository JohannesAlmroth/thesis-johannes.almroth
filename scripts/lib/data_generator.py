import os
from numpy import arange
from random import randint

def create_linear_data(filename):
	'''
	This function creates & populates a data file with linear data.
	'''
	# Prepare data ranges
	NR_OF_DATA_POINTS = 50
	START_VALUE = randint(0, 1000)
	END_VALUE = randint(0, 1000)
	INCREMENT_SIZE = (END_VALUE - START_VALUE) / NR_OF_DATA_POINTS

	# Generate list of data points
	data_generator = data_gen(START_VALUE, END_VALUE, INCREMENT_SIZE)
	data_list = []
	for i in data_generator:
		data_list.append(i)

	# Write to file
	with open(filename, 'w') as f:
		for data in data_list:
			f.write(str(data) + '\n')

def data_gen(start, stop, inc = 1):
	'''
	Generator function that is basically the range() method
	'''
	if stop < start:
		inc = 0 - abs(inc) # If stop is smaller than start, we need to make sure we use a negative increment
	for x in arange(start, stop, inc):
		yield x
	
def read_file(filename):
	'''
	Reads a file
	'''
	fh = open(filename, 'r')
	print(fh.readlines())
	fh.close()


path = os.getcwd() + '/output/'
f = path + 'linear_data.txt'

create_linear_data(f)
read_file(f)
