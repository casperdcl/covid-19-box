# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date            Cases( change)    Deaths(chnge)
US 2023-01-10 101,345,041( 59,695) 1,098,123(  864)
BR 2023-01-10 36,447,486( 75,218)   695,068(  206)
IN 2023-01-10 44,683,548(    171)   523,349(    0)
RU 2023-01-10 21,524,480(  3,010)   386,237(   46)
ME 2023-01-10  7,285,650(    653)   324,313(    9)
PE 2023-01-10  4,474,167(  1,318)   219,241(    1)
GB 2023-01-10 23,373,919(      0)   213,503(    0)
IT 2023-01-10 25,279,830(      0)   185,448(    0)
FR 2023-01-10 39,914,696( 11,773)   163,561(  115)
DE 2023-01-10 37,562,191( 22,119)   163,253(  269)
-- 2023-01-09 663,109,352(361,254) 6,671,404(2,061)
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
