# pylint: disable=undefined-variable
# pylint: disable=import-error
RUN_TESTS = False
RUN_PROGRAM = True

t = pybytes.send_signal

if RUN_TESTS:
	from test_read_rate import *
	unittest.main()
if RUN_PROGRAM:
	import reader as re
	r = re.Reader(transmitter=t)
	while True:
		r.run()
