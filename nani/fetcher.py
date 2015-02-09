import mechanicalsoup
from urllib.parse import urlparse
import traceback
import interfaces

class Fetcher():
	
	def __init__(self):
		self.fetched = [] #turple of (Title, Url)
		self.results = [] #turple of (Question, Answers[*], Ratings[*])

	def fetch_search(self, search, results):
		browser = mechanicalsoup.Browser()
		
		search = ' '.join(search)
		search_page = browser.get("https://google.com/search?q="+search)
		
		search_list = search_page.soup.find_all('h3', class_='r') #make find all when ready
		
		#get the links from the results
		if search_list:
			for item in search_list:
				fixed_url = urlparse(item.parent.a['href'][7:]).geturl().split('&')[0]
				self.fetched.append((item.text,fixed_url))
				#print(urlparse(item.parent.a['href'][7:]).geturl())
			
			for item in self.fetched:
				lookup = urlparse(item[1]).netloc
				lookup = lookup.replace('www.', '')
				lookup = lookup.rsplit('.', 1)[0]
				lookup = lookup.title()
				lookup = lookup.replace('.', '_')

				try:
					interface = eval('interfaces.'+lookup+'()')
					self.results.append(interface.analyze_page(browser.get(item[1])))
		
				except AttributeError:
					print('No Interface OR Incomplete Interface for '+lookup)

				except Exception:
					print(traceback.format_exc())
			
			for item in self.results:
				print('\nQUESTION:')				
				print(item[0] + '\nANSWERS:')
				count = 1
				for post, rating in zip(item[1],item[2]):				
					print('ANSWER '+str(count)+'('+str(rating)+'):\n'+post)
					count += 1
			

	def build_results():
		return "Incomplete"
