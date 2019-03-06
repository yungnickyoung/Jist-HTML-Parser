import amp_parser
import desktop_parser

def parseArticle(domain, ampUrl, desktopUrl):
    """ Returns the article body text for a given request

    Args:
        domain: A string indicating the news website's domain, e.g. 'cnn'
        ampUrl: AMP URL for the article (if available)
        desktopUrl: Desktop article URL (if ampUrl is empty)

    Returns:
        The plaintext of the news article's body.
    """

    articleBody = ""
    
    # Scrape article body from html page depending on source site
    try:
        if ampUrl != '':
            url = ampUrl
            if domain == 'cnn':
                articleBody = amp_parser.amp_cnn(url)
            elif domain == 'nytimes':
                articleBody = amp_parser.amp_nytimes(url)
            elif domain == 'huffpost':
                articleBody = amp_parser.amp_huffpost(url)
            elif domain == 'foxnews':
                articleBody = amp_parser.amp_foxnews(url)
            elif domain == 'usatoday':
                articleBody = amp_parser.amp_usatoday(url)
            elif domain == 'reuters':
                articleBody = amp_parser.amp_reuters(url)
            elif domain == 'politico':
                articleBody = amp_parser.amp_politico(url)
            elif domain == 'yahoo':
                articleBody = amp_parser.amp_yahoo(url)
            elif domain == 'nbcnews':
                articleBody = amp_parser.amp_nbcnews(url)
            elif domain == 'dailymail':
                articleBody = amp_parser.amp_dailymail(url)
            elif domain == 'theguardian':
                articleBody = amp_parser.amp_theguardian(url)
            elif domain == 'abcnews':
                articleBody = amp_parser.amp_abcnews(url)
            elif domain == 'bbc':
                articleBody = amp_parser.amp_bbc(url)
            elif domain == 'latimes':
                articleBody = amp_parser.amp_latimes(url)
            # elif domain == 'wsj':
            #     articleBody = amp_parser.amp_wsj(url)
            else:
                raise Exception("No AMP parsing function available for domain {}".format(domain))
        else:
            url = desktopUrl
            if domain == 'cnn':
                articleBody = desktop_parser.desktop_cnn(url)
            elif domain == 'nytimes':
                articleBody = desktop_parser.desktop_nytimes(url)
            elif domain == 'huffpost':
                articleBody = desktop_parser.desktop_huffpost(url)
            elif domain == 'foxnews':
                articleBody = desktop_parser.desktop_foxnews(url)
            elif domain == 'usatoday':
                articleBody = desktop_parser.desktop_usatoday(url)
            elif domain == 'reuters':
                articleBody = desktop_parser.desktop_reuters(url)
            elif domain == 'politico':
                articleBody = desktop_parser.desktop_politico(url)
            elif domain == 'yahoo':
                articleBody = desktop_parser.desktop_yahoo(url)
            elif domain == 'npr':
                articleBody = desktop_parser.desktop_npr(url)
            elif domain == 'nbcnews':
                articleBody = desktop_parser.desktop_nbcnews(url)
            elif domain == 'dailymail':
                articleBody = desktop_parser.desktop_dailymail(url)
            elif domain == 'theguardian':
                articleBody = desktop_parser.desktop_theguardian(url)
            elif domain == 'abcnews':
                articleBody = desktop_parser.desktop_abcnews(url)
            elif domain == 'bbc':
                articleBody = desktop_parser.desktop_bbc(url)
            elif domain == 'latimes':
                articleBody = desktop_parser.desktop_latimes(url)
            else:
                raise Exception("No desktop parsing function available for domain {}".format(domain))
    except Exception as e:
        raise Exception("Error occurred while parsing article from {0}: {1}".format(url, str(e)))

    return articleBody
