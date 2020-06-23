#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Student Study group led by Daniel Lomelino, and Jo Anna Mollman, written by Kathryn Anderson"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    # parser.add_argument('msg', help="message to display")
    parser.add_argument('-u', "--upper", action='store_true',
        help="convert text to uppercase")
    parser.add_argument('-l', "--lower", action='store_true',
        help="convert text to lowercase")
    parser.add_argument('-t', "--title", action='store_true',
        help="convert text to titlecase")
    parser.add_argument('text', help="text to be manipulated")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    # num_times = ns.n or 1
    text = ns.text

    # apply command line argument logic

    if ns.upper:
        text = text.upper()
    if ns.lower:
        text = text.lower()
    if ns.title:
        text = text.title()
    print(text)

    # # display the tranformed message
    # if ns.border:
    #     print(f"{ns.border * len(msg)}")
    # for n in range(num_times):
    #     print(msg)
    # if ns.border:
    #     print(f"{ns.border * len(msg)}")


    return text


if __name__ == '__main__':
    main(sys.argv[1:])
