#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Student Study group led by Daniel Lomelino, written by Kathryn Anderson"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Transform and display a message.")
    parser.add_argument('msg', help="message to display")
    parser.add_argument('-b', '--border', 
        help="border character around message")
    parser.add_argument('-n', type=int,
        help="number of times to display the message")
    parser.add_argument('-u', action='store_true',
        help="transform message to uppercase")
    parser.add_argument('-l', action='store_true',
        help="transform message to lowercase")
    parser.add_argument('-t', action='store_true',
        help="message to display")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args()

    num_times = ns.n or 1
    msg = ns.msg

    # apply command line argument logic
    if ns.u:
        msg = msg.upper()
    if ns.l:
        msg = msg.lower()
    if ns.t:
        msg = msg.title()

    # display the tranformed message
    if ns.border:
        print(f"{ns.border * len(msg)}")
    for n in range(num_times):
        print(msg)
    if ns.border:
        print(f"{ns.border * len(msg)}")




    return


if __name__ == '__main__':
    main(sys.argv[1:])
