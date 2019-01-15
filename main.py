from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def article_text(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)

    visible_texts = filter(tag_visible, texts)
    article_match = soup.findAll("div", {"class" : "1-full-width"})
    
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen('https://amp-cnn-com.cdn.ampproject.org/c/s/amp.cnn.com/cnn/uk/live-news/brexit-theresa-may-deal-vote-gbr-intl/index.html').read()

print(article_text(html))
