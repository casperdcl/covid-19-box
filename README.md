# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date        Cases(change) Deaths(chg)
US 2020-04-26 939053( 48529) 53189(2172)
IT 2020-04-26 195351(  2357) 26384( 415)
FR 2020-04-26 124114(  1537) 22614( 369)
ES 2020-04-25 219764(  6740) 22524( 367)
UK 2020-04-26 148377(  4913) 20319( 813)
BE 2020-04-26  45325(  1032)  6917( 238)
IR 2020-04-26  89328(  1134)  5650(  76)
DE 2020-04-26 154175(  1737)  5640( 140)
CN 2020-04-26  83909(    10)  4636(   0)
NL 2020-04-26  37190(   655)  4409( 120)
-- 2020-04-26 2844712( 99968) 201315(5929)
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
dvc update COVID-19.xlsx.dvc
dvc repro -P  # auto-generates `world.png` and `top.png`
```

![World graph](world.png)

![Highest number of cases](top.png)

To manually run,

```
dvc update COVID-19.xlsx.dvc  # at least once
python covid19.py --help
```

# Developers

Debug the GitHub action locally using:

```
docker-compose build
docker-compose up
```
