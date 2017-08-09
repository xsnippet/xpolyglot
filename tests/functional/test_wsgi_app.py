import re
import subprocess

import pytest
import requests


@pytest.fixture(scope='session')
def wsgi_server():
    # rough size of the gunicorn startup message, so that we know it has
    # actually bound the socket and is ready to accept incoming connections
    bufsize = 200

    process = subprocess.Popen(['gunicorn', 'xpolyglot.wsgi:app', '-b', 'localhost:0'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                bufsize=bufsize)
    addr = re.search(r'Listening at: (.*) ', process.stderr.read(bufsize).decode('utf-8')).groups()[0]

    yield addr

    process.terminate()


def test_smoke_predict(wsgi_server):
    sample = '''\
#include <stdio.h>

int main()
{
    printf("Hello, World!\n");
    return 0;
}\n'''

    resp = requests.post(wsgi_server + '/predict',
                         json={'data': sample})

    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json'
    assert resp.json() == {'lang': 'C'}


def test_smoke_supported_languages(wsgi_server):
    resp = requests.get(wsgi_server + '/languages')

    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json'

    content = resp.json()
    assert isinstance(content, list)
    assert len(content) > 0
    assert 'Python' in content
    assert 'C' in content
    assert 'C++' in content
    assert 'Haskell' in content
    assert 'Rust' in content
    assert 'Go' in content
    assert 'Clojure' in content
    assert 'Java' in content
