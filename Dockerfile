FROM continuumio/miniconda3:4.6.14

WORKDIR /r10eds
COPY ./environment.yml /r10eds

RUN conda env create
