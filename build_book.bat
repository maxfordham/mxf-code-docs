pushd %~dp0
call conda activate mfcode_docs
call jb build book/
call bat-copy_fol_contents.bat book/_data book/_build/html/_data
call start book/_build/html/index.html
::cmd /k