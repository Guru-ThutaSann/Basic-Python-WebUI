@echo off
rem Create and activate virtual environment
python -m venv venv
call venv\Scripts\activate

rem Upgrade pip
python.exe -m pip install --upgrade pip

rem Install dependencies from requirements.txt
pip install -r requirements.txt

rem Display success message
echo Setup completed successfully.

rem Pause and wait for a key press
pause


