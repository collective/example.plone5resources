Introduction
============

The purpose of this package is to provide a sample package that uses
Plone 5 resources in different ways for people to follow in their projects.

Read the source!


Building methods
----------------

TTW (through the web)
~~~~~~~~~~~~~~~~~~~~~

You can build the JS/CSS in the new Resources Registries control panel.
However Plone won't automatically save the built js and css back into the
filesystem product for you. You'll have to manually copy the data from the
built js/css back into your product, or make use of the next method.


CLI build tool
~~~~~~~~~~~~~~

Plone 5 includes a couple of nice command line build scripts for you to use
with your bundles. To build the bundle provided in this pacakge with the
command line scripts, the process is:

1. Create a Plone site and give it an id
2. Install the example.plone5resources package
3. Shutdown plone
4. Then run the command: `./bin/plone-compile-resources --site-id=Plone5 --bundle=example-bundle`


Caveats
-------

* If you're building with the command line, please beware of a bug that was fixed in master: https://github.com/plone/Products.CMFPlone/commit/99d5952f4329504cc60120562f746f37b045880b
* If you have issues building with the CLI tool, you'll need to checkout master of Products.CMFPlone and use that.
