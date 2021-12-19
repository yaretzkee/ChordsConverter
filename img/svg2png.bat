@ECHO OFF
SET INKSCAPE="C:\PORTABLE\inkscape\inkscape.exe"

FOR %%f IN (*.svg) DO (
    %INKSCAPE% -z "%%f" -e %%~nf.png
)

pause
 