Introduction
============

The purpose of this package is to provide a sample package that uses
Plone 5 resources in different ways for people to follow for their projects.

Read the source!


Building
--------

TTW
~~~~

You can build the JS/CSS in the control panel. Building this way
changed the built js and css url since when you build, it won't save
the built file back to the product for you automatically. You can
copy the data from the built js/css back into your product or
proceed to the next step.


CLI build tool
~~~~~~~~~~~~~~

Plone 5 include a couple nice command line build script for you to use
with your bundles. To build the bundle provided in this pacakge
with the command line scripts, the process is:

1. create a Plone site and give it an id
2. install the example.plone5resources package
3. shutdown plone
4. then run the command: `./bin/plone-compile-resources --site-id=Plone4 --bundle=example-bundle`


Caveats
-------

If you're building with the command line, please beware of a bunch that was fixed in master: https://github.com/plone/Products.CMFPlone/commit/99d5952f4329504cc60120562f746f37b045880b

If you have issues building with the CLI tool, you'll need to checkout master of Products.CMFPlone and use that.
