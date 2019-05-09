from setuptools import setup

version = 0.2
setup(
    name='addsPy',
    version=version,
    packages=['addsPy'],
    install_requires=[
        'pendulum',
        'requests',
        'untangle'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/jgillmanjr/addsPy',
    license='',
    author='Jason Gillman Jr.',
    author_email='jason@rrfaae.com',
    description='A Python library for working with the ADDS data server'
)
