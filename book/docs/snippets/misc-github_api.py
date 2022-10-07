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
# retrieving data from Github using `api.github`

# for example requiring tokens, see:
# https://gist.github.com/mxmader/8281851a99d0cfb53a363286246c08d8

from IPython.display import JSON
import requests
import xmltodict
import base64

url = 'https://api.github.com/repos/buildingSMART/IFC4.3.x-output/contents/IFC.xsd'
req = requests.get(url)

if req.status_code == requests.codes.ok:
    req = req.json()  # the response is a JSON
    # req is now a dict with keys: name, encoding, url, size ...
    # and content. But it is encoded with base64.
    content = base64.b64decode(req['content'])
else:
    print('Content was not found.')
    
IFC = xmltodict.parse(content)
print('keys:')
print('-----')
[print(l) for l in list(IFC['xs:schema'].keys())]
print('-----')
JSON(IFC)
# -


