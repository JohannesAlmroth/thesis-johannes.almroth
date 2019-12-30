# import matplotlib.pyplot as plt
# pylint: disable=import-error
# pylint: disable=undefined-variable
# from uos import urandom
from random import random, uniform, choice, randint
from numpy import arange

def add_linear_data(data_list, nr_of_data_points, start_value, end_value):
	inc = (end_value - start_value) / nr_of_data_points
	data_list.extend([i for i in arange(start_value, end_value, inc)])
	return data_list


def create_disconnect_data(filename):
	data = []
	data.extend([100 for i in range(0, 25)])
	data.extend([i for i in range(100, 60, -2)])
	data.extend([60 for i in range(0, 25)])
	data.extend([0 for i in range(0, 25)])

	write_to_file(data, filename)

def create_half_faulty_data(filename):
	data = []
	data.extend([randint(100, 200) for i in range(0, 50)])
	data.extend([i for i in range(75, 25, -1)])

	write_to_file(data, filename)

def create_faulty_data(filename):
	data = []
	data.extend([randint(100, 200) for i in range(0, 100)])

	write_to_file(data, filename)

def create_some_faulty_data(filename):
	data = []
	data.extend([50 for i in range(0, 25)])
	data.extend([randint(100, 200) for i in range(0, 10)])
	data.extend([50 for i in range(0, 25)])
	data.extend([randint(100, 200) for i in range(0, 10)])
	data.extend([50 for i in range(0, 25)])
	data.extend([randint(100, 200) for i in range(0, 10)])
	data.extend([50 for i in range(0, 25)])

	write_to_file(data, filename)

def create_plateu_data(filename):
	PLATEU_LENGTH = 25
	data = []
	data.extend([100 for i in range(0, PLATEU_LENGTH)])
	data.extend([i for i in range(100, 60, -2)])
	data.extend([60 for i in range(0, PLATEU_LENGTH)])
	data.extend([i for i in range(60, 20, -2)])
	data.extend([20 for i in range(0, PLATEU_LENGTH)])

	write_to_file(data, filename)

def create_linear_data(filename, fuzzy=False, distorted=False):
	'''
	This function creates & populates a data file with linear data.
	If fuzzy is enabled, every data point will be fuzzed
	If distortion is enabled, some data points will be modified to simulate spikes and crashes
	'''
	# Prepare data ranges
	START_VALUE = 30
	END_VALUE = 0
	INCREMENT_SIZE = -1 #(END_VALUE - START_VALUE) / NR_OF_DATA_POINTS

	# Generate list of data points
	data = []
	for i in range(START_VALUE, END_VALUE, INCREMENT_SIZE):
		data_point = i
		# Fuzzing modifies data by no more than 10% of the value in either direction
		if fuzzy:
			data_point = fuzz(data_point)
		# Distortion simulates spikes and crashes
		if distorted:
			data_point = distort(data_point)
		data.append(data_point)
	write_to_file(data, filename)

def write_to_file(data, filename):
	with open(filename, 'w') as f:
		for data_point in data:
			f.write(str(data_point) + '\n')


def fuzz(x):
	'''
	Fuzzes a data value
	'''
	return x * uniform(0.8, 1.2)

def distort(x):
	'''
	Distorts data 30% of the time. Used to simulate data spikes and crashes
	'''
	if random() > 0.95: # 30% of data will be distorted
		x = x * uniform(0.3, 2.0)
	return x


def read_file(filename):
	fh = open(filename, 'r')
	data = fh.readlines()
	data = map(str.strip, data)
	data = list(map(float, data))
	create_graph(data)
	fh.close()


# def create_graph(xdata):
# 	with plt.xkcd():
# 		fig = plt.figure()
# 		ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
# 		ax.spines['right'].set_color('none')
# 		ax.spines['top'].set_color('none')

# 		ax.plot(xdata)
# 		ax.set_ylim(ymin=0) # To start the y-axis from 0

# 		ax.set_xlabel('y-axis')
# 		ax.set_ylabel('x-axis')
# 		plt.show()


if __name__ == "__main__":
	from os import getcwd
	from threading import Thread

	path = getcwd() + '/output/'

	# plateu_file = path + 'plateu_data.txt'
	# create_plateu_data(plateu_file)
	# read_file(plateu_file)

	# linear_file = path + 'linear_data.txt'
	# create_linear_data(linear_file, distorted = False, fuzzy = True)
	# read_file(linear_file)

	# half_faulty_file = path + 'half_faulty_data.txt'
	# create_half_faulty_data(half_faulty_file)
	# read_file(half_faulty_file)

	# faulty_file = path + 'faulty_data.txt'
	# create_faulty_data(faulty_file)
	# read_file(faulty_file)

	# some_faulty_file  = path + 'some_faulty_data.txt'
	# create_some_faulty_data(some_faulty_file)
	# read_file(some_faulty_file)

	# disconnect_file = path + 'disconnect_data.txt'
	# create_disconnect_data(disconnect_file)
	# read_file(disconnect_file)