# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date         Cases(change) Deaths(chng)
US 2020-09-13 6486108( 40820) 193701( 685)
BR 2020-09-13 4315687( 33523) 131210( 814)
IN 2020-09-13 4754356( 94372)  78586(1114)
MX 2020-09-13  663973(  5674)  70604( 421)
UK 2020-09-13  365174(  3497)  41623(   9)
IT 2020-09-13  286297(  1501)  35603(   6)
FR 2020-09-13  373911( 10561)  30910(  17)
PE 2020-09-13  722832(  6162)  30593( 123)
ES 2020-09-12  566326(     0)  29747(   0)
IR 2020-09-13  399940(  2139)  23029( 116)
-- 2020-09-13 28802775(286031) 920931(4926)
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
