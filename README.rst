What is this?
=============

This is a package for reading, writing and managing `Apple
PLIST-files <https://www.unix.com/man-page/OSX/5/plist>`__, in
XML-Format, with Python 3.

Installation
============

.. code:: sh

   pip3 install pyplist

Examples
========

Reading plist files
-------------------

Reading XML-PLists from file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

   from pyplist import XMLParser

   obj = XMLParser.parseFile("path_to_file")

   # ... use obj as a normal python object

Reading XML-PLists from string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

   from pyplist import XMLParser

   obj = XMLParser.parse("some_loaded_string")

   # ... use obj as a normal python object

Reading Binary plists
~~~~~~~~~~~~~~~~~~~~~

Coming Soon

Writing objects to plist files
------------------------------

Writing XML-PLists to file
~~~~~~~~~~~~~~~~~~~~~~~~~~

Objects can be written to xml plists with:

.. code:: py

   from pyplist import XMLParser
   from pyplist import XMLWriter

   obj = XMLParser.parseFile(<path_to_plist_file>)

   with open(<path_to_output_file>, 'wt') as outstream:
     XMLWriter.write(obj, outstream[, indentString=None, level=0])
     outstream.close()

The parameters are:

-  obj - The object being serialized
-  outstream - The output stream to which the object will be serialized.
   If this is None, then a new string outputstream is written to and
   returned.
-  indentString - Indentation string to be used. If this value is None
   then no indentation or pretification is applied. Otherwise this is
   used.
-  level - The level to start with when serializing. Each child node is
   indented an extra level (if indentString is not None).

Writing to Binary plists
~~~~~~~~~~~~~~~~~~~~~~~~

Coming Soon.
