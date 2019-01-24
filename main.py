from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import requests
from flask import Flask
from flask import request

app = Flask(__name__)

# Overarching function for getting the text of an article
# Currently upported news sources: 'cnn', 'huffingtonpost'
def get_body_text(html, news_source):
    soup = BeautifulSoup(html, 'html.parser')
    article_body = ""
    
    # Scrape article body from html page depending on source site
    if news_source == 'cnn':
        article_body = get_article_from_cnn_amp(soup)
    elif news_source == 'huffingtonpost':
        article_body = get_article_from_huffingtonpost_amp(soup)

    return article_body


def get_article_from_cnn_amp(soup):
    body_text = soup.find('div', class_='body_text')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)


def get_article_from_huffingtonpost_amp(soup):
    out_text = []
    for body_div in soup.find_all('div', class_='content-list-component'):
        #print(body_div)
        out_text.append(body_div.text)

    return u" ".join(out_text)

@app.route("/parse", methods = ['POST'])
def parseArticle():
    app.logger.info("Parse Request: " + str(request.form))

    html = urllib.request.urlopen(request.form.get('url')).read()
    article = get_body_text(html, request.form.get('domain'))

    app.logger.info(article)

    requests.get(url = "http://jist-summarizer-container/summarize", data = article.encode("utf-8")) 

    return "200"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    #html = urllib.request.urlopen('https://amp-cnn-com.cdn.ampproject.org/c/s/amp.cnn.com/cnn/2019/01/23/politics/donald-trump-nancy-pelosi-government-shutdown-congress/index.html').read()
    #cnn_article = get_body_text(html, 'cnn')
    #print(cnn_article)

    #html = urllib.request.urlopen('https://m-huffpost-com.cdn.ampproject.org/c/s/m.huffpost.com/us/entry/us_5c47ecdee4b025aa26be2799/amp').read()
    #huffpost_article = get_body_text(html, 'huffingtonpost')
    #print(huffpost_article)

    # The container for this app must be on the same docker network as the container for the summarizer service.
    # Furthermore, the summarizer container/service must have the name "jist-summarizer-container"
    #requests.get(url = "http://jist-summarizer-container/summarize", data = cnn_article.encode("utf-8")) 
    #requests.get(url = "http://jist-summarizer-container/summarize", data = huffpost_article.encode("utf-8")) 
