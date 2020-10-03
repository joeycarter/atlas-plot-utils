ATLAS Plot Utils
================

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
    :target: https://github.com/joeycarter/atlas-plots/blob/master/LICENSE

A collection of utility functions and style settings for making pretty plots with PyROOT for the ATLAS Experiment at CERN.

----

| :warning: ATLAS Plot Utils (formerly *ATLAS Plots*) is now mostly deprecated! :warning:
|
| Check out my new project, `ATLAS Plots <https://github.com/joeycarter/atlas-plots>`_, which uses `matplotlib <https://matplotlib.org/>`_-like syntax and idioms to produce plots in ROOT following the standard ATLAS style guidelines.

----

Installing
----------

**atlasplots** isn't in PyPI (yet) so for now it's best to clone the source and install as editable:

.. code:: bash
    
    $ git clone git@github.com:joeycarter/atlas-plots.git
    $ cd atlas-plots
    $ pip install -e .

To uninstall:

.. code:: bash

    $ pip uninstall atlasplots

Installing on lxplus
--------------------

Installing **atlasplots** is a bit more involved if you want to use it on ``lxplus``.
Full installation instructions can be found `here <https://atlas-plots.readthedocs.io/en/latest/getting_started.html#installing-on-lxplus>`_.

Documentation
-------------

The full documentation is available over at https://atlas-plots.readthedocs.io.
