from bs4 import BeautifulSoup
import urllib.request

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