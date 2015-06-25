A docker container for Sphinx
==============================

This docker image contains `make` command for Sphinx. When your Sphinx source codes are in `/data`, you may compile them and obtain html documents with a docker container.

```sh
$ docker run --rm -v /data:/data jkawamoto/sphinx-make --cwd /data
```

If you also need LaTeX documents, you can obtain it, too.

```sh
$ docker run --rm -v /data:/data jkawamoto/sphinx-make --cwd /data latex
```


Arguments
------------
The container has the following arguments.

```
docker run jkawamoto/sphinx-make [--cwd CWD] [params [params ...]]

positional arguments:
  params      specify options of make (default: html).

optional arguments:
  -h, --help  show this help message and exit
  --cwd CWD   specify a directory containing Makefile.
```


License
--------
This software is released under the MIT License, see LICENSE.
