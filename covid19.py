#!/usr/bin/env python
"""covid19 v%s

Plots current COVID-19 situation.

Usage:
  covid19 [options]

Options:
  -c COUNTRIES, --countries COUNTRIES  : Comma-separated Geo IDs (e.g. CN,IT)
      or [default: all] or "top"
  -k KEY, --key KEY  : [default: new_deaths]|new_cases.
  -o PATH, --output PATH  : Output path [default: COVID-19.png].
      Can be *.txt (use stdout.txt for stdout).
  -i PATH, --input PATH  : Input data path [default: COVID-19.csv].
  --log LEVEL  : (FAT|CRITIC)AL|ERROR|WARN(ING)|[default: INFO]|DEBUG|NOTSET

%s
"""
from __future__ import print_function
import logging
import sys

from argopt import argopt
import pandas as pd

__all__ = ["main", "run"]
__version__ = "1.1.0"
__author__ = "Casper da Costa-Luis <casper.dcl@physics.org>"

log = logging.getLogger(__name__)


def get_top_iso_codes(df, key="new_cases", top=10):
    ids = (
        df.groupby("iso_code")
        .aggregate({"new_cases": sum, "new_deaths": sum})
        .nlargest(top, key)
    )
    return list(ids.index)


def run_text(df, output, countries):
    if "ALL" not in countries:
        df = df[df["iso_code"].apply(lambda x: x in countries)]
    sums = df.groupby("iso_code").aggregate({"new_cases": sum, "new_deaths": sum})

    if output[:-4].lower() in ("stdout", "-"):
        fd = sys.stdout
        fd_close = lambda: None
    else:
        fd = open(output, "w")
        fd_close = fd.close

    try:
        print("ID Date            Cases( change)    Deaths(chnge)", file=fd)
        for country in countries:
            if country == "ALL":
                totals = df.groupby("date").aggregate({"new_cases": sum, "new_deaths": sum})
                last = totals.iloc[-2]
                print(
                        "-- {last.name:%Y-%m-%d} {tot[new_cases]:>10,.0f}({last[new_cases]:>7,.0f}) {tot[new_deaths]:>9,.0f}({last[new_deaths]:>5,.0f})".format(
                        last=last, tot=totals.sum(),
                    ),
                    file=fd,
                )
                continue

            last = df[df["iso_code"] == country].nlargest(1, "date").iloc[0]
            print(
                "{country:.2s} {last[date]:%Y-%m-%d} {tot[new_cases]:>10,.0f}({last[new_cases]:>7,.0f}) {tot[new_deaths]:>9,.0f}({last[new_deaths]:>5,.0f})".format(
                    country=country, last=last, tot=sums.loc[country],
                ),
                file=fd,
            )
    finally:
        fd_close()


def run(args):
    """@param args: RunArgs"""
    input_type = {"csv": "csv", "xlsx": "excel"}[args.input.rsplit('.')[1]]
    dtype={i: "Int32" for i in ["total_cases", "new_cases", "total_deaths", "new_deaths"]}
    dtype.update({"population": "Int64"})
    df = getattr(pd, 'read_' + input_type)(
        args.input, parse_dates=["date"], dtype=dtype,
        encoding="UTF-8", error_bad_lines=False)
    df = df[df.iso_code != "OWID_WRL"]
    for i in ("new_cases", "new_deaths"):
        df[i] = df[i].fillna(0)
    countries = args.countries.upper().split(",") or ["ALL"]
    while "TOP" in countries:
        i = countries.index("TOP")
        countries = countries[:i] + get_top_iso_codes(df, key=args.key.lower()) + countries[i + 1 :]

    # text-only of latest data
    if args.output.lower().endswith(".txt"):
        run_text(df, args.output, countries)
        return

    if countries == ["ALL"]:
        # world summary
        title = "World"
        cum = df.groupby("date").aggregate({"new_cases": sum, "new_deaths": sum})
    elif len(countries) == 1 and countries[0] != "TOP":
        # single country
        title = countries[0]
        cum = (
            df[df["iso_code"] == countries[0]]
            .groupby("date")
            .aggregate({"new_cases": sum, "new_deaths": sum})
        )
    else:
        # multiple countries
        title = args.key.lower()
        idx = df["iso_code"].apply(lambda x: x in countries)
        cum = df[idx]

    # plot data
    import matplotlib.pyplot as plt
    from datetime import datetime, timedelta
    from pandas.plotting import register_matplotlib_converters
    register_matplotlib_converters()

    plt.figure(figsize=(16, 9), dpi=90)

    if title == args.key.lower():
        key = title
        for country, ls, m in zip(
            countries, ["-", "--", "-.", ":"] * 99, ".,ov^<>1234sp*hH+xDd|_"
        ):
            i = cum[cum["iso_code"] == country]
            plt.semilogy(i["date"], i[key], label=country, ls=ls, marker=m)
            plt.title(title)
    else:
        for key in ("new_cases", "new_deaths"):
            plt.semilogy(cum[key], label=key)

    plt.title(title)
    t1 = datetime.now()
    # t0 = t1 - timedelta(7 * 52)
    plt.xlim(None, t1)
    # xticks = [t1 - timedelta(7 * i) for i in range(52, -1, -1)]
    # plt.xticks(xticks, map("{:%d %b}".format, xticks))
    plt.legend()
    plt.tight_layout()
    plt.savefig(args.output)


def main(argv=None):
    """argv  : list, optional (default: sys.argv[1:])"""
    args = argopt(__doc__ % (__version__, __author__), version=__version__).parse_args(
        args=argv
    )
    logging.basicConfig(level=getattr(logging, args.log, logging.INFO))
    log.debug(args)
    return run(args) or 0


if __name__ == "__main__":
    main()
