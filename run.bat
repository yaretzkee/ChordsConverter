@echo off
rem color 1b
cls
rem SET VENV_PATH=%USERPROFILE%\python_venv\songs_converter\Scripts\
rem SET SCRIPT_ABSOLUTE_PATH=%dropbox%\99.TEMP_non_public\PROGRAMMING\python\projects\ChordsConverter
rem CALL %VENV_PATH%\activate.bat
start pythonw -B songs_converter.pyw
exit /b
