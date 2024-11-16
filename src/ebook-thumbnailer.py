#!/usr/bin/python

import sys
import ebookmeta
from PIL import Image
from io import BytesIO
import urllib.request as urllib

# Not enough actual parameters
if len(sys.argv) < 2:
    sys.exit(1)

inputFile = sys.argv[1]
outputFile = sys.argv[2]
if len(sys.argv) > 3:
    size = int(sys.argv[3])
else:
    size = 512

_file = urllib.url2pathname(inputFile).split('file://')[1]
meta = ebookmeta.get_metadata(_file)

# No cover inside
if not meta.cover_image_data:
    sys.exit(2)

cover = Image.open(BytesIO(meta.cover_image_data))
cover.thumbnail((size, size), Image.Resampling.LANCZOS)
cover.save(outputFile, "PNG")
sys.exit(0)
