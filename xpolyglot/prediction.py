import pickle


class Predictor:
    """A wrapper around serialized models for making language predictions."""

    def __init__(self, serialized_model):
        if isinstance(serialized_model, bytes):
            data = pickle.loads(serialized_model)
        else:
            data = pickle.load(serialized_model)

        # TODO: check versions of the libs

        self._vectorizer = data['vectorizer']
        self._model = data['model']
        self._versions = data['versions']
        self.languages = data['languages']

    def predict(self, snippet):
        """Predict programming language given a code snippet."""

        x = self._vectorizer.transform([snippet])
        return {'lang': self.languages[self._model.predict(x)[0]]}
