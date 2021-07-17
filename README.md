# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date            Cases( change)    Deaths(chnge)
US 2021-07-16 34,053,079( 77,438)   608,815(  417)
BR 2021-07-16 19,308,109( 45,591)   540,398(1,456)
IN 2021-07-16 31,026,829(      0)   412,531(    0)
ME 2021-07-16  2,642,068( 12,420)   236,015(  275)
PE 2021-07-16  2,090,175(  2,032)   194,935(   90)
RU 2021-07-16  5,835,523( 25,188)   144,446(  789)
GB 2021-07-16  5,353,245( 51,949)   128,913(   49)
IT 2021-07-16  4,281,214(  2,895)   127,851(   11)
CO 2021-07-16  4,601,335( 17,893)   115,333(  500)
FR 2021-07-16  6,255,115( 10,995)   111,641(   22)
-- 2021-07-15 188,898,563(569,330) 4,072,388(8,449)
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
