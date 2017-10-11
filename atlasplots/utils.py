from __future__ import absolute_import, division, print_function

import ROOT as root


def DrawText(x, y, text, color=1, size=0.05):
    """Draw text.

    Parameters
    ----------
    x : float
        x position in NDC coordinates
    y : float
        y position in NDC coordinates
    text : string, optional
        Text displayed next to label (the default is None)
    color : TColor, optional
        Text colour (the default is 1, i.e. black)
        See https://root.cern.ch/doc/master/classTColor.html
    size : float, optional
        Text size
        See https://root.cern.ch/doc/master/classTLatex.html
    """
    l = root.TLatex()
    # l.SetTextAlign(12)
    l.SetTextSize(size)
    l.SetNDC()
    l.SetTextColor(color)
    l.DrawLatex(x, y, text)
