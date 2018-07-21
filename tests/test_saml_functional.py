import requests
from requests_saml import HTTPSAMLAuth
from pytest_localserver.http import WSGIServer
import pytest


def simple_app(environ, start_response):
    """Simplest possible WSGI application"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    f = "tests/web" + environ['PATH_INFO'][:-1] + ".html"
    r = open(f).read().format(environ['HTTP_HOST'])
    return r


@pytest.fixture
def testserver(request):
    """Defines the testserver funcarg"""
    server = WSGIServer(application=simple_app)
    server.start()
    request.addfinalizer(server.stop)
    return server


def test_saml_auth(testserver):
    saml_auth = HTTPSAMLAuth()
    r = requests.get(testserver.url + "/protected/", auth=saml_auth)
    assert r.status_code == 200
    assert r.text == "You won!!\n"
