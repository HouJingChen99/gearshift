@echo off
setlocal

goto not37

python -V | find "3.7"
if errorlevel 1 goto not37
::python -V
echo pyinstaller only works with versions up to 3.6
pause
goto :eof

:not37
set path=c:\Python36;c:\Python36\scripts;%path%
set path=%path%;"C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64"

pyinstaller -v
@echo.


if exist envPygame\scripts 	echo Using envPygame\scripts 	
if exist envPygame\scripts 	set path=envPygame\Scripts;%path%
if not exist envPygame\scripts	python.exe -m venv envPygame && envPygame/Scripts/activate && python -m pip install -r requirements.txt 

::   --debug=imports 
::  --clean 
::  --paths env\Lib\site-packages 
::  --hidden-import pygame.base 

pyinstaller ^
  --onefile ^
  --distpath . ^
  --paths envPygame\lib\site-packages ^
  "%~dp0\gearshift.py "

if exist version.txt pyi-set_version version.txt Gearshift.exe
pause

