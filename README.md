# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date            Cases( change)    Deaths(chnge)
US 2021-02-24 28,336,096( 74,502)   505,890(3,230)
BR 2021-02-24 10,324,463( 66,588)   249,957(1,428)
ME 2021-02-24  2,060,908(  8,642)   182,815(1,006)
IN 2021-02-24 11,046,914( 16,738)   156,705(  138)
GB 2021-02-24  4,156,702(  9,942)   121,978(  442)
IT 2021-02-24  2,848,564( 16,402)    96,666(  318)
FR 2021-02-24  3,721,061( 31,527)    85,473(  278)
RU 2021-02-24  4,153,735( 11,609)    83,044(  378)
DE 2021-02-24  2,416,037( 10,774)    69,170(  385)
ES 2021-02-24  3,170,644(  9,212)    68,468(  389)
-- 2021-02-23 111,662,224(387,604) 2,495,873(11,253)
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
