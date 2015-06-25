#!/usr/bin/env python
#
# entrypoint.py
#
# Copyright (c) 2015 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
""" The entry point of the image.

This script sets up a directory to make and run make command in it.
"""
import argparse
import logging
import subprocess
import sys


def run(params, cwd):
    """ Run make command.

    Args:
      params: parameters for make command.
      cwd: direcory where make command run.
    """
    cmd = " ".join(["make", ] + params)
    logging.info("Start a build process. (cmd=%s)", cmd)

    # Create a subprocess.
    proc = subprocess.Popen(
        cmd, cwd=cwd, shell=True, stdout=sys.stdout, stderr=sys.stderr)

    # Wait the process will end.
    proc.wait()

    logging.info("The build process has ended.")


def main():
    """ The main function.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cwd", default="/data/",
        help="specify a directory containing Makefile.")
    parser.add_argument(
        "params", default=["html"], nargs="*",
        help="specify options of make (default: html).")

    run(**vars(parser.parse_args()))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    finally:
        logging.shutdown()
