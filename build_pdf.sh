conda init bash
conda activate mfcode_docs
python book/docs/_index.py
jb build book/ --builder pdflatex
