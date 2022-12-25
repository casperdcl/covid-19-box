# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date            Cases( change)    Deaths(chnge)
US 2022-12-24 100,371,551(  5,609) 1,090,729(    4)
BR 2022-12-24 35,987,899(      0)   692,735(    0)
IN 2022-12-24 44,680,268(    227)   523,320(    2)
RU 2022-12-24 21,450,076(  6,922)   385,411(   53)
ME 2022-12-24  7,222,199( 24,566)   323,987(  179)
PE 2022-12-24  4,442,812(      0)   218,834(    0)
GB 2022-12-24 23,298,872(      0)   212,787(    0)
IT 2022-12-24 25,021,754(      0)   183,967(    0)
FR 2022-12-24 39,612,412(      0)   161,608(    0)
DE 2022-12-24 37,212,010(     14)   160,789(    0)
-- 2022-12-23 654,989,160(651,206) 6,637,284(2,515)
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
