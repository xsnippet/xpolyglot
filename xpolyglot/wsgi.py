import json
import os
import pkg_resources
import threading

import falcon

from . import prediction


class Application(falcon.API):

    _LOCAL = threading.local()

    @property
    def predictor(self):
        """Lazily initialize a Predictor instance.

        Instances are cached per thread of execution to prevent possible races
        on concurrent predictions.

        XPOLYGLOT_SERIALIZED_MODEL environment variable can be used to choose
        a different trained model. If not set, the default model shipped with
        xpolyglot will be used.

        """

        try:
            return self._LOCAL.predictor
        except AttributeError:
            serialized_model_path = os.environ.get(
                'XPOLYGLOT_SERIALIZED_MODEL',
                pkg_resources.resource_filename('xpolyglot', 'default.model')
            )
            with open(serialized_model_path, 'rb') as f:
                self._LOCAL.predictor = prediction.Predictor(f)

            return self._LOCAL.predictor


app = Application()


class PredictionResource:

    def on_post(self, req, resp):
        """Predict the programming language for a given code snippet."""

        try:
            snippet = json.load(req.stream)['data']
        except (ValueError, KeyError, TypeError):
            resp.status = falcon.HTTP_400
            resp.content_type = 'application/json'
            resp.body = json.dumps(
                {'message': ('request must be a JSON document with field '
                             '`data` pointing to the code snippet')}
            )
            return

        resp.body = json.dumps(app.predictor.predict(snippet))
        resp.status = falcon.HTTP_200
        resp.content_type = 'application/json'


class SupportedLanguagesResource:

    def on_get(self, req, resp):
        """Return a list of supported programming languages."""

        resp.body = json.dumps(app.predictor.languages)
        resp.status = falcon.HTTP_200
        resp.content_type = 'application/json'


app.add_route('/languages', SupportedLanguagesResource())
app.add_route('/predict', PredictionResource())
