# Creating formatted outputs

![schedules-format-design-brief](images/schedules-format-design-brief.png)

## Word docx

use pandoc to convert markdown to docx using a reference docx for template styling. this is how we're currently doing it.

## LaTex 

_currently not using this and using docx instead, but could convert in the future...

### from markdown using pandoc and pandoc-latex-template

[pandoc-latex-template](https://github.com/Wandmalfarbe/pandoc-latex-template)

required:
```bash
sudo apt install texlive-latex-extra
sudo apt-get install texlive-fonts-recommended texlive-fonts-extra

sudo apt install make
sudo apt-get install latexmk
sudo apt-get install texlive-xetex
# ^ for jupyter book
```

then make:
```bask
pandoc example.md -o example.pdf --from markdown --template eisvogel --listings
```

### from JupyterBook

see build_pdf.sh in this repo