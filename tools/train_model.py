import io
import pickle
import pip
import sys

from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, cross_val_score


def train(code_by_lang, output, min_df=100):
    """Train a LogisticRegression model for classification of code snippets.

    Param `code_by_lang` must point to the following directory structure:

        $code_by_lang >
            $lang1 >
                snippet1
                snippet2
                ...
                snippetM
            $lang2 >
            ...
            $langN >
            ...

    The trained model will then predict a programming language for a given code
    snippet. The classes (i.e. supported programming languages) are effectively
    defined by the directory names in the structure above.

    """

    data = load_files(code_by_lang, encoding='utf-8')
    text_train, y_train = data.data, data.target

    vect = CountVectorizer(min_df=min_df)
    vect.fit(text_train)
    X_train = vect.transform(text_train)

    param_grid = {'C': [0.001, 0.01, 0.1, 1, 10]}
    grid = GridSearchCV(LogisticRegression(solver='sag', multi_class='multinomial'), param_grid, cv=5)
    grid.fit(X_train, y_train)

    payload = {
        'vectorizer': vect,
        'model': grid,
        'versions': [str(r.as_requirement()) for r in pip.get_installed_distributions()],
        'languages': data.get_target_names(),
        'python': sys.version
    }
    with io.open(output, 'wb') as f:
        pickle.dump(payload, f)


if __name__ == '__main__':
    try:
        code_by_lang, output, *rest = sys.argv[1:]
    except IndexError:
        print('Usage: {} <path to code samples> <output path> [min_df]')
        sys.exit(1)

    train()
