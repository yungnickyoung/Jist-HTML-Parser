from bs4 import BeautifulSoup
from bs4.element import Comment

def get_body_text(html, news_source):
    """ Returns the article body text for a given news article html page

    Parses out the article text of an html page for a news site, given the news source.

    Args:
        html: The HTML page of the news article. Can be retrieved with urllib.request.urlopen(%{url}).read()
        news_source: A string indicating the news website the article is taken from.
            Currently supported strings: 'cnn', 'huffingtonpost'

    Returns:
        The plaintext of the news article's body.
    """
    soup = BeautifulSoup(html, 'html.parser')
    article_body = ""
    
    # Scrape article body from html page depending on source site
    if news_source == 'cnn':
        article_body = get_article_from_cnn_amp(soup)
    elif news_source == 'huffingtonpost':
        article_body = get_article_from_huffingtonpost_amp(soup)
    elif news_source == 'nytimes':
        article_body = get_article_from_nytimes_amp(soup)
    elif news_source == 'nbcnews':
        article_body = get_article_from_nbcnews_amp(soup)
    elif news_source == 'dailymail':
        article_body = get_article_from_dailymail_amp(soup)
    elif news_source == 'theguardian':
        article_body = get_article_from_theguardian_amp(soup)
    elif news_source == 'wsj':
        article_body = get_article_from_wsj_amp(soup)
    elif news_source == 'abcnews':
        article_body = get_article_from_abcnews_amp(soup)
    elif news_source == 'bbc':
        article_body = get_article_from_bbc_amp(soup)
    elif news_source == 'usatoday':
        article_body = get_article_from_usatoday_amp(soup)
    elif news_source == 'latimes':
        article_body = get_article_from_latimes_amp(soup)
    elif news_source == 'reuters':
        article_body = get_article_from_reuters_amp(soup)
    elif news_source == 'politico':
        article_body = get_article_from_politico_amp(soup)
    else:
        article_body = 'No parsing function available for domain ' + str(news_source)
    

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
        out_text.append(body_div.text)

    return u" ".join(out_text)

def get_article_from_nytimes_amp(soup):
    body_text = soup.find('article')
    out_text = []

    for paragraph in body_text.find_all('p', class_=['css-1e7dx92', 'e2kc3sl0']):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def get_article_from_foxnews_amp(soup):
    body_text = soup.find('div', class_='article-body')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def get_article_from_nbcnews_amp(soup):
    body_text = soup.find('article')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def get_article_from_dailymail_amp(soup):
    body_text = soup.find('article', class_='article-text')
    out_text = []

    for paragraph in body_text.find_all('p', class_='mol-para-with-font'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def get_article_from_theguardian_amp(soup):
    body_text = soup.find('div', class_='content__article-body')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def get_article_from_wsj_amp(soup):
    body_text = soup.find('div', class_='articleBody')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def get_article_from_abcnews_amp(soup):
    body_text = soup.find('div', class_='amp-page-body')
    out_text = []

    for paragraph in body_text.find_all('p', itemprop='articleBody'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def get_article_from_bbc_amp(soup):
    body_text = soup.find('div', class_='main-content')
    out_text = []

    for paragraph in body_text.find_all('p', class_=['amp-o-paragraph', 'amp-o-paragraph--bold']):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def get_article_from_usatoday_amp(soup):
    body_text = soup.find_all('div', class_='story-container')
    out_text = []

    for div in body_text:
        out_text.append(div.text)

    return u" ".join(out_text)

def get_article_from_latimes_amp(soup):
    body_text = soup.find_all('div', class_='card-content')
    out_text = []

    for div in body_text:
        try:
            out_text.append(div.text)
        except:
            continue

    return u" ".join(out_text)

def get_article_from_reuters_amp(soup):
    body_text = soup.find('div', class_='article-text')
    out_text = []

    for span in body_text.find_all('span', id='articleText'):
        for paragraph in span.find_all('p'):
            try:
                paragraph.span.decompose()
            except:
                pass
            out_text.append(paragraph.text)

    return u" ".join(out_text)

def get_article_from_politico_amp(soup):
    body_text = soup.find('article', class_='story-text')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)
