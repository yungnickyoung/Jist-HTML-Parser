from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import requests


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

    article_match = soup.findAll("div", class_="1-full-width")
    
    return u" ".join(t.strip() for t in visible_texts)

def get_article_from_cnn_amp(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_="body_text")

    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

html = urllib.request.urlopen('https://amp-cnn-com.cdn.ampproject.org/c/s/amp.cnn.com/cnn/2019/01/23/politics/donald-trump-nancy-pelosi-government-shutdown-congress/index.html').read()

# print(article_text(html))
print(get_article_from_cnn_amp(html))

# The container for this app must be on the same docker network as the container for the summarizer service.
# Furthermore, the summarizer container/service must have the name "jist-summarizer-container"
requests.get(url = "http://jist-summarizer-container/summarize", data = article_text(html).encode("utf-8")) 
