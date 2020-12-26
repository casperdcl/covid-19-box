# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date         Cases/wk(   change)  Deaths(change)
US 2020-12-21 17,844,839(1,588,085) 317,670(18,493)
BR 2020-12-21  7,263,619(  361,667) 187,291( 5,889)
IN 2020-12-21 10,055,560(  171,460) 145,810( 2,455)
MX 2020-12-21  1,325,915(   75,871) 118,598( 4,645)
IT 2020-12-21  1,953,185(  109,473)  68,799( 4,279)
UK 2020-12-21  2,040,147(  190,744)  67,401( 3,231)
FR 2020-12-21  2,473,354(   96,502)  60,549( 2,638)
IR 2020-12-21  1,152,072(   43,803)  53,448( 1,252)
ES 2020-12-21  1,819,249(   67,365)  49,260( 1,247)
RU 2020-12-21  2,762,668(  108,740)  49,151( 2,210)
-- 2020-12-21 76,103,424(4,553,839) 1,694,717(80,028)
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
