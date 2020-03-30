FROM python:3.7-slim
LABEL maintainer.name="Casper da Costa-Luis" \
      maintainer.email="casper.dcl@physics.org" \
      repository.url="https://github.com/casperdcl/covid-19-box"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY src/requirements-gist.txt .
RUN pip install --no-cache-dir -r requirements-gist.txt && rm requirements-gist.txt
RUN apt-get update -qq && apt-get install -yqq \
 git \
 && apt-get purge && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /wdir
COPY *.dvc *.py ./
COPY src src
COPY .dvc .dvc
RUN chmod +x src/script.sh
ENTRYPOINT ["/wdir/src/script.sh"]
