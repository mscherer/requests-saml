# code under the general public license v3 or above
# (c) 2018 Michael Scherer <mscherer@redhat.com>

from requests.auth import AuthBase
import requests

import xml.etree.ElementTree as ET


def get_action(text):
    try:
        return ET.fromstring(text).findall("./BODY/FORM[@METHOD='POST'][@ACTION][1]")[0].attrib['ACTION']  # noqa: E501
    except ET.ParseError:
        return None


def get_value(text, value):
    try:
        e = ET.fromstring(text).findall("./BODY/FORM[@METHOD='POST'][@ACTION][0]/INPUT[@NAME='%s'][@TYPE='HIDDEN'][@VALUE][0]" % value)  # noqa: E501
    except ET.ParseError:
        return None

    return e[0].attrib['VALUE']


class HTTPSAMLAuth(AuthBase):

    def __init__(self, chained_auth=None):
        self.chained_auth = chained_auth

    def handle_response(self, response, **kwargs):
        c = response.cookies
        history = [response]

        v = get_value(response.text, 'SAMLRequest')
        if not v:
            return response

        r = requests.post(get_action(response.text),
                          data={"SAMLRequest": v},
                          auth=self.chained_auth)
        history.append(r)

        v = get_value(r.text, 'SAMLResponse')
        if not v:
            return r

        r = requests.post(get_action(r.text),
                          cookies=c,
                          data={"SAMLResponse": v})
        history.append(r)
        r.history = history

        return r

    def __call__(self, request):
        request.register_hook('response', self.handle_response)
        return request
