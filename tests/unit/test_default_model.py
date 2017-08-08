import gzip
import pkg_resources

import pytest

import xpolyglot.prediction as uut


@pytest.fixture(scope='session')
def predictor():
    serialized_model_path = pkg_resources.resource_filename(
        'xpolyglot', 'resources/default.model.gz')

    with gzip.open(serialized_model_path, 'rb') as f:
        return uut.Predictor(f)


def test_smoke_predict(predictor):
    snippet = '''\
#include <stdio.h>

int main()
{
    printf("Hello, World!\n");
}'''

    rv = predictor.predict(snippet)
    assert rv == {'lang': 'C'}


def test_smoke_supported_languages(predictor):
    rv = predictor.languages
    assert isinstance(rv, list)
    assert len(rv) > 0
    assert 'C' in rv
    assert 'C++' in rv
    assert 'Python' in rv
    assert 'Ruby' in rv
    assert 'Haskell' in rv
    assert 'Rust' in rv
    assert 'Go' in rv
    assert 'Clojure' in rv
    assert 'Java' in rv
    assert 'PHP' in rv
