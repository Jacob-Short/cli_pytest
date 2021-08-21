import sys
import argparse
from typing import Optional, Sequence

def main(argv: Optional[Sequence[str]] = None) -> int:
	# will cause errors if no name is given
	# print(f'Hello Person {sys.argv[1]}')
	parser = argparse.ArgumentParser()
	parser.add_argument('person')
	args = parser.parse_args(argv)

	if args.person == '':
		print("Person's name must not be empty!", file=sys.stderr)
		return 1

	print(f'Hey There Cutie, {args.person}')
	return 0


if __name__ == '__main__':
	sys.exit(main())

