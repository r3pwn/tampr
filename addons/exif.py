#!/usr/bin/env python3
import piexif
from PIL import Image, ExifTags
import sys
import argparse

parser = argparse.ArgumentParser(prog='{} exif'.format(sys.argv[0]), 
            description='view/edit the exif data of images', add_help=False)
parser.add_argument('string', metavar='image', type=str,
                    help='the path to an image')

def main(args):
    print("Image:", args[2])
    try:
        img = Image.open(args[2])
        exif_dict = piexif.load(img.info["exif"])
    except:
        print("Not a supported image type or no metadata found")
        return

    if exif_dict:
        # specify the metadata types to return
        metadatatypes = ['0th', 'Exif', 'GPS', 'Interop', '1st']

        for metadatatype in metadatatypes:
            print("Section:", metadatatype)
            for key, val in exif_dict[metadatatype].items():
                if key in ExifTags.TAGS:
                    print(f"  {ExifTags.TAGS[key]}: {repr(val)}")
            print("----------------------------------------")
    else:
        # no metadata found in image
        print("No metadata found in image")
        return

def short_desc():
    print("  exif - " + parser.description)

def help():
    parser.print_help()
