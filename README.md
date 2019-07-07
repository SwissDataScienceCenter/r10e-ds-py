# Reproducible Data Science in Python (SciPy 2019 Tutorial)

Materials for the [Reproducible Data Science in Python](https://www.scipy2019.scipy.org/tutorial/Reproducible-Data-Science-in-Python) tutorial at SciPy 2019.

Presenters: Ramakrishnan Chandrasekhar (Renku) and Xu Fei (Code Ocean)

# Versions

| Date       | Change                                               |
| ---------- | ---------------------------------------------------- |
| 2019-06-18 | Initial version                                      |
| 2019-06-25 | Added instructions for windows                       |
| 2019-07-01 | Updated environment.yml to work on conda 4.7 and 4.6 |
| 2019-07-02 | Updated environment.yml to work be cross-platform    |
| 2019-07-04 | Added dot as a dependency                            |


# Description

The expectation of reproducibility in scientific work has been long established, and, increasingly, communities and funding sources are actually demanding it. Within the Python ecosystem, there are a variety of tools available to support reproducible data science, but choosing and using one is not always straightforward. In this tutorial, we will take a closer look at the concept of _reproducibility_, and, we will examine the technologies that provide building blocks and survey the landscape of tools. We spend the majority of the time looking at two solutions in particular, [Renku](https://renkulab.io) and [Code Ocean](https://codeocean.com), and work through end-to-end scenarios in both.

# Set Up

To avoid conflicts in dependencies, we recommend creating a dedicated environment for this tutorial. You can do this using any tool you like, for example [pipenv](https://pipenv.readthedocs.io/en/latest/) or [conda](https://docs.conda.io/en/latest/miniconda.html). We provide instructions based on conda here. If you use docker, we also provide a Dockerfile with [instructions for set up and use](README-docker.md). If you prefer to use something else, you will need to ensure that `git`, `git-lfs`, `curl`, and `node` are installed in your environment, but you should be able to pip install the requirements.txt file for the rest.

## Step 1: Create Environment

**Create environment using conda**

0. If you do not yet have conda, you should first [install miniconda for your platform](https://conda.io/miniconda.html)
1. Download the [conda environment](https://raw.githubusercontent.com/SwissDataScienceCenter/r10e-ds-py/master/environment.yml)
2. In the directory where `environment.yml` is located, execute `conda env create`

**Verifying the setup**
1. Activate the environment with `conda activate r10eds`
2. Run `git --version` -- the result should be "git version 2.21.0" (or newer)
3. Run `git lfs --version` -- the result should be "git-lfs/2.7.1" (or newer)
4. Run `renku --version` -- the result should be "0.5.0" (or newer)

**Additional setup on Windows**
On Windows, an additional step is necessary. Renku creates symbolic links, and on Windows it is necessary to have privileges in order to do that. Follow these instructions from from [StackExchange/Super User](https://superuser.com/questions/124679/how-do-i-create-a-link-in-windows-7-home-premium-as-a-regular-user/125981#125981) to give your user these privileges.

## Step 2: Clone the tutorial repository

1. Activate the environment with `conda activate r10eds`
2. Clone the repository `git clone https://github.com/SwissDataScienceCenter/r10e-ds-py.git`

# Run the tutorial

Once you have the environment set up and repository cloned, you can use them.

0. cd into the tutorial repository `cd r10e-ds-py`
1. Activate the environment with `conda activate r10eds`
2. Start jupyter lab `jupyter lab` (you can also use plan jupyter)


### Optional Components

If you wish, you can install [Docker Desktop](https://www.docker.com/products/docker-desktop). It is not a requirement, but it will make it possible to dig deeper into certain areas in the tutorial.


# Schedule

<table style="font-size: 14px; margin: 10px;">
    <tbody>
        <tr>
            <th>Introduction (1h)</th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>15 min</th>
            <td>Background &amp; Theory</td>
            <td style="text-align: left">Terminology, history, and philosophy of reproducibility</td>
        </tr>
        <tr>
            <th>30 min</th>
            <td>Building Blocks</td>
            <td style="text-align: left">Building blocks for achieving reproducibility</td>
        </tr>
        <tr>
            <th>15 min</th>
            <td>Tools</td>
            <td style="text-align: left">Survey of the current tool landscape</td>
        </tr>
        <tr>
            <th></th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>Break (10 min)</th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th></th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>Hands-on with Renku (1h 30m)</th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>30 min</th>
            <td>Starting</td>
            <td style="text-align: left">Starting a project, importing data, building a workflow</td>
        </tr>
        <tr>
            <th>30 min</th>
            <td>Iterating</td>
            <td style="text-align: left">Updating code and data to improve analysis</td>
        </tr>
        <tr>
            <th>30 min</th>
            <td>Details and Reflection</td>
            <td style="text-align: left">What is the benefit? How much effort was it? How do we view, share, and reuse artifacts? How do things work under the covers?</td>
        </tr>
        <tr>
            <th></th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>Break (20 min)</th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th></th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>Hands-on with Code Ocean (1h)</th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>10 min</th>
            <td>Demo of a Compute Capsule</td>
            <td style="text-align: left">Intro to Code Ocean and its design philosophy</td>
        </tr>
        <tr>
            <th>30 min</th>
            <td>Creating a Compute Capsule</td>
            <td style="text-align: left">Create a reproducible compute capsule using code and data from the existing Renku project. We will explore options to publish, collaborate, import from Github, export to local server, etc.</td>
        </tr>
        <tr>
            <th>15 min</th>
            <td>Q&A, Wrap up</td>
            <td style="text-align: left">Any questions that you want to ask</td>
        </tr>
     </tbody>
</table>

# Acknowledgements

Many thanks to Erica Moreira, Laura Levin-Gleba, and Maja Garbulinksa from the Harvard School of Public Health for their helpful comments and suggestions!

The icons used are from [Icons8](https://icons8.com/).
