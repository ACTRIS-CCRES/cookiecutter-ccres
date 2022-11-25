import datetime as dt
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr

BASE_DIR = os.path.dirname(__file__)
EXPORT_FOLDER = os.path.join(BASE_DIR, "..", "source", "assets", "plots")
# Do not modify this
DAY_DATE_FORMAT = "%Y%m%d"

DAY_DATE_BEG = "20100101"
DAY_DATE_END = "20100102"
DAY_DATE_BEG_DT = dt.datetime.strptime(DAY_DATE_BEG, DAY_DATE_FORMAT)
DAY_DATE_END_DT = dt.datetime.strptime(DAY_DATE_END, DAY_DATE_FORMAT)
DATE_FREQ = "15T"
DIM_TIME = "time"
MAIN_VARIABLE = "values"


def create_dataset():
    date_beg = dt.datetime.strptime(DAY_DATE_BEG, DAY_DATE_FORMAT)
    date_end = dt.datetime.strptime(DAY_DATE_END, DAY_DATE_FORMAT)

    time = pd.date_range(date_beg, date_end, freq=DATE_FREQ)
    cos_factor = pd.Timedelta(DATE_FREQ).seconds / 3600
    values = np.cos(cos_factor * np.array(range(len(time))))
    ds = xr.Dataset({MAIN_VARIABLE: ([DIM_TIME], values)}, coords={DIM_TIME: time})
    return ds


def doc_plot():
    ds = create_dataset()

    _, ax = plt.subplots(1, 1, figsize=(16, 9))

    ax[0].set_title("Example plot")
    ax[0].plot(
        ds[DIM_TIME], ds[MAIN_VARIABLE], marker="o", markersize=4, label="1D variable"
    )

    plt.subplots_adjust(hspace=0.25)
    plt.savefig(os.path.join(EXPORT_FOLDER, "minmax_check.png"))


def make_plots():
    plt.style.use(os.path.join(os.path.dirname(__file__), "default.mplstyle"))
    os.makedirs(EXPORT_FOLDER, exist_ok=True)
    doc_plot()


if __name__ == "__main__":
    make_plots()
