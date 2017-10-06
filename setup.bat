REM    Requirements: pyinstaller
REM    $ pip install pyinstaller
pyinstaller --onefile --name VendingMachine -i a.ico app.py
REM    --distpath DIR	Where to put the bundled app (default: ./dist)