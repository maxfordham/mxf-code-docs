# mfcode_docs

building mfcode high-level developer documentation into a jupyter-book website.

** References:
- https://jupyterbook.org/intro.html
- https://github.com/executablebooks/quantecon-mini-example

## create conda environment

```bash {install_env.bat}
mamba env create -f environment.yml
conda activate mfcode_docs
```
## Create toc

```bash
jupyter-book toc from-project book\docs > book\_toc.yml
```

## Building a Jupyter Book

```bash {build_book.bat}
call conda activate mfcode_docs
call jb build book/
call start book/_build/html/index.html
cmd /k
```

## Publish book to github pages

```bash {publish_book.bat}
call build_book.bat
call ghp-import -n -p -f book/_build/html
cmd /k
```

## Go to mfcode_docs website

[https://gunstonej.github.io/mfcode_docs/](https://gunstonej.github.io/mfcode_docs)

