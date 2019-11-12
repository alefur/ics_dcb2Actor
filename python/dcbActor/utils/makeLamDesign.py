#!/usr/bin/env python

"""
Executable script to create a PfiDesign for a LAM exposure, given the colors
of fibers used.
"""

import numpy as np

# Mapping of colors to fiberIds
# Constructed from a snippet by Fabrice Madec, "dummy cable B fibers"
# https://sumire-pfs.slack.com/files/U3MLENNHH/FFS6P4UR5/dummy_cable_b_fibers.txt

allFibers = list(np.arange(1, 652))
blank = [44, 91, 93, 136, 183, 185, 228, 272] + list(np.arange(317, 336)) + [383, 427, 470, 472, 516, 559, 561, 608]
blank34 = [281, 309, 359]
engineering = [1, 45, 92, 137, 184, 229, 273, 316, 336, 382, 426, 471, 515, 560, 607, 651]
science = np.array([fib for fib in allFibers if fib not in engineering + blank])
mtp9 = list(science[science < 273])
mtp12 = list(science[science > 273])

FIBER_COLORS = {"red1": [2],
                "red2": [3],
                "red3": [308],
                "red4": [339],
                "red5": [340],
                "red6": [342],
                "red7": [649],
                "red8": [650],
                "orange": [12, 60, 110, 161, 210, 259, 341],
                "blue": [32, 111, 223, 289, 418, 518, 620],
                "green": [63, 192, 255, 401, 464, 525, 587],
                "yellow": [347, 400, 449, 466, 545, 593, 641],
                "engineering": engineering,
                "9mtp": mtp9,
                "12mtpS12": mtp12,
                "12mtpS34": [fib for fib in mtp12 if fib not in blank34]
                }

sortedKeys = ['blue', 'green', 'orange', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'red7', 'red8', 'yellow',
              'engineering', '9mtp', '12mtpS12', '12mtpS34']
# Mapping of colors to hash value
# This scheme makes the hash look like binary, with a 1 if the color was used and 0 if not
HASH_COLORS = {color: 16 ** ii for ii, color in enumerate(sortedKeys)}


def colorsToFibers(colors):
    """Convert a list of colors to an array of fiber IDs
    Parameters
    ----------
    colors : iterable of `str`
        List of colors.
    Returns
    -------
    fiberId : `numpy.ndarray`
        Array of fiber IDs.
    """
    return np.array(sorted(set(sum([FIBER_COLORS[col] for col in colors], []))))


def hashColors(colors):
    """Convert a list of colors to a hash for the pfiDesignId
    Parameters
    ----------
    colors : iterable of `str`
        List of colors.
    Returns
    -------
    hash : `int`
        Hash, for the pfiDesignId.
    """
    return sum(HASH_COLORS[col] for col in set(colors))
