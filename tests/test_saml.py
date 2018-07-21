from requests_saml.saml import get_action

def test_get_action():
    string = '<HTML><BODY><FORM METHOD="POST" ACTION="foo"></FORM></BODY></HTML>'
    assert get_action("foobar") == None
    assert get_action(string) == "foo"
