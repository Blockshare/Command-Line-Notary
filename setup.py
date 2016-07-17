from setuptools import setup

setup(
    name='notary21',
    version='0.1',
    py_modules=['notary21'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        notary21=notary21:cli
    ''',
)
