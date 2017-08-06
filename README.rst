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

    HTTP/1.0 200 OK
    Date: Sun, 06 Aug 2017 15:37:57 GMT
    Server: WSGIServer/0.2 CPython/3.6.2
    content-length: 8214
    content-type: application/json

    "[\"0815\", \"360-Assembly\", \"4D\", \"4DOS-Batch\", \"6502-Assembly\", \"6800-Assembly\", \"68000-Assembly\", \"8-1-2\",
    \"80386-Assembly\", \"8051-Assembly\", \"8080-Assembly\", \"8086-Assembly\", \"8th\", \"A+\", \"ABAP\", \"ACL2\", \"ALGOL\",
    \"ALGOL-60\", \"ALGOL-68\", \"ALGOL-W\", \"AMPL\", \"ANT\", \"ANTLR\", \"APL\", \"ARM-Assembly\", \"ASP\", \"ASP.Net\",
    \"ATS\", \"AWK\", \"ActionScript\", \"Ada\" ...


``POST /predict`` - detect the programming language of a given snippet, e.g.:

.. code-block::

    POST /predict HTTP/1.1
    Accept: application/json, */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Content-Length: 478
    Content-Type: application/json
    Host: localhost:8000
    User-Agent: HTTPie/0.9.9

    {
        "data": "#include <stdio.h>\n\n\nconst size_t SIZE = 65536;\n\n\nint main(int argc, char **argv)
        {\n    char buf[65536];\n    size_t counts[256];\n\n    FILE* f = fopen(argv[1], \"rb\");\n\n
        size_t read_bytes = fread(buf, 1, SIZE, f);\n    while (read_bytes != 0) {\n
        for (size_t i = 0; i < read_bytes; ++i) {\n            counts[(unsigned char) buf[i]] += 1;\n
        }\n\n        read_bytes = fread(buf, 1, SIZE, f);\n    }\n\n    fclose(f);\n\n    return 0;\n}\n"
    }

    HTTP/1.0 200 OK
    Date: Sun, 06 Aug 2017 15:33:44 GMT
    Server: WSGIServer/0.2 CPython/3.6.2
    content-length: 19
    content-type: application/json

    "{\"lang\": \"C\"}"


Deployment
==========

Model training
==============

* https://github.com/acmeism/RosettaCodeData

Links
=====

* Source: https://github.com/xsnippet/xpolyglot
* Bugs: https://github.com/xsnippet/xpolyglot/issues
