@echo off
color 1b
cls
SET VENV_PATH=%USERPROFILE%\python_venv\songs_converter\Scripts\
SET SCRIPT_ABSOLUTE_PATH=d:\00_CLOUD\Dropbox\99.TEMP_non_public\PROGRAMMING\python\projects\ChordsConverter
CALL %VENV_PATH%\activate.bat
start python songs_converter.pyw
exit /b
