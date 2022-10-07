# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
# write json
import pathlib
import json

di = {
    "string": "adsf",
    "int_slider": 2,
    "int_text": 1,
    "int_range_slider": [
        0,
        3
    ]
}
path = pathlib.Path('test.json')
path.write_text(json.dumps(di, indent=4))
# -

# read json
json.loads(path.read_text())


