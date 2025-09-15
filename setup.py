
#

from os import path
from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

VERSION = "1.13.9"

setup(
    version=VERSION,
    name="tb-mqtt-client",
    author="IOTPlatform",
    author_email="info@seariiot.io",
    license="Apache Software License (Apache Software License 2.0)",
    description="IOTPlatform python client SDK",
    url="https://github.com/thingsboard/thingsboard-python-client-sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    packages=["."],
    install_requires=['tb-paho-mqtt-client>=2.1.2', 'requests>=2.31.0', 'orjson'])
