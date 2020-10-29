# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date         Cases(change) Deaths(chng)
US 2020-10-29 8858024( 78371) 227700( 977)
BR 2020-10-29 5468270( 28629) 158456( 510)
IN 2020-10-29 8040203( 49881) 120527( 517)
MX 2020-10-29  906863(  5595)  90309( 495)
UK 2020-10-29  942275( 24700)  45675( 310)
IT 2020-10-29  589766( 24988)  37905( 205)
FR 2020-10-29 1235132( 36437)  35785( 244)
ES 2020-10-28 1136503( 19765)  35466( 168)
PE 2020-10-29  894928(  2431)  34315(  58)
IR 2020-10-29  588648(  6824)  33714( 415)
-- 2020-10-29 44574981(479707) 1175279(6914)
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
