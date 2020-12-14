# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date         Cases(change) Deaths(chng)
US 2020-12-14 16256754(189723) 299177(1340)
BR 2020-12-14 6901952( 21825) 181402( 279)
IN 2020-12-14 9884100( 27071) 143355( 336)
MX 2020-12-14 1250044(  8608) 113953( 249)
IT 2020-12-14 1843712( 17937)  64520( 484)
UK 2020-12-14 1849403( 18447)  64170( 144)
FR 2020-12-14 2376852( 11533)  57911( 150)
IR 2020-12-14 1108269(  7451)  52196( 247)
ES 2020-12-13 1730575(     0)  47624(   0)
RU 2020-12-14 2653928( 28080)  46941( 488)
-- 2020-12-14 71503614(540659) 1612833(7085)
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
