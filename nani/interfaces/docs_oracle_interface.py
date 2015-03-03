
class Docs_Oracle:

    def __init__(self):
        self.title = ''
        self.content = []
        self.rating = []

    def analyze_page(self, page, search):
        try:
            title_tag = page.soup.title
            content_tag = page.soup.find(id="PageContent")

            self.title = title_tag.text
            content_merge = ''
            content_merge += content_tag.text+'\n'

            self.content.append(content_merge)
            self.rating.append('NA')
        except:
            print("ERROR in Docs_Oracle")

        return (self.title, self.content, self.rating)

