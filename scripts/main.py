# pylint: disable=undefined-variable
# pylint: disable=import-error
RUN_TESTS = True
RUN_PROGRAM = False

# t = pybytes.send_signal

if RUN_TESTS:
	from test_poll_rate import *
	from test_fail_check import *
	unittest.main()
if RUN_PROGRAM:
	import reader as re
	r = re.Reader(transmitter=t)
	while True:
		r.run()
