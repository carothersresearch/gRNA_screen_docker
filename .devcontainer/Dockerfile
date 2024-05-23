FROM ubuntu:xenial-20160422
USER root
RUN apt-get update && apt-get install build-essential -y

RUN apt-get install -y ca-certificates 
RUN update-ca-certificates --fresh 
RUN SSL_CERT_DIR=/etc/ssl/certs

# miniconda
# Install miniconda
ENV CONDA_DIR /opt/conda
COPY Miniconda-latest-Linux-x86_64.sh /root 
RUN /bin/bash /root/Miniconda-latest-Linux-x86_64.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

WORKDIR /root

COPY /.devcontainer/*.bz2 /root 

COPY /.devcontainer/*_part_* /root
RUN cat mkl-11.3.1-0.tar_part_* > mkl-11.3.1-0_v2.tar.bz2

RUN conda install --offline libgfortran-1.0-0.tar.bz2 \
    && conda install --offline mkl-11.3.1-0.tar.bz2 \
    && conda install --offline numpy-1.10.4-py27_1.tar.bz2 \
    && conda install --offline pytz-2016.2-py27_0.tar.bz2 \
    && conda install --offline six-1.10.0-py27_0.tar.bz2 \
    && conda install --offline pandas-0.18.0-np110py27_0.tar.bz2 \
    && conda install --offline python-dateutil-2.5.1-py27_0.tar.bz2 \
    && conda install --offline biopython-1.66-np110py27_0.tar.bz2 \
    && conda install --offline linux-64_functools_lru_cache-1.4-hf48f6e4_0.tar.bz2 \
    && conda install --offline libpng-1.6.17-0.tar.bz2 \
    && conda install --offline libsodium-1.0.3-0.tar.bz2 \
    && conda install --offline freetype-2.5.5-0.tar.bz2 \
    && conda install --offline libxml2-2.9.2-0.tar.bz2 \
    && conda install --offline zeromq-4.1.3-0.tar.bz2 \
    && conda install --offline backports_abc-0.4-py27_0.tar.bz2 \
    && conda install --offline decorator-4.0.9-py27_0.tar.bz2 \
    && conda install --offline fontconfig-2.11.1-5.tar.bz2 \
    && conda install --offline ipython_genutils-0.1.0-py27_0.tar.bz2 \
    && conda install --offline jsonschema-2.4.0-py27_0.tar.bz2 \
    && conda install --offline markupsafe-0.23-py27_0.tar.bz2 \
    && conda install --offline mistune-0.7.2-py27_0.tar.bz2 \
    && conda install --offline path.py-8.1.2-py27_1.tar.bz2 \
    && conda install --offline ptyprocess-0.5-py27_0.tar.bz2 \
    && conda install --offline pygments-2.1.1-py27_0.tar.bz2 \
    && conda install --offline pyzmq-15.2.0-py27_0.tar.bz2 \
    && conda install --offline simplegeneric-0.8.1-py27_0.tar.bz2 \
    && conda install --offline sip-4.16.9-py27_0.tar.bz2 \
    && conda install --offline ssl_match_hostname-3.4.0.2-py27_0.tar.bz2 \
    && conda install --offline jinja2-2.8-py27_0.tar.bz2 \
    && conda install --offline pexpect-4.0.1-py27_0.tar.bz2 \
    && conda install --offline pickleshare-0.5-py27_0.tar.bz2 \
    && conda install --offline qt-4.8.7-1.tar.bz2 \
    && conda install --offline singledispatch-3.4.0.3-py27_0.tar.bz2 \
    && conda install --offline traitlets-4.2.1-py27_0.tar.bz2 \
    && conda install --offline ipython-4.1.2-py27_1.tar.bz2 \
    && conda install --offline jupyter_core-4.1.0-py27_0.tar.bz2 \
    && conda install --offline pyqt-4.11.4-py27_1.tar.bz2 \
    && conda install --offline tornado-4.3-py27_0.tar.bz2 \
    && conda install --offline jupyter_client-4.2.2-py27_0.tar.bz2 \
    && conda install --offline nbformat-4.0.1-py27_0.tar.bz2 \
    && conda install --offline terminado-0.5-py27_1.tar.bz2 \
    && conda install --offline ipykernel-4.3.1-py27_0.tar.bz2 \
    && conda install --offline nbconvert-4.1.0-py27_0.tar.bz2 \
    && conda install --offline jupyter_console-4.1.1-py27_0.tar.bz2 \
    && conda install --offline notebook-4.1.0-py27_1.tar.bz2 \
    && conda install --offline qtconsole-4.2.0-py27_0.tar.bz2 \
    && conda install --offline ipywidgets-4.1.1-py27_0.tar.bz2 \
    && conda install --offline jupyter-1.0.0-py27_2.tar.bz2 \
    && conda install --offline noarch_decorator-4.4.1-py_0.tar.bz2

RUN yes | apt-get install python-dev

COPY ViennaRNA-2.3.5.tar.gz /root
RUN tar -xzvf ViennaRNA-2.3.5.tar.gz
WORKDIR /root/ViennaRNA-2.3.5/
RUN ./configure --without-perl --without-python3 --with-python2
RUN make && make check && make install && make clean

WORKDIR /root
