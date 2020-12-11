# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date         Cases(change) Deaths(chng)
US 2020-12-11 15616381(224680) 292179(2748)
BR 2020-12-11 6781799( 53347) 179765( 770)
IN 2020-12-11 9796769( 29398) 142186( 414)
MX 2020-12-11 1217126( 11897) 112326( 671)
UK 2020-12-11 1787783( 20964)  63082( 516)
IT 2020-12-11 1787147( 16998)  62626( 887)
FR 2020-12-11 2337966( 13750)  56940( 292)
IR 2020-12-11 1083023( 10403)  51496( 284)
ES 2020-12-10 1720056(  7955)  47344( 325)
RU 2020-12-11 2569126( 27927)  45280( 562)
-- 2020-12-11 69282662(644911) 1582381(11754)
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
