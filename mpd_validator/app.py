"""
MPD Validator service.

"""

import falcon

from lxml import etree

class MPDs(object):
    """
    Resource to handle MPDs.
    """
    def __init__(self):
        self.schema = ""
        self.schematron = ""

    def on_post(self, request, response):
        """
        Handles POST requests
        """
        if request.content_length:
            mpd = etree.parse(request.stream)
            response.status = falcon.HTTP_200  # This is the default status
        else:
            response.status = falcon.HTTP_400  # This is the default status

# falcon.API instances are callable WSGI apps
APP = falcon.API()

# Resources are represented by long-lived class instances
mpds = MPDs()

# things will handle all requests to the '/things' URL path
APP.add_route('/mpds', mpds)
