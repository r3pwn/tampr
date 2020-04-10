# Tampr

## EXIF Metadata Viewing

For this, we want to use the 'exif' module. Let's try viewing the metadata of "sample3.jpg"

`./tampr.py exif 'samples/exif/sample1.jpg'`

This should print out something similar to:
```
$ ./tampr.py exif 'samples/exif/sample1.jpg'
Image: samples/exif/sample1.jpg
Section: 0th
  ImageDescription: b'DCIM/100MEDIA/DJI_0002.JPG'
  Make: b'DJI'
  Model: b'FC1102'
  Orientation: 1
  XResolution: (72, 1)
  YResolution: (72, 1)
  ResolutionUnit: 2
  Software: b'GIMP 2.10.8'
  DateTime: b'2019:03:27 01:43:18'
  YCbCrPositioning: 1
  ExifOffset: 242
  GPSInfo: 1134
----------------------------------------
(...)
```

## EXIF Metadata Editing
For this, we want to use the 'exif' module. Let's try editing the metadata of "sample3.jpg"

First, we want to see what some of the metadata keys are, so let's run

`./tampr.py exif 'samples/exif/sample3.jpg'`

This should print out something similar to:
```
$ ./tampr.py exif 'samples/exif/sample3.jpg'
Image: samples/exif/sample3.jpg
Section: 0th
  ImageWidth: 4032
  ImageLength: 3024
  Make: b'Google'
  Model: b'Pixel 3 XL'
  Orientation: 6
  XResolution: (72, 1)
  YResolution: (72, 1)
  ResolutionUnit: 2
  Software: b'HDR+ 1.0.300173574zdh'
  DateTime: b'2020:03:28 20:23:27'
  YCbCrPositioning: 1
  ExifOffset: 246
  GPSInfo: 21413
----------------------------------------
(...)
```
Let's try changing the "Make" and "Model" of the picture to make it look like it was taken using an iPhone 11 Pro
```
$ ./tampr.py exif edit 'samples/exif/sample3.jpg' Make 'Apple'
Image: samples/exif/sample3.jpg
Old value:
  Make: b'Google'
New value:
  Make: b'Apple'
  ```
```
$ ./tampr.py exif edit 'samples/exif/sample3.jpg' Model 'iPhone 11 Pro'
Image: samples/exif/sample3.jpg
Old value:
  Model: b'Pixel 3 XL'
New value:
  Model: b'iPhone 11 Pro'
  ```

## File hash checking
For this, we want to use the 'hash' module. Let's try examining the hashes of plane.jpg and ship.jpg in samples/hash

Let's start by taking a look at plane.jpg by running:

`./tampr.py hash samples/hash/plane.jpg`

This should print out something like:
```
$ ./tampr.py hash samples/hash/plane.jpg 
File: samples/hash/plane.jpg
Hashes:
  md5: 253dd04e87492e4fc3471de5e776bc3d
  sha1: 780973c1c165e76de3f10e1771db31cf9362d1f5
  sha224: 247f332626e78d26917089bcd96053e19bcb76a92bf7e6858eed41f1
  sha256: 91e34644af1e6c36166e1a69d915d8ed5dbb43ffd62435e70059bc76a742daa6
  sha384: 2e0cc8f18143c94ed3c022035b3d6f4968d04b97e1287d7bfa600fc45cd69ff792cc812e34c4e61f04e13f3a27c5ccc4
  sha512: 6451d0a8082905f5910a981e89185446c3f03912bf0f62c216e082f0f37d51f2ec6735553590a550520483655165b022863d7e61b54a45534f37448493908e12
  blake2b: ea958574bebc9efea243ddb0ed5903da61b76af8feef32429bf0e96642e5cdd4bab2e2f8009b7735abe832d37a5efe0e2ffef477015c0b22f70da0779ed073e6
  blake2s: cb3d206fa0eca291845b401ccfbae1fc69bfa389b1e61a069e4cfea4e54a8ca0
```
Now that we know the hashes for plane.jpg, let's take a look at ship.jpg
```
$ ./tampr.py hash samples/hash/ship.jpg 
File: samples/hash/ship.jpg
Hashes:
  md5: 253dd04e87492e4fc3471de5e776bc3d
  sha1: 9639db1fbadfcfbd4025a9b95d10b7799f65fcfb
  sha224: 883696ef71737ef8a12b48a129f17140f4db04dcfbb4acf137c3b318
  sha256: caf110e4aebe1fe7acef6da946a2bac9d51edcd47a987e311599c7c1c92e3abd
  sha384: 7fe3867995ce283d06dc8b98c2bd99320e162ed29502861b2e2f71e1c6b611e48748c3347c5f7c9aeff738dda13d1bd1
  sha512: 434425fd7ad9ef91ab9805e1a87dc35ecfc4db00b085c4cf2d5984e1c10bda5d0c3b85499b9f362dcd66d389ad374ca16bfc902c45fb777a80f09b3b7a773e55
  blake2b: 10aa7a5d3acf49995d632a73e4946324ea331f4a656dc0c347908f804e2af2dd5278846f64e7e0464dd35c8e876a72840a6b768b6771c7e893ba0cdbc4822fb6
  blake2s: 02747c8b4b2552932a2121bfc8aa53d228d8ab81dfc14c9654c656ec140f9321
```

If you look closely, you may notice that these two files have the same md5 hash. MD5 is not a secure algorithm, and this type of situation is what's considered a "hash collision".
