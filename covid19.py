#!/usr/bin/env python
"""covid19 v%s

Plots current COVID-19 situation.

Usage:
  covid19 [options]

Options:
  -c COUNTRIES, --countries COUNTRIES  : Comma-separated Geo IDs (e.g. CN,IT)
      or [default: all] or "top"
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
__version__ = "0.0.0"
__author__ = "Casper da Costa-Luis <casper.dcl@physics.org>"

log = logging.getLogger(__name__)


def get_top_geoIds(df, key="cases", top=10):
    ids = (
        df.groupby("geoId")
        .aggregate({"cases": sum, "deaths": sum})
        .nlargest(top, key)
    )
    return list(ids.index)


def run_text(df, output, countries):
    if "ALL" not in countries:
        df = df[df["geoId"].apply(lambda x: x in countries)]
    sums = df.groupby("geoId").aggregate({"cases": sum, "deaths": sum})

    if output[:-4].lower() in ("stdout", "-"):
        fd = sys.stdout
        fd_close = lambda: None
    else:
        fd = open(output, "w")
        fd_close = fd.close

    try:
        print("ID Date        Cases(change) Deaths(chg)", file=fd)
        for country in countries:
            if country == "ALL":
                totals = df.groupby("dateRep").aggregate({"cases": sum, "deaths": sum})
                last = totals.iloc[-1]
                print(
                    "-- {last.name:%Y-%m-%d} {tot[cases]:>6d}({last[cases]:>6d}) {tot[deaths]:>5d}({last[deaths]:>4d})".format(
                        last=last, tot=totals.sum(),
                    ),
                    file=fd,
                )
                continue

            last = df[df["geoId"] == country].nlargest(1, "dateRep").iloc[0]
            print(
                "{country} {last[dateRep]:%Y-%m-%d} {tot[cases]:>6d}({last[cases]:>6d}) {tot[deaths]:>5d}({last[deaths]:>4d})".format(
                    country=country, last=last, tot=sums.loc[country],
                ),
                file=fd,
            )
    finally:
        fd_close()


def run(args):
    """@param args: RunArgs"""
    df = pd.read_csv(args.input, parse_dates=["dateRep"], dayfirst=True, encoding="ISO-8859-1")
    countries = args.countries.upper().split(",") or ["ALL"]
    while "TOP" in countries:
        i = countries.index("TOP")
        countries = countries[:i] + get_top_geoIds(df) + countries[i + 1 :]

    # text-only of latest data
    if args.output.lower().endswith(".txt"):
        run_text(df, args.output, countries)
        return

    if countries == ["ALL"]:
        # world summary
        title = "World"
        cum = df.groupby("dateRep").aggregate({"cases": sum, "deaths": sum})
    elif len(countries) == 1 and countries[0] != "TOP":
        # single country
        title = countries[0]
        cum = (
            df[df["geoId"] == countries[0]]
            .groupby("dateRep")
            .aggregate({"cases": sum, "deaths": sum})
        )
    else:
        # multiple countries
        title = "cases"
        idx = df["geoId"].apply(lambda x: x in countries)
        cum = df[idx]

    # plot data
    import matplotlib.pyplot as plt

    plt.figure()

    if title == "cases":
        key = "cases"
        for country, ls, m in zip(
            countries, ["-", "--", "-.", ":"] * 99, ".,ov^<>1234sp*hH+xDd|_"
        ):
            i = cum[cum["geoId"] == country]
            plt.semilogy(i["dateRep"], i[key], label=country, ls=ls, marker=m)
            plt.title(title)
    else:
        for key in ("cases", "deaths"):
            plt.semilogy(cum[key], label=key)

    plt.title(title)
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
