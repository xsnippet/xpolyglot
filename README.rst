=========
xpolyglot
=========

A (micro-) service that detects the programming language the given code snippet
is written in.

API
===

``GET /languages`` - get a list of supported programming languages, e.g.:

.. code-block::

    GET /languages HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Host: localhost:8000
    User-Agent: HTTPie/0.9.9

    HTTP/1.1 200 OK
    Connection: close
    Date: Mon, 07 Aug 2017 19:57:23 GMT
    Server: gunicorn/19.7.1
    content-length: 6908
    content-type: application/json

    [
        "8086-Assembly",
        "ALGOL",
        "ANT",
        "ANTLR",
        "APL",
        "ARM-Assembly",
        "ASP",
        "ASP.Net",
        "ATS",
        "AWK",
        "ActionScript",
    ...


``POST /predict`` - detect the programming language of a given snippet, e.g.:

.. code-block::

    POST /predict HTTP/1.1
    Accept: application/json, */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Content-Length: 102
    Content-Type: application/json
    Host: localhost:8000
    User-Agent: HTTPie/0.9.9

    {
        "data": "#include <stdio.h>\n\nint main()\n{\n    printf(\"Hello, World!\\n\");\n    return 0;\n}\n"
    }

    HTTP/1.1 200 OK
    Connection: close
    Date: Mon, 07 Aug 2017 19:55:41 GMT
    Server: gunicorn/19.7.1
    content-length: 13
    content-type: application/json

    {
        "lang": "C"
    }


Deployment
==========

Model training
==============

* https://github.com/acmeism/RosettaCodeData

Links
=====

* Source: https://github.com/xsnippet/xpolyglot
* Bugs: https://github.com/xsnippet/xpolyglot/issues
