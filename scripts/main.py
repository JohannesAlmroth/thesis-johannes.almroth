# pylint: disable=import-error
# pylint: disable=undefined-variable
from utime import sleep
from basic import FIFO
from data_generator import create_linear_data, create_plateu_data
import _thread
# TODO: Include failure for too many extremes
# TODO: Include failure for disconnection of the scale

# A value we expect to never read, motivated by that the scale doesn't have the capacity for it
MAX_READING_VALUE = 200
MIN_READING_VALUE = 0  # A value we are sure the scale will never dip below, realistically
MAX_READING_DELAY = 1   # The max amount of time allowed between readings
MIN_READING_DELAY = 0.5  # The minimum amount of time allowed between delay
READING_DELAY_INC = 0.5  # The increments in which reading delay is allowed to move in
DELTA_THRESHOLD = 8  # The delta value determined to increase or decrease reading delay
RECENT_FAILURE = False
GRACE_PERIOD = True


reading_delay = 1

def read_data(f):

	short_term_buffer = FIFO(maxlen = 2)
	stream = reading(f)

	while True:
		data = float(next(stream).strip())  # Convert from String to float
		short_term_buffer.add(data)
		pybytes.send_signal(2, data)
		modify_reading_delay(short_term_buffer.queue)
		sleep(reading_delay)


def increase_delay():
	global reading_delay
	if reading_delay < MAX_READING_DELAY:
		reading_delay += READING_DELAY_INC


def decrease_delay():
	global reading_delay
	if reading_delay > MIN_READING_DELAY:
		reading_delay -= READING_DELAY_INC


def reading(f):
	for data in open(f, 'r'):
		yield data


def is_valid(value):
	return value < MAX_READING_VALUE and value > MIN_READING_VALUE


def rinse_extremes(buffer):
	crude_list = [x for x in buffer if is_valid(x)]
	difference = len(buffer) - len(crude_list)
	if difference / len(buffer) > 0.3:
		raise_error()
	return crude_list


def total_delta(l):
	prev = l[0]
	total_delta = 0
	for x in l[1:]:
		new_delta = prev - x
		total_delta += new_delta
		x = prev
	return total_delta



def failure_detection(l):
	# TODO: Add timer thread that modifies GRACE_PERIOD
	# TODO: Add global failure count
	# TODO: Add check for 0.0 if jump is too big
	if not failure_check(l): return

	global GRACE_PERIOD
	if RECENT_FAILURE and not GRACE_PERIOD:
		increase_fail_rate()
	if RECENT_FAILURE:
		GRACE_PERIOD = False


def modify_reading_delay(buffer):
	'''
	Purpose of this function is to modify reading_delay depending on the delta produced when comparing the values in the short term buffer.
	'''
	print(buffer)
	crude_list = rinse_extremes(buffer)
	delta = total_delta(crude_list)
	if abs(delta) > DELTA_THRESHOLD:
		decrease_delay()
		pybytes.send_signal(3, "Reading speed decreased")
	else:
		increase_delay()
		pybytes.send_signal(3, "Reading speed increased")

f = 'plateu_data.txt'
create_plateu_data(f)
read_data(f)
