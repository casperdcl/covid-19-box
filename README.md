# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date        Cases(change) Deaths(chg)
US 2020-05-07 1228603( 24128) 73431(2353)
UK 2020-05-07 201201(  6211) 30076( 649)
IT 2020-05-07 214457(  1444) 29684( 369)
ES 2020-05-06 220325(   996) 25857( 244)
FR 2020-05-07 137150(  4183) 25809( 278)
BR 2020-05-07 125218( 10503)  8536( 615)
BE 2020-05-07  50781(   272)  8339( 323)
DE 2020-05-07 166091(  1194)  7119( 123)
IR 2020-05-07 101650(  1680)  6418(  78)
NL 2020-05-07  41319(   232)  5204(  36)
-- 2020-05-07 3713796( 89007) 263288(6174)
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
