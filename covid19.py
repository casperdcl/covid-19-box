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
  --log LEVEL  : (FAT|CRITIC)AL|ERROR|WARN(ING)|[default: INFO]|DEBUG|NOTSET

%s
"""
import logging
import sys

from argopt import argopt
import pandas as pd

__all__ = ["main", "run"]
__version__ = "0.0.0"
__author__ = "Casper da Costa-Luis <casper.dcl@physics.org>"

log = logging.getLogger(__name__)


def get_top_geoIds(df, key="Cases", top=10):
    ids = df.groupby('GeoId').aggregate({"Cases": sum, "Deaths": sum}).sort_values(key)[-top:][::-1]
    return list(ids.index)

def run(args):
    """@param args: RunArgs"""
    df = pd.read_csv("COVID-19.csv", parse_dates=["DateRep"], dayfirst=True)

    # text-only of latest data
    if args.output.lower().endswith('.txt'):
        countries = (args.countries or "all").split(',')

        if args.output[:-4].lower() in ("stdout", "-"):
            fd = sys.stdout
            fd_close = lambda: None
        else:
            fd = open(args.output, "w")
            fd_close = fd.close

        print("ID Date        Cases(change) Deaths(chg)", file=fd)
        if "top" in countries:
            i = countries.index("top")
            countries = countries[:i] + get_top_geoIds(df) + countries[i + 1:]
        if "all" not in countries:
            df = df[df['GeoId'].apply(lambda x: x in countries)]

        sums = df.groupby("GeoId").aggregate({"Cases": sum, "Deaths": sum})

        for country in countries:
            if country == "all":
                totals = df.groupby("DateRep").aggregate({"Cases": sum, "Deaths": sum})
                last = totals.iloc[-1]
                print(
                    "-- {last.name:%Y-%m-%d} {tot[Cases]:>6d}({last[Cases]:>6d}) {tot[Deaths]:>5d}({last[Deaths]:>4d})".format(
                        last=last,
                        tot=totals.sum(),
                    ),
                    file=fd
                )
                continue

            last = df[df["GeoId"] == country].iloc[0]
            print(
                "{country} {last[DateRep]:%Y-%m-%d} {tot[Cases]:>6d}({last[Cases]:>6d}) {tot[Deaths]:>5d}({last[Deaths]:>4d})".format(
                    country=country,
                    last=last,
                    tot=sums.loc[country],
                ),
                file=fd
            )

        fd_close()
        return

    if not args.countries or args.countries.lower() == "all":
        title = "World"
        cum = df.groupby("DateRep").aggregate({"Cases": sum, "Deaths": sum})
    elif ',' not in args.countries and args.countries.lower() != "top":
        title = args.countries
        cum = df[df["GeoId"] == args.countries].groupby("DateRep").aggregate({"Cases": sum, "Deaths": sum})
    else:
        title = "Cases"
        if args.countries.lower() == "top":
            countries = get_top_geoIds(df)
        elif ',' in args.countries:
            countries = args.countries.upper().split(',')

        idx = df['GeoId'].apply(lambda x: x in countries)
        cum = df[idx]

    # plot data
    import matplotlib.pyplot as plt
    plt.figure()

    if title == "Cases":
        key = "Cases"
        for country, ls, m in zip(countries, ['-', '--', '-.', ':'] * 99, ".,ov^<>1234sp*hH+xDd|_"):
            i = cum[cum['GeoId'] == country]
            plt.semilogy(i["DateRep"], i[key], label=country, ls=ls, marker=m)
            plt.title(title)
    else:
        for key in ("Cases", "Deaths"):
            plt.semilogy(cum[key], label=key)

    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(args.output)


def main(argv=None):
    """argv  : list, optional (default: sys.argv[1:])"""
    args = argopt(__doc__ % (__version__, __author__),
                  version=__version__).parse_args(args=argv)
    logging.basicConfig(level=getattr(logging, args.log, logging.INFO))
    log.debug(args)
    return run(args) or 0


if __name__ == "__main__":
    main()
