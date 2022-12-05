#!/usr/bin/env python
import subprocess


def check_if_git_installed():
    return_code = subprocess.run(["git", "--version"]).returncode
    if return_code != 0:
        raise SystemError(
            "git does not seem installed. ",
            "Please see https://git-scm.com/ to install it",
        )


def check_if_lfs_is_installed():
    return_code = subprocess.run(["git", "lfs", "--version"]).returncode
    if return_code != 0:
        raise SystemError(
            "git LFS does not seem installed. ",
            "Please see https://git-lfs.github.com/ to install it",
        )


def main():
    check_if_git_installed()
    check_if_lfs_is_installed()


if __name__ == "__main__":
    main()
