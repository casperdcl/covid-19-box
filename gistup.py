#!/usr/bin/env python
"""
Updates gist from stdin. Requires:
- $INPUT_GIST_ID
- $INPUT_GH_TOKEN
"""
import json
import logging
import os
import requests
import sys

url = "https://api.github.com/gists/" + os.environ["INPUT_GIST_ID"]
headers = {"Authorization": "token " + os.environ["INPUT_GH_TOKEN"]}
log = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    req = requests.get(url, headers=headers)
    res = req.json()
    files = sorted(res["files"].keys())
    log.debug(files)

    # update first file
    payload = {
        "description": "COVID-19 Status",
        "files": {files[0]: {"content": sys.stdin.read(), "filename": "COVID-19"}},
    }
    # delete other files
    for f in files[1:]:
        payload["files"][f] = None
    log.debug(payload)
    req = requests.patch(url, headers=headers, json=payload)
    req.raise_for_status()
