# 🏥 covid-19-box

GitHub Action for injecting COVID-19 status into a gist.

```
ID Date        Cases(change) Deaths(chg)
CN 2020-03-25  81847(    99)  3287(   4)
IT 2020-03-25  69176(  5249)  6820( 743)
US 2020-03-25  55231(  8789)   801( 211)
ES 2020-03-25  39673(  6584)  2696( 514)
DE 2020-03-25  31554(  2342)   149(  23)
IR 2020-03-25  24811(  1762)  1934( 122)
FR 2020-03-25  22302(  2446)  1100( 240)
KR 2020-03-25   9137(   100)   126(   6)
CH 2020-03-25   8789(   774)    86(  20)
UK 2020-03-25   8077(  1427)   422(  87)
-- 2020-03-25 416916( 38876) 18565(2200)
```

---

## ✨ Inspiration

[Data from ECDC](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)

## 🎒 Prep Work
1. Create a new public GitHub Gist (https://gist.github.com/)
1. Create a token with the `gist` scope and copy it. (https://github.com/settings/tokens/new)

## 🖥 Project Setup
1. Fork this repo
1. Go to your fork's `Settings` > `Secrets` > `Add a new secret` for each environment secret (below)

## 🤫 Environment Secrets
- **gist_id:** The ID portion from your gist url `https://gist.github.com/<github username>/`**`6d5f84419863089a167387da62dd7081`**.
- **gh_token:** The GitHub token generated above.
- **countries:** Comma-separated list of country IDs. Also can use `all` (world summary), or `top` (10 highest). Example: **top,all,JP**.

## 💸 Donations

Feel free to use the GitHub Sponsor button to donate towards my work if you're feeling generous <3

## Local Install

Requires Python and either pip or conda. Supports interactive plotting (rather than just plain-text gists).

### pip

```
pip install -r requirements.txt
```

### conda

```
conda env create -f environment.yml
conda activate covid-19
```

### Run

To (re)generate all graphs and summaries:

```
dvc update COVID-19.csv.dvc
dvc repro -P  # auto-generates `world.png` and `top.png`
```

[World graph](world.png)

[Highest number of cases](top.png)

To manually run,

```
dvc update COVID-19.csv.dvc  # at least once
python covid19.py --help
```
