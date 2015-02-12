
class Stackoverflow:

	def __init__(self):
		self.post_texts = []
		self.post_ratings = []
		
	#use this method to grab all the information from the page and return a tuple (Question, Answers[], Ratings[])
	def analyze_page(self, page, search):
		try:
			post_tags = page.soup.find_all('div', class_="post-text")
			vote_tags = page.soup.find_all('span', class_="vote-count-post ")

			for tag in post_tags:
				self.post_texts.append(tag.text)

			for tag in vote_tags:
				self.post_ratings.append(int(tag.text))
		except:
			print("ERROR in Stackoverflow")

		return (self.post_texts[0], self.post_texts[1:], self.post_ratings[1:])
		
