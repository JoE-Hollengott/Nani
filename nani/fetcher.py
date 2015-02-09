import mechanicalsoup
from urllib.parse import urlparse
import webbrowser
import textwrap
import interfaces

class Fetcher():
	
	def __init__(self):
		self.fetched = [] #turple of (Title, Url)
		self.results = [] #turple of (Question, Answers[*], Ratings[*])
		self.max_results = 0

	def fetch_search(self, search, results):
		browser = mechanicalsoup.Browser()
		
		search = ' '.join(search)
		search_page = browser.get("https://google.com/search?q="+search)
		
		search_list = search_page.soup.find_all('h3', class_='r') #make find all when ready
		
		#get the links from the results
		if search_list:
			for item in search_list:
				if item.parent.a != None:
					parsed_url = urlparse(item.parent.a['href'][7:])
					if parsed_url.netloc != '':
						fixed_url = parsed_url.geturl().split('&')[0]
						self.fetched.append((item.text,fixed_url))
						#print(urlparse(item.parent.a['href'][7:]).geturl())
			
			new_fetched = []
			for item in self.fetched:
				lookup = urlparse(item[1]).netloc
				lookup = lookup.replace('www.', '')
				lookup = lookup.rsplit('.', 1)[0]
				lookup = lookup.title()
				lookup = lookup.replace('.', '_')

				try:
					interface = eval('interfaces.'+lookup+'()')
					self.results.append(interface.analyze_page(browser.get(item[1])))
					new_fetched.append(item)
		
				except AttributeError:
					print('No Interface OR Incomplete Interface for '+lookup)
					
			self.fetched = new_fetched
			self.max_results = len(self.results)
			

	def format_output(self, focus=None):
		wrapper = textwrap.TextWrapper()
		wrapper.width = 70
		wrapper.replace_whitespace = False
		output = '\n'
		if focus == None:
			count = 1
			for search_item in self.fetched:
				output += '[+] '+str(count)+'. '+search_item[0]+'\n'
				output += ' - '+search_item[1]+'\n\n'
				count += 1
		else:
			item = self.results[focus]
			output += '\n[*] QUESTION:\n'				
			output += item[0] + '\n[*] ANSWERS:\n'
			count = 1
			for post, rating in zip(item[1],item[2]):				
				output += '[+] ANSWER '+str(count)+' Rating('+str(rating)+'):\n'+wrapper.fill(post)+'\n'
				count += 1

		return output

	def open_page(self, index):
		webbrowser.open(self.fetched[index][1])
