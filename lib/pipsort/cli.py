""" Implementation of the command line interface.

"""
from __future__ import absolute_import

from argparse import ArgumentParser

import subprocess

from . import __version__
from .core import config
from .core import logger
from .command import cmd1
from .command import cmd2


__all__ = "main",


def _cmdline(argv=None):
    """ Parse command line arguments.

    """
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", action="append",
            help="config file [etc/config.yml]")
    parser.add_argument("-v", "--version", action="version",
            version="pipsort {:s}".format(__version__),
            help="print version and exit")
    parser.add_argument("-w", "--warn", default="WARNING",
            help="logger warning level [WARNING]")
    parser.add_argument("search_term", type=str,
                        help="Search term for PyPI")
    # subparsers = parser.add_subparsers(title="commands")
    # search_term = subparsers.add_parser("search_term")
    # search_term.set_defaults(command=search_term)
    # cmd2_parser = subparsers.add_parser("cmd2")
    # cmd2_parser.set_defaults(command=cmd2)
    args = parser.parse_args(argv)
    if not args.config:
        # Don't specify this as an argument default or else it will always be
        # included in the list.
        args.config = ["etc/config.yml"]
    return args


def main(argv=None):
    """ Execute the application CLI.

    Arguments are taken from sys.argv by default.

    """
    args = _cmdline(argv)
    # logger.start(args.warn)
    # logger.info("starting execution")
    config.load(args.config)
    # print args
    import ipdb; ipdb.set_trace()
    # args.command(**vars(args))
    # logger.info("successful completion")
    results = subprocess.check_output(['pip', 'search', args.search_term]).split('\n')
    results = sorted([result for result in results if "(" in result and ")" in result], key=lambda t: t[t.find("("):t.find(")")], reverse=True)
    print '\n'.join(results)

    return 0
 

# Make the module executable.

if __name__ == "__main__":
    try:
        status = main()
    except:
        logger.critical("shutting down due to fatal error")
        raise  # print stack trace
    else:
        raise SystemExit(status)
