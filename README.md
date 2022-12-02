# Quickstart
## Prerequisites

In order to use this template you nedd to install Cookiecutter

```shell
pip install cookiecutter
```

You'll also need to have the following installed :
- `git`. See [Installation](https://git-scm.com/)
- `git-lfs`. See [Installation](https://git-lfs.github.com/)
- `pre-commit`. See [Installation](https://pre-commit.com/)

If one or more of these packages are not installed, you will know what is missing by an error occurring during creation
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
## Generate the Python package project:

### From the github url
```shell
cookiecutter https://github.com/ACTRIS-CCRES/cookiecutter-ccres  <wherever you want>
```

### By cloning it
```shell
git clone https://github.com/ACTRIS-CCRES/cookiecutter-ccres
cookiecutter cookiecutter-ccres -o <wherever you want>
```

Then let yourself be guided by the command line interface.

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
