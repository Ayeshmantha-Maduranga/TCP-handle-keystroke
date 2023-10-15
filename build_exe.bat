@echo off
rem Specify the name of the executable without the ".exe" extension
set EXECUTABLE_NAME=TCP_Key_Controller

rem Build the executable using PyInstaller with the specified name
venv\Scripts\pyinstaller --onefile --name %EXECUTABLE_NAME% app.py

rem Specify the path to the icon file (if any)
set ICON_FILE=TCP_Hkey.ico

rem Check if the icon file is provided and add it to the spec file
if exist %ICON_FILE% (
    rem Generate a spec file
    venv\Scripts\pyinstaller --name %EXECUTABLE_NAME% --add-data "%ICON_FILE%;." --windowed --specpath=. --distpath=dist app.py

    rem Build the executable based on the modified spec file
    venv\Scripts\pyinstaller app.spec
) else (
    rem Build the executable without modifying the spec file
    venv\Scripts\pyinstaller app.py
)

rem Pause the script so you can see any error messages
pause
