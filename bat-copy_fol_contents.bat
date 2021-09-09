REM refs:
REM ------------------------------------------------------------------------------------ 
REM if commands
REM http://steve-jansen.github.io/guides/windows-batch-scripting/part-5-if-then-conditionals.html
REM copying files
REM https://stackoverflow.com/questions/3018289/xcopy-file-rename-suppress-does-xxx-specify-a-file-name-message
REM check if params passed to batch file
REM https://stackoverflow.com/questions/5735146/windows-7-batch-files-how-to-check-if-parameter-has-been-passed-to-batch-file
@ECHO off
if "%~1"=="" (
    SET /p src="Enter directory of folder whose contents you'd like to copy? "
    SET /p dstn="Enter directory folder to paste the contents to? "
) else (
    SET src=%1%
    SET dstn=%2%
)
IF NOT EXIST %dstn% MKDIR %dstn%
REM robocopy %src% %dstn% /MIR REM this deletes what is in the dstn fol
robocopy %src% %dstn% /e 
