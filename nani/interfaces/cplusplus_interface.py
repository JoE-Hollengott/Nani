
class Cplusplus:

	def __init__(self):
		self.tut_page = ''
		self.post_texts = []
		self.post_ratings = []
		
		#use this method to grab all the information from the page and return a turple (Question, Answers[], Ratings[])
	def analyze_page(self, page, search):
		title = page.soup.title.text
		if title.endswith('Forum'):
			try:
				post_tags = page.soup.find_all('div', class_="dwhat")
			
				max_posts = 5
				current = 1
				for tag in post_tags:
					self.post_texts.append(tag.text)
					self.post_ratings.append('NA')
					current +=  1
					if current > max_posts:
						break
			except:
				print("ERROR in Cplusplus (Forum)")
			
			return (self.post_texts[0], self.post_texts[1:], self.post_ratings)
			
		else:
			try:
				section_tags = page.soup.find_all('section')
				self.tut_page = page.soup.find('h1').text
				search_terms = search.split('+')
				for tag in section_tags:
					if tag['id'] in search_terms:
						self.post_texts.append(tag.text)
						self.post_ratings.append('NA')
			except:			
				print("ERROR in Cplusplus (Tutorials)")

			return (self.tut_page, self.post_texts, self.post_ratings)
