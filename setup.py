from setuptools import setup

setup(
    name='notary',
    version='0.1',
    py_modules=['notary'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        notary=notary:cli
    ''',
)
