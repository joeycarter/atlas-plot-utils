"""
Config File Reader
==================

The config files are written in the `TOML <https://github.com/toml-lang/toml>`_
format.
"""

from __future__ import absolute_import, division, print_function

import sys
import toml
import crayons


def read(config_file):
    """Read the plotting configuration parameters into a dictionary.

    TODO
    ----
    Set more default values

    Parameters
    ----------
    config_file : str
        Path to the config file

    Returns
    -------
    dict
        Dictionary of configuration parameters
    """
    with open(config_file, 'r') as file:
        config_file_str = file.read()

    params = toml.loads(config_file_str)

    _check_required(params)
    _fill_missing(params)

    return params


def _check_required(params):
    """Check that the configuration file has all the required parameters and
    exit if any are missing.

    TODO
    ----
    Add more required parameters

    Parameters
    ----------
    params : dict
        Dictionary of configuration parameters
    """
    exit = False

    if 'file' not in params:
        _print_missing("file")
        exit = True
    else:
        for file in params['file']:
            if 'name' not in file:
                _print_missing("name", "[[file]]")
                exit = True
            if 'tree' not in file:
                _print_missing("tree", "[[file]]")
                exit = True

    if 'plot' not in params:
        _print_missing("plot")
        exit = True
    else:
        for plot in params['plot']:
            if 'name' not in plot:
                _print_missing("name", "[[plot]]")

    if exit:
        sys.exit(1)


def _print_missing(param, parent="Config file"):
    """Print error message if parameter is missing.

    Also print where the parameter should be in the config file.

    Parameters
    ----------
    param : str
        The missing parameter
    parent : str, optional
        "Parent" of the missing parameter (the default is "Config file")
    """
    print("{} {} missing {} parameter".format(
        crayons.red("Error:"),
        crayons.white(parent, bold=True),
        crayons.white(param, bold=True))
    )


def _fill_missing(params):
    """Fill in missing configuration parameters with default values

    Parameters
    ----------
    params : dict
        Dictionary of configuration parameters
    """
    # Missing [[file]] parameters
    for file in params['file']:
        if 'label' not in file:
            file['label'] = file['name']

        if 'color' not in file:
            file['color'] = "#000000"  # black

        if 'fill' not in file:
            file['fill'] = None

        if 'scale' not in file:
            file['scale'] = 1.0
