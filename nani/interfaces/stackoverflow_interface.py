
class Stackoverflow:

	def __init__(self):
		self.post_texts = []
		self.post_ratings = []
		
		#use this method to grab all the information from the page and return a turple (Question, Answers[], Ratings[])
	def analyze_page(self, page):

		post_tags = page.soup.find_all('div', class_="post-text")
		vote_tags = page.soup.find_all('span', class_="vote-count-post ")

		for tag in post_tags:
			self.post_texts.append(tag.text)

		for tag in vote_tags:
			self.post_ratings.append(int(tag.text))

		return (self.post_texts[0], self.post_texts[1:], self.post_ratings[1:])
		
