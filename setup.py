from setuptools import setup


setup(
    name='pip-merge',
    version='0.1.0',
    url='https://github.com/cnds/pip-merge',
    license='MIT',
    author='cnds',
    author_email='dingsong87@gmail.com',
    description=__doc__.strip('\n'),
    scripts=['pip-merge'],
    zip_safe=False,
    paltforms='any',
    install_requires=['docopt'],
    classifiers=[
        'Programming Language :: Python :: 2.7'
    ]
)
