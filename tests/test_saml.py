from requests_saml.saml import get_action, get_value


def test_get_action():
    string = """<HTML><BODY><FORM METHOD="POST" ACTION="foo">
    </FORM></BODY></HTML>"""
    assert get_action("foobar") is None
    assert get_action(string) == "foo"


def test_get_value():
    string = """<HTML><BODY>
    <FORM METHOD="POST" ACTION="foo">
    <INPUT NAME="%s" TYPE="HIDDEN" VALUE="bar" />
    </FORM>
    </BODY></HTML>""" % 'SAMLThing'
    assert get_value("foobar", "SAMLThing") is None
    assert get_value(string, "SAMLThing") == "bar"


def test_get_protected_response():
    string = open('tests/web/protected.html').read().format('127.0.0.1')
    assert get_value(string, "SAMLRequest") == "Mi4wOmFzcb3RvY29sL3NhbW+"


def test_get_idp_response():
    string = open('tests/web/idp.html').read().format('127.0.0.1')
    assert get_value(string, "SAMLResponse") == "p0YzpTQUOWIyM2YiIEbnNlPg=="
