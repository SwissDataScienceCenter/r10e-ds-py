## Create an environment using docker

If you use docker, you can use the provided Dockerfile to create an environment for the tutorial. We assume you have git installed.

0. Clone the git repository `git clone https://github.com/SwissDataScienceCenter/r10e-ds-py.git`
1. Enter the directory `cd r10e-ds-py`
2. Build the dockerfile `docker build -t r10eds .`

## Use the docker environment

Execute
```bash
docker run --rm -it -p"8888:8888" -p"8889:8889" -v$(pwd):/r10eds r10eds
conda activate r10eds
jupyter lab --ip=0.0.0.0 --no-browser --allow-root
```
