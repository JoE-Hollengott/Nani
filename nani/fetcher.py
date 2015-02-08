import mechanicalsoup

class Fetcher():

	def fetch_search(search, results):
		browser = mechanicalsoup.Browser()
		
		results_page = browser.get("https://google.com/search?q="+search)
		
		results_list = results_page.soup.find('h3', class_='r')

		if results_list:
			for res in results_list:
				print(res)
