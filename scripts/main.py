# pylint: disable=undefined-variable
# pylint: disable=import-error
RUN_TESTS = True
RUN_PROGRAM = False


# import sqnsupgrade
# sqnsupgrade.run('upgdiff_33080-to-39529.dup', 'updater.elf')


def t(value):
	print("Now sending value", value)
	pybytes.send_signal(2, value)

if RUN_TESTS:
	from test_reader_poll_rate import *
	from test_error_tracker import *
	unittest.main()
if RUN_PROGRAM:
	import reader as re
	r = re.Reader(transmitter=t)
	while True:
		r.run()
