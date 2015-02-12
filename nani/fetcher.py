import mechanicalsoup
from urllib.parse import urlparse
from urllib.parse import quote_plus
import webbrowser
import textwrap
import nani.interfaces

#This class goes of to google and fetches all the results,
#This class also handles creating the classes to handle the websites.
#Also formats the information based on whether a user is focused on an item.
#Handles opening pages when requested.

class Fetcher():
	
	def __init__(self, show_unsupported):
		self.fetched = [] #tuple of (Title, Url)
		self.results = [] #tuple of (Question, Answers[*], Ratings[*])
		self.max_results = 0 #number of results found
		self.unsupported = show_unsupported #toggle to show unsupported sites.

	def fetch_search(self, search, results):
		browser = mechanicalsoup.Browser()
		
		search = ' '.join(search) 
		search = quote_plus(search) #URL encode characters that aren't supported
		search_page = browser.get("https://google.com/search?q="+search)
		
		search_list = search_page.soup.find_all('h3', class_='r') #find each of the results
		
		#get the links from the results
		if search_list:
			for item in search_list:
				if item.parent.a != None:
					parsed_url = urlparse(item.parent.a['href'][7:])
					if parsed_url.netloc != '':
						fixed_url = parsed_url.geturl().split('&')[0]
						self.fetched.append((item.text,fixed_url))
			
			new_fetched = [] #A list of the successful results
			for item in self.fetched:
				lookup = urlparse(item[1]).netloc
				lookup = lookup.replace('www.', '') #neaten the domain name.
				lookup = lookup.rsplit('.', 1)[0]
				lookup = lookup.title()
				lookup = lookup.replace('.', '_')

				try: #dynamically lookup the required class & if no error pass the interface the page.
					interface = eval('nani.interfaces.'+lookup+'()')
					self.results.append(interface.analyze_page(browser.get(item[1]),search))
					new_fetched.append(item)
		
				except AttributeError: 
					if self.unsupported:
						print('No Interface OR Incomplete Interface for '+lookup)
					else:
						pass
					
			self.fetched = new_fetched #replace the fetched list
			self.max_results = len(self.results)
			
	#setup the output.
	def format_output(self, focus=None):
		wrapper = textwrap.TextWrapper() #wrap text and leave whitespace in.
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
	
	#open the currently selected item in the default browser.
	def open_page(self, index):
		webbrowser.open(self.fetched[index][1])
