import argparse
import logging
import sys

"""
I often want to control logging options with a repeated -v[vv, vvv] flag; this works
and I can never remember how I did it.

The use of zip and range ensures a maximum log level no matter how many 'v's you provide.

"""


parse = argparse.ArgumentParser()
parse.add_argument('--verbose', '-v', action='count', dest='log_v', default=0)
args = parse.parse_args()

for level, _ in zip((logging.CRITICAL, logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG), range(args.log_v + 1)):
	pass

logging.basicConfig(
	level = level,
	stream=sys.stderr
)

print("log level", level)

