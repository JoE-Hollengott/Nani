
class En_Wikipedia:
	
	def __init__(self):
		self.title = ''
		self.summary = []
		self.refrences = []

	def analyze_page(self, page):
		try:
			title_tag = page.soup.title
			content_tag = page.soup.find(id="mw-content-text")
			refs_tags = page.soup.find_all('span', class_="reference-text")
			
			self.title = title_tag.text.split("&")[0]
			self.summary.append(content_tag.p.text)
			self.refrences.append(len(refs_tags))
		except:
			print("ERROR in EnWikipedia")

		return (self.title, self.summary, self.refrences)
