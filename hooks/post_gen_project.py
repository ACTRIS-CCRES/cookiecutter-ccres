#!/usr/bin/env python
import subprocess
import shutil

# Cannot use a constants.py file because this script is alone
# in a tmp folder. It need to be self consistent

LICENSE_TEMPLATE = "./LICENSE"
LICENSES_DIR = "./LICENSES"
ARG = "license"


def remove_folder_license():
    shutil.rmtree(LICENSES_DIR)


error_prefix = "Something went wrong"


def git_init():
    print("Init git repository")
    return_code = subprocess.run(["git", "init"]).returncode
    if return_code != 0:
        raise SystemError(f"{error_prefix} initializing the git repo")


def git_lfs_install():
    print("Init git LFS")
    return_code = subprocess.run(["git", "lfs", "install"]).returncode
    if return_code != 0:
        raise SystemError(f"{error_prefix} installing git LFS")


def main():
    remove_folder_license()
    git_init()
    git_lfs_install()


if __name__ == "__main__":
    main()
