import argparse

def run():
	parser = argparse.ArgumentParser(prog='nani',
					description='A Software Development Question & Answer Aggregator.')
	parser.add_argument('search', type=str, nargs='+',
					help='The question your want to search')
	parser.add_argument('-r', '--results', type=int, default=3,
					help='The number of results to return')
	args = parser.parse_args()
	
	