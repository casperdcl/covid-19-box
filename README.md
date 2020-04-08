# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date        Cases(change) Deaths(chg)
IT 2020-04-08 135586(  3039) 17129( 604)
ES 2020-04-08 140510(  5478) 13798( 743)
US 2020-04-08 398809( 30613) 12895(1906)
FR 2020-04-08  78167(  3777) 10328(1417)
UK 2020-04-08  55242(  3634)  6159( 786)
IR 2020-04-08  62589(  2089)  3872( 133)
CN 2020-04-08  82784(    86)  3337(   2)
NL 2020-04-08  19580(   777)  2101( 234)
BE 2020-04-08  22194(  1380)  2035( 403)
DE 2020-04-08 103228(  4003)  1861( 254)
-- 2020-04-08 1391890( 74902) 81478(7412)
```

---

As of now, the automatic [cloud-based pinned gist](#pinned-gist) functionality is text-only;
while [running locally](#local-install) allows graph plotting.

## ✨ Sources

[Data from ECDC](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)

# pinned gist

## 🎒 Prep Work
1. Create a new public GitHub Gist (https://gist.github.com/)
1. Create a token with the `gist` scope and copy it. (https://github.com/settings/tokens/new)

## 🖥 Project Setup
1. Fork this repo
1. Go to your fork's `Settings` > `Secrets` > `Add a new secret` for each environment secret (below)

## 🤫 Environment Secrets
- **gist_id:** The ID portion from your gist url `https://gist.github.com/<github username>/`**`37496a4e4c84aed9711fbe3ec560888a`**.
- **gh_token:** The GitHub token generated above.
- **countries:** Comma-separated list of country IDs. Also can use `all` (world summary), or `top` (10 highest). Example: **top,all,JP**.

## 💸 Donations

Feel free to use the GitHub Sponsor button to donate towards my work if you're feeling generous <3

# Local Install

Requires Python and either pip or conda. Supports interactive plotting (rather than just plain-text gists).

## pip

```
pip install -r requirements.txt
```

## conda

```
conda env create -f environment.yml
conda activate covid-19
```

## Run

To (re)generate all graphs and summaries:

```
dvc update COVID-19.csv.dvc
dvc repro -P  # auto-generates `world.png` and `top.png`
```

![World graph](world.png)

![Highest number of cases](top.png)

To manually run,

```
dvc update COVID-19.csv.dvc  # at least once
python covid19.py --help
```

# Developers

Debug the GitHub action locally using:

```
docker-compose build
docker-compose up
```
