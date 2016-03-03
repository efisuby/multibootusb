#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from distutils.core import setup
import os
import sys

mbusb_version = open(os.path.join("tools", "version.txt"), 'r').read().strip()
setup(
    name='multibootusb',
    version=mbusb_version,
    packages=['scripts', 'scripts.pyudev', 'scripts.gui'],
    scripts=['multibootusb'],
    platforms=['Linux'],
    url='http://multibootusb.org/',
    license='General Public License (GPL)',
    author='Sundar',
    author_email='feedback.multibootusb@gmail.com',
    description='Create multi boot live Linux on a USB disk...',
    long_description='multibootusb is an advanced cross-platform application for installing/uninstalling Linux operating systems on to a single USB flash drives.',
    data_files=[("/usr/share/applications", ["data/multibootusb.desktop"]),
                ('/usr/share/pixmaps', ["data/multibootusb.png"]),
                (os.path.join(sys.prefix, "multibootusb", "tools"), ["tools/mbr.bin"]),
                (os.path.join(sys.prefix, "multibootusb", "tools"), ["tools/version.txt"]),
                (os.path.join(sys.prefix, "multibootusb", "tools"), ["tools/multibootusb.png"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "dd"), ["tools/dd/dd.exe"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "dd"), ["tools/dd/diskio.dll"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "multibootusb"), ["tools/multibootusb/chain.c32"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "multibootusb"), ["tools/multibootusb/bg.png"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "multibootusb"), ["tools/multibootusb/extlinux.cfg"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "multibootusb"), ["tools/multibootusb/grub.exe"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "multibootusb"), ["tools/multibootusb/memdisk"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "multibootusb"), ["tools/multibootusb/menu.c32"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "multibootusb"), ["tools/multibootusb/menu.lst"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "multibootusb"), ["tools/multibootusb/syslinux.cfg"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "multibootusb"), ["tools/multibootusb/vesamenu.c32"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/1024.ext4.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/2048.ext4.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/2048.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/3072.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/512.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/1024.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/256.ext4.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/3072.ext4.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/4096.ext4.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/768.ext4.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/256.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/4096.ext4.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/512.ext4.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "persistence_data"), ["tools/persistence_data/768.tar.bz2"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "syslinux"), ["tools/syslinux/syslinux_modules.zip"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "syslinux"), ["tools/syslinux/syslinux_linux.zip"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "syslinux"), ["tools/syslinux/syslinux_linux_64.zip"]),
                (os.path.join(sys.prefix, "multibootusb", "tools", "syslinux"), ["tools/syslinux/syslinux_windows.zip"])]
)

