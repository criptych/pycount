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
from .core import TextReport
from .core import ChartReport

from .version import __version__ as VERSION


def main(args):
    PARSER = argparse.ArgumentParser(description='Perform LOC counting.')
    PARSER.add_argument('-v', '--version', action='version',
                        version=VERSION)
    PARSER.add_argument('-e', '--exclude', nargs=1, type=str,
                        help='directories/files to be excluded from counting')
    PARSER.add_argument('-r', '--report-file', nargs='?', type=str,
                        help='report output file name', const='report.pdf')
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

    TextReport().generate(COUNTER, TIMED)

    if ARGS.get('report_file'):
        ChartReport().generate(COUNTER, TIMED, ARGS.get('report_file'))


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
