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
