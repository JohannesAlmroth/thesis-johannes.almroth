# import matplotlib.pyplot as plt
# pylint: disable=import-error
# pylint: disable=undefined-variable
from uos import urandom

def create_plateu_data(filename):
	PLATEU_LENGTH = 2
	data_list = []
	data_list.extend([100 for i in range(0, PLATEU_LENGTH)])
	data_list.extend([75 for i in range(0, PLATEU_LENGTH)])
	data_list.extend([50 for i in range(0, PLATEU_LENGTH)])
	data_list.extend([25 for i in range(0, PLATEU_LENGTH)])
	data_list.extend([0 for i in range(0, PLATEU_LENGTH)])

	# Write to file
	with open(filename, 'w') as f:
		for data in data_list:
			f.write(str(data) + '\n')

def create_linear_data(filename, fuzzy=False, distorted=False):
	'''
	This function creates & populates a data file with linear data.
	If fuzzy is enabled, every data point will be fuzzed
	If distortion is enabled, some data points will be modified to simulate spikes and crashes
	'''
	# Prepare data ranges
	START_VALUE = 100
	END_VALUE = 0
	INCREMENT_SIZE = -1 #(END_VALUE - START_VALUE) / NR_OF_DATA_POINTS

	# Generate list of data points
	data_list = []
	for i in range(START_VALUE, END_VALUE, INCREMENT_SIZE):
		data = i
		# Fuzzing modifies data by no more than 10% of the value in either direction
		if fuzzy:
			data = fuzz(data)
		# Distortion simulates spikes and crashes
		if distorted:
			data = distort(data)
		data_list.append(data)

	# Write to file
	with open(filename, 'w') as f:
		for data in data_list:
			f.write(str(data) + '\n')


def fuzz(x):
	'''
	Fuzzes a data value
	'''
	return x * uniform(0.9, 1.1)

def distort(x):
	'''
	Distorts data 30% of the time. Used to simulate data spikes and crashes
	'''
	if random() > 0.7: # 30% of data will be distorted
		x = x * uniform(0.3, 2.0)
	return x


def read_file(filename):
	fh = open(filename, 'r')
	data = fh.readlines()
	data = map(str.strip, data)
	data = list(map(float, data))
	# create_graph(data)
	fh.close()


# def create_graph(xdata):
# 	with plt.xkcd():
# 		fig = plt.figure()
# 		ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
# 		ax.spines['right'].set_color('none')
# 		ax.spines['top'].set_color('none')

# 		ax.plot(xdata)
# 		ax.set_ylim(ymin=0) # To start the y-axis from 0

# 		ax.set_xlabel('seconds')
# 		ax.set_ylabel('kilos')
# 		plt.show()