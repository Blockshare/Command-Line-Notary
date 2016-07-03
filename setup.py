from setuptools import setup

setup(
    name='notarize',
    version='0.1',
    py_modules=['notarize'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        notarize=notarize:cli
    ''',
)
