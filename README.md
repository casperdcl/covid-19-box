# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date         Cases(change) Deaths(chng)
US 2020-11-27 12883845(106091) 263455(1189)
BR 2020-11-27 6204220( 37614) 171460( 691)
IN 2020-11-27 9309787( 43082) 135715( 492)
MX 2020-11-27 1078594(  8107) 104242( 645)
UK 2020-11-27 1574562( 17555)  57031( 498)
IT 2020-11-27 1509875( 29001)  52850( 822)
FR 2020-11-27 2183660( 13563)  50957( 339)
IR 2020-11-27  908346( 13961)  46689( 482)
ES 2020-11-26 1617355( 12289)  44374( 337)
RU 2020-11-27 2215533( 27543)  38558( 496)
-- 2020-11-27 61079040(531411) 1433516(10227)
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
