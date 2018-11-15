=========
Pyinspire
=========

Retrieve results from the INSPIRE HEP database (http://inspirehep.net) from the
command line.

Author: Ian Huston

Contributors: David Straub

Released under the modified BSD license.

Usage: pyinspire.py [options]
Example: pyinspire.py -b -s "find a Feynman, Richard"

Options:
--version             show program's version number and exit
-h, --help            show this help message and exit
-s STRING, --search=STRING
                        search string to send to INSPIRE
-b, --bibtex          output bibtex for entries
--latexEU             use LaTeX(EU) format for entries
--latexUS             output bibtex for entries
-v, --verbose         print informative messages
--debug               log lots of debugging information


Tested with Python 2.7 and 3.4.
  
Please be careful to not overload the INSPIRE server by repeatedly requesting 
large numbers of results. If using pyinspire in a script please add some 
throttling of frequency of search queries.

Note: Currently only the first 100 results are returned.
