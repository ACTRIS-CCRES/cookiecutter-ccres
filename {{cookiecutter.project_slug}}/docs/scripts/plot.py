"""This script allow to create plot when building the docs
You can then access to your plot through the docs.

For doing this, the make_plots function is called in the conf.py directory.
"""
import os

BASE_DIR = os.path.dirname(__file__)
EXPORT_FOLDER = os.path.join(BASE_DIR, "..", "source", "assets", "plots")


def doc_plot():
    """doc_plot You can generate plot when building docs
    and save it in EXPORT_FOLDER.
    """


def make_plots():
    os.makedirs(EXPORT_FOLDER, exist_ok=True)
    doc_plot()


if __name__ == "__main__":
    make_plots()
