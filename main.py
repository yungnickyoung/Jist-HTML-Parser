import requests
import sys
from flask import Flask, request, jsonify, abort, Response
from bcolors import bcolors
import hashlib
import parse_protocol

app = Flask(__name__)

## /parse -- POST
# Required body data: 
#   - domain
#   - article_url (if amp_url is empty)
#   - amp_url
# 
# Returns:
#   - 200: If article was successfully parsed
#   - 400: If request data is missing or invalid
#   - 500: If problem occurs during HTML parsing
@app.route("/parse", methods = ['POST'])
def parseArticle():
    requestData = request.get_json()

    # Validate required data
    try:
        domain = requestData['domain']
        ampUrl = requestData['amp_url']
        desktopUrl = requestData['article_url']
    except KeyError as kerr:
        abort(Response(status=400, response="400: Error(400): Missing or invalid data provided: {}".format(str(kerr))))

    # Extract article text from URL
    try:
        articleText = parse_protocol.parseArticle(domain, ampUrl, desktopUrl)
    except Exception as e:
        abort(Response(status=500, response="500: Error (500): " + str(e)))

    articleHash = hashlib.md5(articleText.encode()).hexdigest()
    data = { 'article_text': articleText, 'article_hash': articleHash }

    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
