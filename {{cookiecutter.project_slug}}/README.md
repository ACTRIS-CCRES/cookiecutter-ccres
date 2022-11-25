{% set is_open_source = cookiecutter.license != "Not Open Source" -%}
# {{ cookiecutter.project_name }}

![https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)
![https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}]( https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg)
![https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest]( https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)

{{ cookiecutter.project_short_description }}

- License: {{ cookiecutter.license }}
- Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
