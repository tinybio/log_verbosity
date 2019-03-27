import argparse
import logging

"""
I often want to control logging options with a repeated -v[vv, vvv] flag; this works
and I can never remember how I did it.

"""


parse = argparse.ArgumentParser()
parse.add_argument('--verbose', '-v', action='count', dest='log_v', default=0)
args = parse.parse_args()

for level, _ in zip((logging.ERROR, logging.INFO, logging.DEBUG), range(args.log_v + 1)):
	pass

logging.basicConfig(
	level = level,
	stream=sys.stderr
)

