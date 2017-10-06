#  Requirements: pyinstaller
#    $ pip install pyinstaller
#    $ pyinstaller --onefile --name VendingMachine -i a.ico app.py
pyinstaller --onefile --name VendingMachine -i a.ico app.py
#    --distpath DIR	Where to put the bundled app (default: ./dist)