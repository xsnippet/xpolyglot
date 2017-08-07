from setuptools import setup, find_packages


setup(
    name='xpolyglot',
    version='0.1',
    description=(
        'xpolyglot is a simple web-service that detects programming '
        'language of code snippets.'
    ),
    license='MIT',
    url='https://github.com/xsnippet/xpolyglot/',
    keywords='web-service restful-api snippet machine-learning',
    author='The XSnippet Team',
    author_email='dev@xsnippet.org',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'falcon',
        'numpy == 1.13.1',
        'scikit-learn == 0.18.2',
        'scipy == 0.19.1',
    ],
    tests_require=[
        'pytest >= 2.8.7',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
