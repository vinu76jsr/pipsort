Overview
========

This is the pipsort application - sorts pip search results based on version number


Minimum Requirements
====================

* Python 2.7


Optional Requirements
=====================

..  _py.test: http://pytest.org
..  _Sphinx: http://sphinx-doc.org

* `py.test`_ 2.7 (for running the test suite)
* `Sphinx`_ 1.3 (for generating documentation)


Basic Setup
===========

Install for the current user:

..  code-block::

    $ python setup.py install --user


Run the application:

..  code-block::

    $ python -m pipsort --help


Run the test suite:

..  code-block::
   
    $ py.test test/


Build documentation:

..  code-block::

    $ cd doc && make html
    
    
Deploy the application in a self-contained `Virtualenv`_ environment:

..  _Virtualenv: https://virtualenv.readthedocs.org

..  code-block::

    $ python deploy.py /path/to/apps
    $ cd /path/to/apps/ && pipsort/bin/cli --help
