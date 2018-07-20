requests SAML authentication library
====================================

.. image:: https://travis-ci.org/mscherer/requests-saml.svg?branch=master
    :target: https://travis-ci.org/mscherer/requests-saml

Requests is an HTTP library, written in Python, for human beings. This library
add the support for SAML authentication, with the help of another authentication
module. For example, if your SAML portal use Kerberos, you can use this:

.. code-block:: python

    >>> import requests
    >>> from requests_saml import HTTPSAMLAuth
    >>> from requests_kerberos import HTTPKerberosAuth
    >>> k = HTTPKerberosAuth()
    >>> s = HTTPSAMLAuth(chained_auth=k)
    >>> r = requests.get("http://entreprise.example.org", auth=s)
    ...

The entire ``requests.api`` should be supported.


