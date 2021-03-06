import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='django-csv-exports',
    version=__import__('django_csv_exports').__version__,
    author='Victor Rocha',
    author_email='victor@rochapps.com',
    packages=find_packages(),
    install_requires=[
        'unicodecsv',
    ],
    include_package_data=True,
    url='https://github.com/fdemmer/django-csv-exports',
    license='BSD',
    description=u' '.join(__import__('django_csv_exports').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.rst'),
    test_suite="runtests.runtests",
    zip_safe=False,
)
