#!/usr/bin/python
# Script for creating an ebook cover thumbnail
# For use in Nautilus (GNOME Explorer)

import sys
import ebookmeta
from PIL import Image
from io import BytesIO
import urllib.request as urllib

# Set the thumbnail size (512px by default)
SIZE = 512

# Check the number of passed arguments
if len(sys.argv) < 2:
    # Not enough parameters
    sys.exit(1)

# Get input parameters
inputFile = sys.argv[1]  # Path to an e-book file
outputFile = sys.argv[2] # Path to save the thumbnail

# Convert the URL path to a regular file path
_file = urllib.url2pathname(inputFile).split('file://')[1]

try:
    # Get book metadata
    meta = ebookmeta.get_metadata(_file)
except Exception as e:
    # Error during metadata retrieval
    sys.exit(4)

# Checking for a cover exitence
if not meta.cover_image_data:
    #  Cover not found in book
    sys.exit(2)

try:
    # Open the cover image
    cover = Image.open(BytesIO(meta.cover_image_data))

    # Creating a thumbnail using Lanczos resampling algorithm
    cover.thumbnail((SIZE, SIZE), Image.Resampling.LANCZOS)

    # Save the result in PNG format
    cover.save(outputFile, "PNG")

    sys.exit(0)
except Exception as e:
    # Error creating a thumbnail
    sys.exit(5)
