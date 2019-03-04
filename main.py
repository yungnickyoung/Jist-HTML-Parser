import requests
import sys
from flask import Flask, request, jsonify, abort, Response
import parse_protocol
from bcolors import bcolors

app = Flask(__name__)

## /parse -- POST
# Required body data: 
#   - domain
#   - article_url (if amp_url is empty)
#   - amp_url
# 
# Returns:
#   - 200: If article was successfully parsed and summarized
#   - 400: If request data is missing or invalid
#   - 500: If problem occurs during HTML parsing or summarization
@app.route("/parse", methods = ['POST'])
def parseArticle():
    requestData = request.get_json()

    try:
        domain = requestData['domain']
        ampUrl = requestData['amp_url']
        desktopUrl = requestData['article_url']
    except KeyError as kerr:
        abort(Response(status=400, response="400: Error(400): Missing or invalid data provided: {}".format(str(kerr))))

    # print('Retrieved url from domain ' + requestData['domain'] + ': ' + requestData['amp_url'], file=sys.stderr )

    try:
        article_text = parse_protocol.parseArticle(domain, ampUrl, desktopUrl)
    except Exception as e:
        abort(Response(status=500, response="500: Error (500): " + str(e)))

    # app.logger.info('Full text:')
    # app.logger.info(article_text)

    data = { 'full_text': article_text, 'domain': domain }

    resp = requests.post(url="http://jist-summarizer:5002/summarize", json=data) 

    print('Response from summarizer: ' + str(resp.status_code), file=sys.stderr)
    # app.logger.info(resp.json())

    return jsonify(resp.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
