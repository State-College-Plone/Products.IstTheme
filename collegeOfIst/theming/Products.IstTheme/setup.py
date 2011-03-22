from setuptools import setup, find_packages
import os

version = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 
    'Products', 'IstTheme', 'version.txt')).read().strip()

setup(name='Products.IstTheme',
    version=version,
    description="Theme product for College of IST.",
    long_description=open("README.txt").read() + "\n" +
                     open("HISTORY.txt").read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
      "Framework :: Plone",
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='',
    author='WebLion Group, Penn State',
    author_email='support@weblion.psu.edu',
    url='http://weblion.psu.edu/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'setuptools',
      # -*- Extra requirements: -*-
      ],
    entry_points="""
      # -*- Entry points: -*-
      """,
    )
