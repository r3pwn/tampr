#!/usr/bin/env python3
import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(prog='{} exif'.format(sys.argv[0]), 
            description='view/edit the exif data of images', add_help=False)

def main(args):
    # tool exif 'filename'
    process = subprocess.Popen(['exif', args[2]], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break

def short_desc():
    print("  exif - " + parser.description)

def help():
    parser.print_help()
