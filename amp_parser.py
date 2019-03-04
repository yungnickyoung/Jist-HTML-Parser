from bs4 import BeautifulSoup
import urllib.request

def amp_cnn(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    out_text = []

    # CNN AMP URLs have one of two formats:
    if "amp-cnn-com" in url:
        body_text = soup.find('div', class_='body_text')
        for paragraph in body_text.find_all('p'):
            out_text.append(paragraph.text)
    elif "www-cnn-com" in url:
        for body_div in soup.find_all('div', class_='Paragraph__component'):
            out_text.append(body_div.text)

    return u" ".join(out_text)

def amp_huffingtonpost(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    out_text = []
    for body_div in soup.find_all('div', class_='content-list-component'):
        out_text.append(body_div.text)

    return u" ".join(out_text)

def amp_nytimes(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('article')
    out_text = []

    for paragraph in body_text.find_all('p', class_=['css-1e7dx92', 'e2kc3sl0']):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def get_article_from_foxnews_amp(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='article-body')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def amp_nbcnews(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('article')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def amp_dailymail(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('article', class_='article-text')
    out_text = []

    for paragraph in body_text.find_all('p', class_='mol-para-with-font'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def amp_theguardian(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='content__article-body')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def amp_wsj(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='articleBody')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def amp_abcnews(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='amp-page-body')
    out_text = []

    for paragraph in body_text.find_all('p', itemprop='articleBody'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def amp_bbc(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='main-content')
    out_text = []

    for paragraph in body_text.find_all('p', class_=['amp-o-paragraph', 'amp-o-paragraph--bold']):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def amp_usatoday(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find_all('div', class_='story-container')
    out_text = []

    for div in body_text:
        out_text.append(div.text)

    return u" ".join(out_text)

def amp_latimes(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find_all('div', class_='card-content')
    out_text = []

    for div in body_text:
        try:
            out_text.append(div.text)
        except:
            continue

    return u" ".join(out_text)

def amp_reuters(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
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

def amp_politico(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('article', class_='story-text')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)