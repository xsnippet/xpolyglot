import io
import json
import os
import pkg_resources
import threading

import hug

from . import prediction


XPOLYGLOT_SERIAZLIZED_MODEL = os.environ.get(
    'XPOLYGLOT_SERIAZLIZED_MODEL',
    pkg_resources.resource_filename('xpolyglot', 'default.model')
)
_LOCAL = threading.local()


@hug.directive()
def predictor(**kwargs):
    """Return an initialized Predictor (cached per thread)."""

    try:
        return _LOCAL.predictor
    except AttributeError:
        with io.open(XPOLYGLOT_SERIAZLIZED_MODEL, 'rb') as f:
            _LOCAL.predictor = prediction.Predictor(f)

        return _LOCAL.predictor


@hug.post('/predict')
def predict(body, hug_predictor, versions=1):
    """Predict the programming language of a given code snippet."""

    return json.dumps(hug_predictor.predict(body['data']))


@hug.get('/languages')
def supported_languages(hug_predictor, response, versions=1):
    """Return a list of known programming languages."""

    return json.dumps(hug_predictor.languages)
