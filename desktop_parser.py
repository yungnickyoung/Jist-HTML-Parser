from bs4 import BeautifulSoup
import urllib.request
import sys

def desktop_cnn(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    out_text = []

    # Seems like articles have one <p> with text, followed by <div>s with text
    for body_p in soup.find_all('p', class_='zn-body__paragraph'):
        out_text.append(body_p.text)

    for body_div in soup.find_all('div', class_='zn-body__paragraph'):
        out_text.append(body_div.text)

    return u" ".join(out_text)

def desktop_nytimes(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    out_text = []

    for paragraph in soup.find_all('p', class_=['css-1ygdjhk', 'evys1bk0']):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_huffpost(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    out_text = []
    for body_div in soup.find_all('div', class_='yr-content-list-text'):
        out_text.append(body_div.text)

    return u" ".join(out_text)


def desktop_foxnews(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='article-body')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_usatoday(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    out_text = []

    for paragraph in soup.find_all('p', class_='p-text'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_reuters(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='StandardArticleBody_body')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_politico(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='story-text')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_yahoo(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    out_text = []

    for paragraph in soup.find_all('p', class_='canvas-text'):
        upper = paragraph.text.upper()
        if "REPORTING BY" in upper or "WRITING BY" in upper or "THIS ARTICLE" in upper:
            continue

        out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_npr(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Check if article is an audio transcript - we do not want these
    if soup.find_all(class_='transcript'):
        raise Exception("Detected 'transcript' class in article. Article may be an audio transcript.")

    body_text = soup.find_all('div', class_='storytext')
    out_text = []

    for div in body_text:
        for paragraph in div.find_all('p'):
            out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_nbcnews(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='body___2BbXy')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_dailymail(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', itemprop='articleBody')
    out_text = []

    for paragraph in body_text.find_all('p', class_='mol-para-with-font'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_theguardian(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='content__article-body')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)


def desktop_abcnews(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='article-copy')
    out_text = []

    for paragraph in body_text.find_all('p', itemprop='articleBody'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_bbc(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find('div', class_='story-body__inner')
    out_text = []

    for paragraph in body_text.find_all('p'):
        out_text.append(paragraph.text)

    return u" ".join(out_text)

def desktop_latimes(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.find_all('div', class_='card-content')
    out_text = []

    for div in body_text:
        try:
            paragraph = div.find('p')
            out_text.append(paragraph.text)
        except:
            continue

    return u" ".join(out_text)