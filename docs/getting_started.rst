.. _getting_started:

Getting Started
===============

.. contents::
   :local:

Before You Begin
----------------

If you can, use Python 3. Have a look at `Picking a Python Interpreter <http://docs.python-guide.org/en/latest/starting/which-python/>`_ on Kenneth Reitz's `Guide to Python <http://docs.python-guide.org/>`_ for a few reasons why.

Also have a look at the chapter on `Properly Installing Python <http://docs.python-guide.org/en/latest/starting/installation/>`_ for recommendations on how to install your Python interpreter.

If you're using a Mac, you can install Python with `Homebrew <https://brew.sh/>`_:

.. code:: bash

    $ brew install python3

Homebrew also installs ``pip3`` for you, which is an alias pointing to ``pip`` in your Homebrew'd version of Python 3.

.. note::

    You may encounter issues with file permissions when installing software because Homebrew needs write access to ``/usr/local/``.
    Since ``brew install`` will not work with root privileges (unless ``brew`` itself is owned by root), you can change the ownership of the contents of ``/usr/local/``, or wherever Homebrew installs software, with,

    .. code:: bash

        $ sudo chown -R $(whoami) $(brew --prefix)/*

    Proceed with caution, however, if you have other non-Homebrew'd software here.

Installing ROOT
---------------

`ROOT <https://root.cern.ch/>`_ is a scientific software framework developed at CERN for data analysis in high energy physics.
The easiest way to install ROOT if you're using a Mac is also with Homebrew:

.. code:: bash

    $ brew install root --with-python3 --without-python

This compiles ROOT from source which can take upwards of 90 minutes, but at the advantage of giving you access to the ROOT libraries from Python 3.
``brew install root`` on the other hand installs a pre-compiled version of ROOT, which by default only supports Python 2.

If you don't like using Homebrew, you can always download ROOT from https://root.cern.ch/downloading-root and install it manually.
Or if you're feeling really adventurous, you can clone the `ROOT GitHub repository <https://github.com/root-project/root>`_ and install it from source.

.. note::

    Because ROOT depends on several installation-dependent environment variables to function properly, you should add the following commands to your shell initialization script (.bashrc/.profile/etc.), or call them directly before using ROOT.

    For bash users:
        ``. /usr/local/bin/thisroot.sh``
    For zsh users:
        ``pushd /usr/local >/dev/null; . bin/thisroot.sh; popd >/dev/null``
    For csh/tcsh users:
        ``source /usr/local/bin/thisroot.csh``

PyROOT
------

`PyROOT <https://root.cern.ch/pyroot>`_ is a Python extension module that allows the user to interact with any ROOT class from the Python interpreter. 
Using PyROOT is super easy.
As an example, consider opening a TBrowser:

>>> import ROOT
>>> br = ROOT.TBrowser()

Or if you prefer, you can import ROOT classes directly:

>>> from ROOT import TBrowser
>>> br = TBrowser()

.. note::

    As a shortcut, set an alias to ``python -i -c "import ROOT"`` to open a Python shell with ROOT ready to go. 

To illustrate the power and simplicity of PyROOT, consider opening a ROOT file ``data_file.root`` containing a TTree called ``data_tree``:

>>> import ROOT
>>> file = ROOT.TFile.Open("data_file.root")
>>> tree = file.data_tree
>>> tree.Print()
******************************************************************************
*Tree    :data_tree : Test ROOT tree                                         *
*Entries :     3524 : Total =         2104055 bytes  File  Size =     196761 *
*        :          : Tree compression factor =  10.76                       *
******************************************************************************
*Br    0 :eta       : eta/D                                                  *
*Entries :     3524 : Total  Size=     542582 bytes  File Size  =      49459 *
*Baskets :       18 : Basket Size=      32000 bytes  Compression=  10.96     *
*............................................................................*
*Br    1 :phi       : phi/D                                                  *
*Entries :     3524 : Total  Size=     542582 bytes  File Size  =      49459 *
*Baskets :       18 : Basket Size=      32000 bytes  Compression=  10.96     *
*............................................................................*
...

As a complete example, suppose you want to print all the values in the ``eta`` branch:

.. code:: python

    import ROOT

    file = ROOT.TFile.Open("data_file.root")
    tree = file.data_tree
    
    for entry in tree:
        print(entry.eta)

Compare this to the equivalent C++ ROOT macro:

.. code:: c++

    {
        TFile* file = TFile::Open("data_file.root");

        TTreeReader data_reader("data_tree", file);
        TTreeReaderValue<double> eta(data_reader, "eta");

        while (data_reader.Next()) {
            std::cout << *eta << std::endl;
        }
    }

Installing atlasplots
---------------------

**atlasplots** isn't in PyPI (yet) so for now it's best to clone the source and install as editable:

.. code:: bash

    $ git clone git@github.com:joeycarter/atlas-plots.git
    $ cd atlas-plots
    $ pip install -e .

To uninstall:

.. code:: bash

    $ pip uninstall atlasplots


Basic Usage
-----------

Import the **atlasplots** package:

>>> import atlasplots

Set the ATLAS Style for plotting:

>>> from atlasplots import atlas_style as astyle
>>> astyle.SetAtlasStyle()

Add the "*ATLAS* Internal" label to a plot:

>>> from atlasplots import atlas_style as astyle
>>> astyle.ATLASLabel(0.2, 0.87, "Internal")

For a collection of complete examples, see the :ref:`examples` section.
