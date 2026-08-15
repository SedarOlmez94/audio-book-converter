from html.parser import HTMLParser

class HTMLFilter(HTMLParser):
    # Tags that should trigger a line break when they open or close
    block_tags = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "h5", "h6"}

    def __init__(self):
        super().__init__()
        self.text = ""

    def handle_starttag(self, tag, attrs):
        if tag in self.block_tags:
            self.text += "\n"

    def handle_endtag(self, tag):
        if tag in self.block_tags:
            self.text += "\n"

    def handle_data(self, data):
        self.text += data