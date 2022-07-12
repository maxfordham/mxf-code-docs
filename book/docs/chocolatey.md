---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# [Chocolatey](https://chocolatey.org/)

- some opensource software for windows is easily and simply installable using chocolatey. 
- installers need to be run with Admin credentials

## Suggested installers

```{code-cell}
:tags: [remove-input]
import pathlib
from IPython.display import display

def display_choco(path):
	display(Markdown(f'`{str(path)}`')
	display(Markdown(f'`{path.read_text()}`')
	display(Markdown('---')
	
paths = pathlib.Path('choco').glob('*.bat')
display(Markdown('---')
[display_choco(path) for path in paths]
```
