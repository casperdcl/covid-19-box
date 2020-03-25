#!/usr/bin/env python
"""covid19 v%s

Plots current COVID-19 situation.

Usage:
  covid19 [options]

Options:
  -c COUNTRIES, --countries COUNTRIES  : Comma-separated Geo IDs (e.g. CN,IT)
    or [default: all] or "top"
  -o FIGURE, --output FIGURE  : Output figure path [default: COVID-19.png]
  --log LEVEL  : (FAT|CRITIC)AL|ERROR|WARN(ING)|[default: INFO]|DEBUG|NOTSET

%s
"""
import logging

from argopt import argopt
import matplotlib.pyplot as plt
import pandas as pd

__all__ = ["main", "run"]
__version__ = "0.0.0"
__author__ = "Casper da Costa-Luis <casper.dcl@physics.org>"

log = logging.getLogger(__name__)


def run(args):
    """@param args: RunArgs"""
    df = pd.read_csv("COVID-19.csv", parse_dates=["DateRep"], dayfirst=True)

    if not args.countries or args.countries.lower() == "all":
        title = "World"
        cum = df.groupby("DateRep").aggregate({"Cases": sum, "Deaths": sum})
    elif ',' not in args.countries and args.countries.lower() != "top":
        title = args.countries
        cum = df[df["GeoId"] == args.countries].groupby("DateRep").aggregate({"Cases": sum, "Deaths": sum})
    else:
        title = "Cases"
        if args.countries.lower() == "top":
            ids = df.groupby('GeoId').aggregate({"Cases": sum, "Deaths": sum}).sort_values("Cases")[-10:][::-1]
            countries = ids.index
        elif ',' in args.countries:
            countries = args.countries.upper().split(',')
    
        idx = df['GeoId'].apply(lambda x: x in countries)
        cum = df[idx]

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
