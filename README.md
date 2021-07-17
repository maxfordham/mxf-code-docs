# mfcode_docs

building mfcode high-level developer documentation into a jupyter-book website.

## create conda environment

```bash
mamba env create -f environment.yml
conda activate mfcode_docs
```
## Create toc

```bash
jupyter-book toc from-project book\docs > book\_toc.yml
```

## Building a Jupyter Book

```bash
conda activate mfcode_docs
jb build book/
```

