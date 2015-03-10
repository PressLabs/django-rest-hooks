from distutils.core import setup # setuptools breaks

# Dynamically calculate the version
version_tuple = __import__('rest_hooks').VERSION
version = '.'.join([str(v) for v in version_tuple])

setup(
    name = 'django-rest-hooks-ng',
    description = 'A powerful mechanism for sending real time API notifications via a new subscription model.',
    version = version,
    author = 'Bryan Helmig, Calin Don',
    author_email = 'calin@presslabs.com',
    url = 'http://github.com/PressLabs/django-rest-hooks-ng',
    install_requires=['Django>=1.4','requests'],
    packages=['rest_hooks'],
    package_data={
        'rest_hooks': [
            'migrations/*.py'
        ]
    },
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
