from distutils.core import setup

setup (
    name = 'pi-sysinfo',
    version = '0.1.0',
    description = 'Displays basic system information on a Raspberry Pi',
    scripts = [ 'sysinfo' ],
    author = 'Vrai Stacey',
    author_email = 'vrai.stacey@gmail.com',
    url = 'http://github.com/vrai/pi-sysinfo',
    license = 'GPL',
    long_description = """\
Pretty much everyone who owns a Raspberry Pi has written a script to dump all
the useful system information in one go; this one is mine.

It takes no arguments and dumps the following to stdout:
  - CPU and GPU temperatures in centigrade
  - CPU voltage (with separate over-voltage component when present)
  - CPU minimum, maximum and current frequencies
  - CPU frequency governor mode and upscale threshold
  - Hostname and any non-loopback IP addresses
  - Firmware date and version
  - Enabled and disabled media codecs. """ )
# vim: ft=python:sw=4:ts=4:et
