"""
MPD Validator service.

"""

import falcon

from lxml import etree
from lxml import isoschematron

class MPDs(object):
    """
    Resource to handle MPDs.
    """
    def __init__(self):
        with open("./mpd_validator/schemas/"
                  "DASH-MPD.xsd") as schema_file:
            self.mpd_schema = etree.XMLSchema(etree.parse(schema_file))
        #with open("./mpd_validator/schematrons/"
        #          "schematron.xsd") as schematron_file:
        #    self.mpd_schematron = isoschematron.Schematron(
        #        etree.parse(schematron_file))

    def on_post(self, request, response):
        """
        Handles POST requests
        """
        if request.content_length:
            mpd = etree.parse(request.stream)
            try:
                self.mpd_schema.assert_(mpd)
               # self.mpd_schematron.validate(mpd)
                response.body = "Schema test: OK"
                response.status = falcon.HTTP_200  # This is the default status
            except Exception as error:
                response.status = falcon.HTTP_400
                response.body = error.message
        else:
            response.body = "Empty request"
            response.status = falcon.HTTP_400

# falcon.API instances are callable WSGI apps
application = falcon.API()

# Resources are represented by long-lived class instances
mpds = MPDs()

# things will handle all requests to the '/things' URL path
application.add_route('/mpds', mpds)
