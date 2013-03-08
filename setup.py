try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = __import__('dj_weil').__version__

setup(
    name="django-weil",
    packages=['dj_weil'],
    version=version,
    author="Baye Wayly",
    author_email="baye@wayly.net",
    url="https://github.com/waylybaye/django-weil",
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
