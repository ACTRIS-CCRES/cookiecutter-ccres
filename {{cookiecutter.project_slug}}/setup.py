"""The setup script."""
import os

from setuptools import find_packages, setup

long_description = "ACTRIS weather station converter"
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

test_requirements = ['pytest>=3']

{%- set license_classifiers = {
    "GNU Affero General Public License v3.0":"License :: OSI Approved :: GNU Affero General Public License v3",
    "Apache License 2.0":"License :: OSI Approved :: Apache Software License",
    "BSD 2-Clause \"Simplified\" License":"License :: OSI Approved :: BSD License",
    "BSD 3-Clause \"New\" or \"Revised\" License":"License :: OSI Approved :: BSD License",
    "Creative Commons Zero v1.0 Universal":"License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    "GNU General Public License v2.0":"License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    "GNU General Public License v3.0":"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "GNU Lesser General Public License v2.1":"License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
    "MIT License":"License :: OSI Approved :: MIT License",
    "Mozilla Public License 2.0":"License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
} %}

setup(
    author="{{ cookiecutter.author.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: Implementation :: CPython'
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="{{ cookiecutter.project_short_description }}",
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli.cli:main',
        ],
    },
    install_requires=requirements,
{%- if cookiecutter.license in license_classifiers %}
    license="{{ cookiecutter.license }}",
{%- endif %}
    long_description=long_description,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
