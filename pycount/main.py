#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
   pycount/main
   ~~~~~~~~~~~~~~~

   Command-line utility module.

   :copyright: (c) Tihomir Saulic
   :license: DO WHAT YOU WANT TO PUBLIC LICENSE, see LICENSE for more details
"""


from __future__ import print_function

import argparse
import pkg_resources

from .core import Counter
from .core import Timer

from .version import __version__ as VERSION


def report(COUNTER, TIMED):
    """Generates and prints a decent looking breakdown report for lines
       of code for all existent languages under our path
    """
    if COUNTER.results:
        counted = sum(COUNTER.file_types.values())
        print("version " + VERSION)
        print("\nLanguage                       Files         LOC")
        print("-" * 48)
        for key, value in sorted(COUNTER.results.items(), key=lambda x: x[1],
                                 reverse=True):
            if value is not 0:
                print("{0:24}     {1:7d}   {2:9d}".format(key, COUNTER.file_types[key], value))
        print("-" * 48)
        print("{0:24}     {1:7d}   {2:9d}".format("SUM:", counted, sum(COUNTER.results.values())))
        print("-" * 48)
        print("{0:24} {1:23.2f}".format("RUNTIME (sec):", TIMED))
        print("-" * 48)
    else:
        print("No results.")


def main(args):
    PARSER = argparse.ArgumentParser(description='Perform LOC counting.')
    PARSER.add_argument('-v', '--version', action='version',
                        version=VERSION)
    PARSER.add_argument('-e', '--exclude', nargs=1, type=str,
                        help='directories/files to be excluded from counting')
    PARSER.add_argument('files', nargs='*')
    ARGS = vars(PARSER.parse_args(args))
    try:
        EXCLUDED = ARGS['exclude'][0].split(',')
    except (KeyError, TypeError):
        EXCLUDED = None
    if ARGS['files']:
        COUNTER = Counter(ARGS['files'], ignore=EXCLUDED)
    else:
        COUNTER = Counter('.', ignore=EXCLUDED)
    try:
        with Timer() as timer:
            COUNTER.discover()
            COUNTER.count()
    finally:
        TIMED = timer.interval
    report(COUNTER, TIMED)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
