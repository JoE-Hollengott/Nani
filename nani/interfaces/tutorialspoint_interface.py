
class Tutorialspoint:

    def __init__(self):
        self.title = ''
        self.content = []
        self.rating = []

    def analyze_page(self, page, search):
        try:
            title_tag = page.soup.title
            content_tags = page.soup.find_all('p')
            code_tags = page.soup.find_all('pre', class_="prettyprint")

            self.title = title_tag.text
            content_merge = ''
            for tag in content_tags:
                content_merge += tag.text+'\n'

            if len(code_tags) > 0:
                content_merge += '\n\n--FOUND CODE--\n==============\n'
                for tag in code_tags:
                    content_merge += tag.text
            self.content.append(content_merge)
            self.rating.append('NA')
        except:
            print("ERROR in Tutorialspoint")

        return (self.title, self.content, self.rating)

