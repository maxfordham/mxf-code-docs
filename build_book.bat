pushd %~dp0
call conda activate mfcode_docs
pushd book\docs
call python _index.py
pushd %~dp0
call jb build book/
call bat-copy_fol_contents.bat book/_data book/_build/html/_data
call start book/_build/html/index.html
cmd /k