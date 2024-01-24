@echo off

rem Set the path to your virtual environment activate script
set VENV_PATH=.\venv\Scripts\activate

rem Activate the virtual environment
call %VENV_PATH%

rem Run the Python script
python very_basic_FlaskUI.py

rem Deactivate the virtual environment
deactivate
