"""
Config File Reader
==================

The config files are written in the `TOML <https://github.com/toml-lang/toml>`_
format.
"""

from __future__ import absolute_import, division, print_function

import collections
import sys
import toml

from .console import bcolor


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

    # If using Python 2, convert unicode keys and values to strings
    if sys.version_info[0] == 2:
        params = _convert_to_string(params)

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
    print("{}  {} missing {} parameter".format(
        bcolor.error(),
        bcolor.bold + parent + bcolor.end,
        bcolor.bold + param + bcolor.end)
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


def _convert_to_string(data):
    """Convert data in unicode format to string.

    Parameters
    ----------
    data : {str, dict}
        Data in unicode format
    
    Returns
    -------
        Data in string format
    """
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(_convert_to_string, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(_convert_to_string, data))
    else:
        return data
