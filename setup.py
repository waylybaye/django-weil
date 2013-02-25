try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = __import__('dj_mailman').__version__

setup(
    name="django-mailman",
    packages=['dj_mailman'],
    version=version,
    author="Baye Wayly",
    author_email="havelove@gmail.com",
    url="https://github.com/waylybaye/django-mailman",
    install_requires=["Django>=1.2", "requests"],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
