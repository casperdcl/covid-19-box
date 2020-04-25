# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date        Cases(change) Deaths(chg)
US 2020-04-25 890524( 21352) 51017(1054)
IT 2020-04-25 192994(  3021) 25969( 420)
ES 2020-04-25 219764(  6740) 22524( 367)
FR 2020-04-25 122577(  1773) 22245( 389)
UK 2020-04-25 143464(  5386) 19506( 768)
BE 2020-04-25  44293(  1496)  6679( 189)
IR 2020-04-25  88194(  1168)  5574(  93)
DE 2020-04-25 152438(  2055)  5500( 179)
CN 2020-04-25  83899(    15)  4636(   0)
NL 2020-04-25  36535(   806)  4289( 112)
-- 2020-04-25 2744744( 76607) 195707(5471)
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
