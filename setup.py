from setuptools import setup, find_packages

version = '1.0.0'

setup(name='example.plone5resources',
      version=version,
      description="example plone 5 resources product",
      long_description=open("README.rst").read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 5.0",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
      ],
      keywords='javascript plone less css',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['example'],
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,

      )
