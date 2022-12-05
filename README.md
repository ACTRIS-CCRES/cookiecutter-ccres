# Quickstart

This repo is a `cookiecutter` template that creates a modern python project with a lot of [features](#features). It basically creates a repository based on custom information (e.g. author, organization etc) and init the repository with git.
## Prerequisites

In order to use this template you need to install Cookiecutter

```shell
pip install cookiecutter
```

You'll also need to have the following installed :
- `git`. See [Installation](https://git-scm.com/)
- `git-lfs`. See [Installation](https://git-lfs.github.com/)

If one or more of these packages are not installed, you will know what is missing by an error occurring during creation.

### Virtual environment

In order to create this template one should meet the prerequisites. To do so, you have many solutions :
- Install `cookiecutter` system-wide.
- Install `cookiecutter` in a virtual environment.

**`conda` installation**

Make sure you have conda installed by running `conda --version`. If the command is not installed, please see the [installation documentation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

You can then run :

```shell
conda create -n cookiecutter_env python=3.10
conda activate cookiecutter_env
pip install cookiecutter
```

**`venv` installation**

This method do not allow to create directly a virtual environment with a specific version of python. It uses the one of your system. You can check for the version with `python --version`. You can check `pyenv` software if you want to manage multiple `python` version.

Assuming that you have `python >= 3.10` installed, you can then run the following to create a python environment :

```shell
python -m venv cookiecutter_env
source cookiecutter_env/bin/activate
pip install cookiecutter
```

## Generate the Python package project:

### From the github url
```shell
cookiecutter https://github.com/ACTRIS-CCRES/cookiecutter-ccres -o <wherever you want>
```

### By cloning it
```shell
git clone https://github.com/ACTRIS-CCRES/cookiecutter-ccres
cookiecutter cookiecutter-ccres -o <wherever you want>
```

Then let yourself be guided by the command line interface.

### After creation

Go to the freshly created environment :
```
cd <name_of_your_repo>/
```
Then create an environment

**`venv`**
```
python -m venv <name_of_your_env>
source <name_of_your_env>/bin/activate
pip install -e .[dev]
```

**`conda`**
```
conda create -n <name_of_your_env> python=3.10
conda activate <name_of_your_env>
pip install -e .[dev]
```

Install the `pre-commit` hooks by running :
```
pre-commit install
```

You can then :
```
git add .
git commit -m "First commit"
```

> :information_source: Replace  `<name_of_your_repo>` and `<name_of_your_env>` by the corresponding name.


## Github Repo configuration
### Tokens
In order to pass the github workflows you'll need the following tokens in your github repo :
- `PYPI_TOKEN` -> You can get it [here](https://pypi.org/)
- `TEST_PYPI_TOKEN` -> You can get it [here](https://test.pypi.org/)

You can add them by following the steps in [this tutorial](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository)

### Sync with `readthedocs`

This step can not be automated easily with workflows, you need to follow [this tutorial](https://docs.readthedocs.io/en/stable/tutorial/#getting-started)

## Deep Further

Much more documentation on how to work with this template can be found in the `CONTRIBUTING.md` file.

## Features

-  git LFS integration : All files in tests/data and all netcdf file will be commited using the LFS storage.
- `pre-commit` integration : **19** `pre-commit` hooks
- `pyproject.toml` : Use of the latest packaging conventions for python see [PEP-621](https://peps.python.org/pep-0621/)
- `setuptools` build : Allow dynamic build if necessary
- `bump2version` : Automatically bump your version by calling bump2version <which> where which can be `major` / `minor` / `patch` / `release_candidate` / `dev`
- `pytest` : Unit-testing and coverage
- `sphinx` : For documentation testing
- `click` : command line interface
- `black` : Formatting
- `Dockerfile` for testing
- Numpy `docstring`
- Usual project files :
    - CHANGELOG.md
    - README.md with a lot of badges
    - CONTRIBUTING.md
    - LICENSE
- Github Specific files :
  - Workflows
    - pre-commit testing
    - Unit testing on Python 3.8, 3.9, 3.10, 3.11 and testing Windows / Mac-Os / Linux for Python 3.10
    - flake8
    - Coverage for badge
    - Automatic deployment on Test PyPI and PyPI
  - Templates
    - Issues
    - Pull request
- Conditional License choice
- Conditional typing. You can choose if you want your package to be typed.

## IDE extensions
We recommend to use VSCode thank to all the amazing tools and extensions it provides :
- Python
  - `black` formatter. You can configure format on save that saves a lot of time
- `autoDocstring`
- `gitLens`
- `isort`
