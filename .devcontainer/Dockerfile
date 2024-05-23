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

COPY /.devcontainer/libgfortran-1.0-0.tar.bz2 /root 
RUN conda install --offline libgfortran-1.0-0.tar.bz2

RUN yes | conda install numpy \
    && conda install pandas \
    && conda install biopython \
    && conda install functools_lru_cache \
    && conda install jupyter \
    && conda install decorator=4.4.1 

RUN yes | apt-get install python-dev

COPY ViennaRNA-2.3.5.tar.gz /root
RUN tar -xzvf ViennaRNA-2.3.5.tar.gz
WORKDIR /root/ViennaRNA-2.3.5/
RUN ./configure --without-perl --without-python3 --with-python2
RUN make && make check && make install && make clean

WORKDIR /root
