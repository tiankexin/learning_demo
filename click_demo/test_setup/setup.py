from setuptools import setup, find_packages

setup(
    name='dotsmap',
    version='0.1',
    py_modules=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        dotsmap=dots_map:cli
    ''',
)
