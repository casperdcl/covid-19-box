# COVID-19 graphs

## Install

Requires Python and either pip or conda.

### pip

```
pip install -r requirements.txt
```

### conda

```
conda env create -f environment.yml
conda activate covid-19
```

## Run

```
dvc update COVID-19.csv.dvc
dvc repro -P
```

[World graph](world.png)

[Highest number of cases](top.png)
