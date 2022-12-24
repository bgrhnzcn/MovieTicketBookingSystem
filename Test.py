text = "Example text for search engine."


str.join()

class Test:

    def searchengine(self, text=None):
        self.text = text
        words = text.split()
        text = words[0]
        text = text.join()
        return text

test = Test()
print(test.searchengine(text))