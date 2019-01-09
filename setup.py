from setuptools import setup

setup(
    name='pynpr',
    version='0.2',
    packages=['pynpr'],
    url='https://github.com/JarbasAl/pynpr',
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='unofficial NPR api',
    install_requires=["requests", "bs4", "feedparser", "algoliasearch"],
    keywords='public, radio, stream, metadata, api, service, npr'
)
