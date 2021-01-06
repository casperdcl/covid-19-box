# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date         Cases/wk(   change)  Deaths(change)
US 2021-01-04 20,640,214(1,488,563) 351,590(18,264)
BR 2021-01-04  7,733,746(  249,461) 196,018( 4,879)
IN 2021-01-04 10,340,469(  132,598) 149,649( 1,748)
MX 2021-01-04  1,448,755(   59,325) 127,213( 4,358)
IT 2021-01-04  2,155,446(  107,750)  75,332( 3,407)
UK 2021-01-04  2,654,779(  325,049)  75,024( 3,915)
FR 2021-01-04  2,655,728(   93,082)  65,037( 1,928)
RU 2021-01-04  3,260,138(  182,103)  58,988( 3,723)
IR 2021-01-04  1,243,434(   42,969)  55,540(   847)
ES 2021-01-04  1,958,844(   79,431)  51,078(   956)
-- 2021-01-04 84,532,824(4,205,212) 1,845,597(74,321)
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
