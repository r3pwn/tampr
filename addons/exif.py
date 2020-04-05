#!/usr/bin/env python3
import piexif
from PIL import Image, ExifTags
import sys
import argparse

# parser help for viewing and editing
parser = argparse.ArgumentParser(prog='{} exif'.format(sys.argv[0]),
                    description='view the exif data of images', add_help=False)
parser.add_argument('string', metavar='image', type=str, help='the path to an image')
edit_parser = argparse.ArgumentParser(prog='{} exif edit'.format(sys.argv[0]),
                    description='edit the exif data of images', add_help=False)
edit_parser.add_argument('string', metavar='image', type=str, help='the path to an image')
edit_parser.add_argument('string', metavar='key', type=str, help='the metadata key')
edit_parser.add_argument('string', metavar='value', type=str, help='the new value for the metadata key')

def main(args):
    if args[2] == "edit":
        try:
            edit_metadata(args[3], args[4], args[5])
        except:
            edit_parser.print_help()
        return
    else:
        print_metadata(args[2])
        return

def print_metadata(image_path):
    print("Image:", image_path)
    try:
        img = Image.open(image_path)
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
                # MakerNote contains a large binary string, seemingly of garbage
                if key in ExifTags.TAGS and ExifTags.TAGS[key] is not "MakerNote":
                    print(f"  {ExifTags.TAGS[key]}: {repr(val)}")
            print("----------------------------------------")
    else:
        # no metadata found in image
        print("No metadata found in image")
        return

def edit_metadata(image_path, metadata_key, new_value):
    print("Image:", image_path)
    try:
        img = Image.open(image_path)
        exif_dict = piexif.load(img.info["exif"])
    except:
        print("Not a supported image type or no metadata found")
        return

    if exif_dict:
        # specify the metadata types to return
        metadatatypes = ['0th', 'Exif', 'GPS', 'Interop', '1st']

        for metadatatype in metadatatypes:
            for key, val in exif_dict[metadatatype].items():
                if key in ExifTags.TAGS and ExifTags.TAGS[key] == metadata_key:
                    print("Old value:")
                    print(f"  {ExifTags.TAGS[key]}: {repr(val)}")
                    exif_dict[metadatatype][key] = new_value
                    print("New value:")
                    print(f"  {ExifTags.TAGS[key]}: b'{new_value}'")
    else:
        # no metadata found in image
        print("No metadata found in image")
        return
    exif_bytes = piexif.dump(exif_dict)
    img.save(image_path, "jpeg", exif=exif_bytes)

def short_desc():
    print("  exif - " + "view/edit the exif data of images")

def help():
    parser.print_help()
    print("----------------------------------------")
    edit_parser.print_help()
