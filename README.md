# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date         Cases/wk(   change)  Deaths(change)
US 2020-12-28 19,151,651(1,306,812) 333,326(15,656)
BR 2020-12-28  7,484,285(  220,666) 191,139( 3,848)
IN 2020-12-28 10,207,871(  152,311) 147,901( 2,091)
MX 2020-12-28  1,389,430(   63,515) 122,855( 4,257)
IT 2020-12-28  2,047,696(   94,511)  71,925( 3,126)
UK 2020-12-28  2,329,730(  289,583)  71,109( 3,708)
FR 2020-12-28  2,562,646(   89,292)  63,109( 2,560)
RU 2020-12-28  3,078,035(  315,367)  55,265( 6,114)
IR 2020-12-28  1,200,465(   48,393)  54,693( 1,245)
ES 2020-12-28  1,879,413(   60,164)  50,122(   862)
-- 2020-12-28 80,316,555(4,212,527) 1,770,695(75,539)
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
