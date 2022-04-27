# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date            Cases( change)    Deaths(chnge)
US 2022-04-26 81,100,598( 57,284)   991,940(  331)
BR 2022-04-26 30,272,979( 22,142)   663,108(  144)
IN 2022-04-26 43,065,496(  5,399)   516,281(1,431)
RU 2022-04-26 17,887,152(  6,998)   367,692(  171)
ME 2022-04-26  5,735,115(  1,190)   317,112(   39)
PE 2022-04-26  3,562,300(    623)   213,478(    8)
GB 2022-04-26 21,228,126( 16,778)   170,243(  452)
IT 2022-04-26 16,191,471( 29,984)   162,958(  146)
ID 2022-04-26  6,045,043(    576)   156,163(   30)
FR 2022-04-26 28,893,008( 97,498)   145,883(  170)
-- 2022-04-25 509,524,816(576,090) 6,181,324(2,412)
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
