# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date         Cases/wk(   change)  Deaths(change)
US 2021-01-11 22,423,006(1,782,792) 374,442(22,852)
BR 2021-01-11  8,131,612(  397,866) 203,580( 7,562)
IN 2021-01-11 10,466,595(  126,126) 151,160( 1,511)
MX 2021-01-11  1,541,633(   92,878) 134,368( 7,155)
UK 2021-01-11  3,072,349(  417,570)  81,431( 6,407)
IT 2021-01-11  2,276,491(  121,045)  78,755( 3,423)
FR 2021-01-11  2,783,256(  127,528)  67,750( 2,713)
RU 2021-01-11  3,425,269(  165,131)  62,273( 3,285)
IR 2021-01-11  1,286,406(   42,972)  56,171(   631)
ES 2021-01-11  2,111,782(  152,938)  52,275( 1,197)
-- 2021-01-11 89,802,096(5,270,998) 1,940,529(93,681)
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
