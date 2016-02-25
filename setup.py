from setuptools import setup


setup(
    name='XWING',
    version='0.0.1.dev0',
    url='https://github.com/victorpoluceno/xwing',
    license='ISC',
    description='XWING is a Python library writen using that help '
        'to distribute connect to a single port to other process',
    author='Victor Poluceno',
    author_email='victorpoluceno@gmail.com',
    packages=['xwing'],
    install_requires=[
        'gevent',
        'pyzmq'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Networking',
    ]
)
