A docker container for Sphinx
===============================

Install
---------
```sh
docker pull jkawamoto/sphinx-make
```

Usage
------

```
docker run jkawamoto/sphinx-make [--cwd CWD] [params [params ...]]

positional arguments:
  params      Specify options of make (default: html).

optional arguments:
  -h, --help  show this help message and exit
  --cwd CWD   Specify a directory containing Makefile.
```


License
--------
This software is released under the MIT License, see LICENSE.
