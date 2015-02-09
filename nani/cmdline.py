import argparse
from fetcher import Fetcher
import textwrap

def run():
	parser = argparse.ArgumentParser(prog='nani',
					description='A Software Development Question & Answer Aggregator.')
	parser.add_argument('search', type=str, nargs='+',
					help='The question your want to search')
	parser.add_argument('-r', '--results', type=int, default=3,
					help='The number of results to return')
	args = parser.parse_args()
	
	exit = False
	fetch = Fetcher()
	fetch.fetch_search(args.search, args.results)
	focus = None

	exits = ['q','Q','Quit','quit','exit','Exit','done','Done']
	opens = ['o','O','Open','open']
	backs = ['b','B','Back','back']
	helps = ['h','H','Help','help']

	help = '''
Help:\n
===Search List===\n
\t<number> - Select a search result\n
\tquit - Quit the Nani search\n
\t\tAliases: q, quit, exit, done\n
\thelp - This help output\n
\t\tAliases: h, help\n
===Answer List===\n
\topen - Open this page in your default browser\n
\t\tAliases: o, open\n
\tback - Go back to the Search List\n
\t\tAliases: b, back\n'''

	while not exit:
		print(fetch.format_output(focus))
		in_string = input(">")
		if focus != None:
			if in_string in opens:
				fetch.open_page(focus)
			elif in_string in backs:
				focus = None
			elif in_string in exits:
				exit = True
			else:
				print('Unrecognised Command. back OR open')
		else:
			if in_string in helps:
				print(help)
			elif in_string in exits:
				exit = True
			else:
				try:
					focus = int(in_string)
					if focus > fetch.max_results or focus < 1:
						print('No Matching Result!')
						focus = None
					else:
						focus = focus-1
				except:
					print('Unrecognised command, Use help')
					focus = None

run()
