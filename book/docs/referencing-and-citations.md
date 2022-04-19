---
jupyter:
  jupytext:
    cell_metadata_json: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Referencing and Citations

Within Engineering we rely heavily of external references for calculation methodologies and reference values. 

These references should be formally structured; the practice of doing this is well established within the academic community and can be leveraged for our use-cases. 

Follow these rules: 

- store external references in .bib file(s)
- use [pybtex](https://pybtex.org/) for handling references where required
- use Harvard referencing style for in-line references
- you can use [citethisforme](https://www.citethisforme.com/) to create citations
- if you're using jupyterbook, follow these guides:
    - use {cite:p}`perez2011python` as the default style
    - https://jupyterbook.org/content/citations.html
    
## Links

- [jupyterbook-citations](https://jupyterbook.org/content/citations.html)
- [sphinxcontrib-bibtex (jupyterbook uses this)](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#roles-and-directives)
- [pandoc-bibliographies-and-citations](https://github.com/shd101wyy/markdown-preview-enhanced/blob/master/docs/pandoc-bibliographies-and-citations.md)
- [entry-types](https://www.bibtex.com/e/entry-types/)
- [wiki-bibtex](https://en.wikipedia.org/wiki/BibTeX)


## Converting from the IHS csv export

```python
import csv
import re
from pybtex.database import BibliographyData, Entry
type_ = "techreport"  # assume all types are technical reports

with open('data/ihs_export.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    li = [_ for _ in reader]  # take only 1st 10 for demonstration purposes

# handle missing data:
# 1. add institution same as publisher if not given
# 1. add author same as institution if not given
# 2. "Series" = "Title" if series does not exist
# 3. add key, alphanumeric only from "Series"
[_.__setitem__('Institution', _['Publisher']) for _ in li if 'Institution' not in _.keys()]
[_.__setitem__('Author', _['Institution']) for _ in li if 'Author' not in _.keys()]
[_.__setitem__('Series', _['Title'][0:30]+'...') for _ in li if _['Series'] == '']
[_.__setitem__('Key', re.sub(r'\W+', '',  _['Series'])) for _ in li]

di_bibs = {_['Key']: Entry(type_, _) for _ in li}
bib_data = BibliographyData(di_bibs)

bib_data.to_file('data/ihs_export.yaml', bib_format='yaml')
bib_data.to_file('data/ihs_export.bib', bib_format='bibtex')
```

<!-- #region -->
## What does the output look like in JupyterBook

__note__ - pandoc can be used for this also but they follow a slightly different markdown syntax. 


### Config

add this to config.yml

```yaml
bibtex_bibfiles:
  - docs/data/ihs_export.bib
```
<!-- #endregion -->

### Formatting in-line citations



`` {cite:p}`GoodPracticeGuide74` `` == {cite:p}`GoodPracticeGuide74`  
`` {cite:t}`GoodPracticeGuide74` `` == {cite:t}`GoodPracticeGuide74`  
`` {cite:ts}`GoodPracticeGuide74` `` == {cite:ts}`GoodPracticeGuide74`  
`` {cite:ps}`GoodPracticeGuide74` `` == {cite:ps}`GoodPracticeGuide74`  
`` {cite:ps}`GoodPracticeGuide74` `` == {cite:label}`GoodPracticeGuide74`  
`` {cite:ps}`GoodPracticeGuide74` `` == {cite:author_year}`GoodPracticeGuide74`



### bibliography

```{bibliography}
:style: unsrt
```

```python
# s = bib_data.to_string(bib_format='yaml')[0:1085]
# print('for example:')
# print('------------')
# print(s)
```

```python

```
