from setuptools import setup, find_packages

setup(
    name="xbrl-analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "lxml",
    ],
    entry_points={
        'console_scripts': [
            'xbrl-analyzer=cli.main:main',
            'xbrl-db-import=cli.importer:main',
            'xbrl-db-query=cli.db_query:main',
        ],
    },
    python_requires='>=3.6',
)