#
# Dockerfile
#
# Copyright (c) 2015 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
FROM ubuntu:latest
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>

# Install packages
RUN apt-get update && \
    apt-get install -y make python-pip python-mysqldb python-networkx \
                        python-numpy python-scipy python-matplotlib \
                        graphviz

RUN pip install --upgrade sphinx

# Copy entrypoint
COPY bin /root/

# Change working directory
VOLUME /data

ENTRYPOINT ["/root/entrypoint.py"]
