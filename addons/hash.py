#!/usr/bin/env python3
import sys
import argparse
import hashlib

# parser help for viewing hashes
parser = argparse.ArgumentParser(prog='{} hash'.format(sys.argv[0]),
                    description='view different hashes of a file', add_help=False)
parser.add_argument('string', metavar='image', type=str, help='the path to a file')\

# We use a chunk size of 64kb as to not use too much ram
BUF_SIZE = 65536

# sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s()
def main(args):
    try:
        file = args[2]
        print(f"File: {file}")

        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha224 = hashlib.sha224()
        sha256 = hashlib.sha256()
        sha384 = hashlib.sha384()
        sha512 = hashlib.sha512()
        blake2b = hashlib.blake2b()
        blake2s = hashlib.blake2s()

        with open(file, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
            print("Hashes:")
            print(f"  md5: {md5.hexdigest()}")
            print(f"  sha1: {sha1.hexdigest()}")
            print(f"  sha224: {sha224.hexdigest()}")
            print(f"  sha256: {sha256.hexdigest()}")
            print(f"  sha384: {sha384.hexdigest()}")
            print(f"  sha512: {sha512.hexdigest()}")
            print(f"  blake2b: {blake2b.hexdigest()}")
            print(f"  blake2s: {blake2s.hexdigest()}")
    except:
        help()
    

def short_desc():
    print("  hash - " + parser.description)

def help():
    parser.print_help()
