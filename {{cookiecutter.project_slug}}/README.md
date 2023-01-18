{% set is_open_source = cookiecutter.license != "Not Open Source" -%}
# {{ cookiecutter.project_name }}


{%- set LICENSE_BADGES = {
    "GNU Affero General Public License v3.0": {
        "link": "https://www.gnu.org/licenses/agpl-3.0",
        "badge": "https://img.shields.io/badge/License-AGPL_v3-blue.svg",
    },
    "Apache License 2.0": {
        "link": "https://opensource.org/licenses/Apache-2.0",
        "badge": "https://img.shields.io/badge/License-Apache_2.0-blue.svg",
    },
    'BSD 2-Clause "Simplified" License': {
        "link": "https://opensource.org/licenses/BSD-2-Clause",
        "badge": "https://img.shields.io/badge/License-BSD_2--Clause-orange.svg",
    },
    'BSD 3-Clause "New" or "Revised" License': {
        "link": "https://opensource.org/licenses/BSD-3-Clause",
        "badge": "https://img.shields.io/badge/License-BSD_3--Clause-blue.svg",
    },
    "Boost Software License 1.0": {
        "link": "https://www.boost.org/LICENSE_1_0.txt",
        "badge": "https://img.shields.io/badge/License-Boost_1.0-lightblue.svg)",
    },
    "Creative Commons Zero v1.0 Universal": {
        "link": "http://creativecommons.org/publicdomain/zero/1.0/",
        "badge": "https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg",
    },
    "Eclipse Public License 2.0": {
        "link": "https://www.eclipse.org/legal/epl-2.0/",
        "badge": "https://img.shields.io/badge/License-EPL_2.0-red.svg",
    },
    "GNU General Public License v2.0": {
        "link": "https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html",
        "badge": "https://img.shields.io/badge/License-GPL_v2-blue.svg",
    },
    "GNU General Public License v3.0": {
        "link": "https://www.gnu.org/licenses/gpl-3.0",
        "badge": "https://img.shields.io/badge/License-GPLv3-blue.svg",
    },
    "GNU Lesser General Public License v2.1": {
        "link": "https://www.gnu.org/licenses/lgpl-2.0",
        "badge": "https://img.shields.io/badge/License-LGPL_v2-blue.svg",
    },
    "MIT License": {
        "link": "https://opensource.org/licenses/MIT",
        "badge": "https://img.shields.io/badge/License-MIT-yellow.svg",
    },
    "Mozilla Public License 2.0": {
        "link": "https://opensource.org/licenses/MPL-2.0",
        "badge": "https://img.shields.io/badge/License-MPL_2.0-brightgreen.svg",
    },
}%}


<p align="center">
    <a href="{{ cookiecutter.github_repo_url }}/actions"><img alt="CI Status" src="{{ cookiecutter.github_repo_url }}/actions/workflows/ci.yaml/badge.svg?branch=main"></a>
    <a href="https://{{ cookiecutter.project_slug | replace('_', '-') }}.readthedocs.io/en/latest/?version=latest"><img alt="Documentation Status" src="https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace('_', '-') }}"></a>
    <a href="https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}"><img alt="PyPI" src="(https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg"></a>
    <a href="{{ cookiecutter.github_repo_url }}"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
    <a href="https://codecov.io/gh/{{cookiecutter.github_username_or_project}}/{{ cookiecutter.project_slug }}"><img alt="Coverage Status" src="https://codecov.io/gh/{{cookiecutter.github_username_or_project}}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg"></a>
    {%- if cookiecutter.license in LICENSE_BADGES %}
    <a href="{{ LICENSE_BADGES[cookiecutter.license]['link'] }}"><img alt="License: {{cookiecutter.license}}" src="{{ LICENSE_BADGES[cookiecutter.license]['badge'] }}"></a>
    {%- endif %}
</p>

{{ cookiecutter.project_short_description }}

- License: {{ cookiecutter.license }}
- Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
