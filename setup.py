from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='esu',
      version='3.0.0',
      description='Enjoy the flexibility of structs with esu!',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/torokmark/esu',
      author='Mark Torok',
      license='Apache License 2.0',
      packages=['esu'],
      test_suite='nose.collector',
      tests_require=['nose'],
      python_requires='>=3.5',
      classifiers=[
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      entry_points = {
          'console_scripts': ['esu-bin=esu.command_line:main'],
      },
      project_urls={
        'Documentation': 'https://esu.readthedocs.io',
        'Source': 'https://github.com/torokmark/esu',
      }
    )
