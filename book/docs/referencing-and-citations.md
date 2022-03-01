# Referencing and Citations

Within Engineering we rely heavily of external references for calculation methodologies and reference values. 

These references should be formally structured; the practice of doing this is well established within the academic community and can be leveraged for our use-cases. 

Follow these rules: 
- store external references in a (or multiple) separate .bib file(s)
- use [pybtex](https://pybtex.org/) for handling references where required
- use Harvard referencing style for in-line references
- you can use [citethisforme](https://www.citethisforme.com/) to create citations
- if you're using jupyterbook, follow these guides:
    - use {cite:p}`perez2011python` as the default style
    - https://jupyterbook.org/content/citations.html
    - https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#roles-and-directives