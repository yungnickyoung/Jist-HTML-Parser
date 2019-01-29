from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import requests
from flask import Flask, request, jsonify
from parse_protocol import get_body_text

app = Flask(__name__)

@app.route("/parse", methods = ['POST'])
def parseArticle():
    req_data = request.get_json()

    app.logger.info('Retrieved url from domain ' + req_data['domain'] + ': ' + req_data['url'] )

    html = urllib.request.urlopen(req_data['url']).read()
    article_text = get_body_text(html, req_data['domain'])

    app.logger.info('Full text:')
    app.logger.info(article_text)

    data = { 'full_text': article_text, 'domain': req_data['domain'] }

    resp = requests.post(url="http://jist-summarizer-container/summarize", json=data) 

    app.logger.info('Response from summarizer: ' + str(resp.status_code))
    app.logger.info(resp.json())

    return jsonify(resp.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
