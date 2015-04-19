Cirdan
======

This software is a tool to easily create and manage LXC unprivileged containers. The containers are owned by root and use a LVM backend. Cirdan needs LXC 1.0.7 at least and has been tested on Debian Jessie.

Install
-------

Use `./autogen` followed by the famous triptych `./configure`, `make` and `make install`.

Configure
---------

The main configuration file is `cirdan.conf` that is located in `/usr/local/etc/cirdan` by default. Before creating any container, you should really tweak it. Please, read the comments to set the variables according to your needs.

Issues
------

If you encounter any problem with this software, do not hesitate to report it in a [GitHub issue][1].


  [1]: https://github.com/Meseira/cirdan/issues
