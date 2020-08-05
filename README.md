# Chess Engine

Building a simple chess engine in Python

## Run these notebooks on the web Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MichaelAllen1966/2008_chess/)


## Run these notebooks on the web using BinderHub:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MichaelAllen1966/2008_chess/master)


## Dependencies to install manually

In addition to Python (I am using 3.7 for this) you will need to:

`pip install python-chess`


## Set up the anaconda environment locally

Alternatively, to get the same libraries and versions I am using then you may recreate the environment. To create and activate the `chess` environment used:

To create environment. Navigate to the `binder` folder.

`conda env create -f environment.yml`

To activate environment:

`conda activate chess`

To deactivate:

`conda deactivate`

To update environment (from updated yml file):

`conda env update --prefix ./env --file environment.yml  --prune`

To remove the environemnt:

`conda env remove -n chess`
