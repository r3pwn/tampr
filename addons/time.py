#!/usr/bin/env python3
import os
import time
import sys
import datetime
import argparse

parser = argparse.ArgumentParser(prog='{} time'.format(sys.argv[0]), 
            description='view file last modified date', add_help=False)
parser.add_argument('string', metavar='file', type=str, help='the path to a file')
set_parser = argparse.ArgumentParser(prog='{} time set'.format(sys.argv[0]),
                    description='edit the exif data of images', add_help=False)
set_parser.add_argument('string', metavar='file', type=str, help='the path to a file')
set_parser.add_argument('string', metavar='timestamp', type=str, help='the desired modified time, in UNIX timestamp format')

def main(args):
    if args[2] == "set":
        try:
            edit_file_time(args[3], args[4])
        except:
            set_parser.print_help()
        return
    else:
        view_file_time(args[2])
        return

def view_file_time(filename):
    print(f"File: {filename}")
    modified = os.path.getmtime(filename)
    print("  Date modified:",datetime.datetime.fromtimestamp(modified))

def edit_file_time(filename, timestamp):
    print(f"File: {filename}")
    modified = os.path.getmtime(filename)
    accessed = os.path.getatime(filename)
    print("  Current modified date:", datetime.datetime.fromtimestamp(modified))
    print("  New modified date:", datetime.datetime.fromtimestamp(int(timestamp)))

    os.utime(filename, (accessed, int(timestamp)))

def short_desc():
    print("  time - " + "view/edit file last modified date")

def help():
    parser.print_help()
    print("----------------------------------------")
    set_parser.print_help()
