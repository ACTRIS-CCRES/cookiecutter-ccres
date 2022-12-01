#!/usr/bin/env python
import subprocess


def git_init():
    print("Init git repository")
    subprocess.run(["git", "init"])


def git_lfs_install():
    print("Init git LFS")
    subprocess.run(["git", "lfs", "install"])


def precommit_install():
    print("Install pre-commit hooks")
    subprocess.run(["pre-commit", "install"])


def git_add_all():
    print("Add all files")
    subprocess.run(["git", "add", "."])


def run_precommit():
    print("Run precommit")
    subprocess.run(["pre-commit"])


def git_first_commit():
    print("init git repository")
    subprocess.run(["git", "commit", "-m", '"First commit"'])


def main():
    git_init()
    git_lfs_install()
    precommit_install()
    git_add_all()
    run_precommit()
    git_first_commit()


if __name__ == "__main__":
    main()
