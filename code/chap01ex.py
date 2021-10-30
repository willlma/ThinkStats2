"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def validate_pregnum(df):
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)
    for index, pregnum in df.pregnum.items():
        caseid = df.caseid[index]
        indices = preg_map[caseid]

        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = nsfg.ReadFemResp()
    counts = df.pregnum.value_counts()
    assert(counts[1] == 1267)
    assert(len(df) == 2610+1432+1267+1110+611+305+150+80+40+21+9+3+2+2+1)
    assert(validate_pregnum(df))
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
