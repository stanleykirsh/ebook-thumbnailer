ebook-thumbnailer
=================

A simple FB2 and EPUB thumbnailer for Nautilus.

How to install:

1) sudo ./install

How to install manually:

1) sudo pip install ebookmeta
2) Place the ebook-thumbnailer file in the /usr/share/thumbnailers directory.
Put ebook-thumbnailer.py in /usr/bin.

Don't forget to enable "Show Miniatures on All Devices" in Nautilus.

To work correctly with SAMBA drives, use the local path to which the SMB drive is mounted. For example: /mnt/nas.

How to test:

src/ebook-thumbnailer.py file://test.fb2 test.png