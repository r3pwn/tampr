# Tampr

## EXIF Metadata Viewing

For this, we want to use the 'exif' module. Let's try viewing the metadata of "sample3.jpg"
`./tampr.py exif 'samples/exif/sample3.jpg'`
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
