#!/usr/bin/env python3
import sys
import argparse
import hashlib

# parser help for viewing hashes
parser = argparse.ArgumentParser(prog='{} hash'.format(sys.argv[0]),
                    description='view different hashes of a file', add_help=False)
parser.add_argument('string', metavar='image', type=str, help='the path to a file')\

# We use a chunk size of 128kb as to not use too much ram
CHUNK_SIZE = 128 * 1024

algs = {
    "md5": hashlib.md5(),
    "sha1": hashlib.sha1(),
    "sha224": hashlib.sha224(),
    "sha256": hashlib.sha256(),
    "sha384": hashlib.sha384(),
    "sha512": hashlib.sha512(),
    "blake2b": hashlib.blake2b(),
    "blake2s": hashlib.blake2s()
}

def main(args):
    try:
        file = args[2]
        print(f"File: {file}")

        chunk_array = bytearray(CHUNK_SIZE)
        mv = memoryview(chunk_array)
        with open(file, 'rb', buffering=0) as file:
            for chunk in iter(lambda : file.readinto(mv), 0):
                for alg in algs:
                    # update all of our hashes
                    algs[alg].update(mv[:chunk])
            print("Hashes:")
            for alg in algs:
                # print all of our final hashes
                print(f"  {alg}: {algs[alg].hexdigest()}")
    except:
        help()

def short_desc():
    print("  hash - " + parser.description)

def help():
    parser.print_help()
