# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['morning_digest', 'morning_digest.component']

package_data = \
{'': ['*']}

install_requires = \
['aiodns>=1.1,<2.0',
 'aiohttp>=3.4,<4.0',
 'beautifulsoup4>=4.6,<5.0',
 'cchardet>=2.1,<3.0',
 'click>=7.0,<8.0',
 'jinja2>=2.10,<3.0']

entry_points = \
{'console_scripts': ['digest = morning_digest.cli:main']}

setup_kwargs = {
    'name': 'morning-digest',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'David Buckley',
    'author_email': 'buckley.w.davdid@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
