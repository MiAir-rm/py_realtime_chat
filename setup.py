from setuptools import setup,find_packages
import realtime_chat as app

setup(
    name = app.__application__,
    version = app.__version__,
    packages = find_packages(),
    package_data = {
        'app':['']
    },
    author_email = "thisisaspider@gmail.com",
    description = app.__description__,
    url = None,
    entry_points = {
        'console_scripts':[
        ]
    },
    install_requires = [
        'twitcasting-py',
        'websocket_client',
        'chat-downloader' 
    ],
    long_description = open("README.md","r", encoding='utf-8').read(),
    long_description_content_type = "text/markdown",
    python_requires = ">=3.6"
)