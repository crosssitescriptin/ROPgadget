## -*- coding: utf-8 -*-
##
##  incon - 2014-05-12 - ROPgadget tool
##
##  http://twitter.com/Hexdumping
##  
##

import ropgadget.args
import ropgadget.binary
import ropgadget.core
import ropgadget.gadgets
import ropgadget.options
import ropgadget.rgutils
import ropgadget.updateAlert
import ropgadget.version
import ropgadget.loaders
import ropgadget.ropchain

def main():
    import sys
    from   ropgadget.args import Args
    from   ropgadget.core import Core
    try:
        args = Args()
    except ValueError as e:
        print(e)
        sys.exit(-1)
    sys.exit(0 if Core(args.getArgs()).analyze() else 1)
