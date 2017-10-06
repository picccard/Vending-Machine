# Vending-Machine
Python app to simulate a vending machine with multiple currencies.

## Check for python install
To check if you have python installed and added the the `PATH` variable, run this command:
````
python --version
````

## Build Instructions
If you have python installed on your machine you can run the program directly from the terminal/command prompt with the following command:

````
python app.py
````


### Windows Notes

* Build with pyinstaller and setup.bat in windows:

````
./pip install pyinstaller
./setup.bat
````
    
### Linux Notes

* Download with git:

````
git clone https://github.com/picccard/Vending-Machine.git
````

* Build with pyinstaller and setup.sh in linux:

````
$ pip install pyinstaller
$ cd Vending-Machine
$ setup.sh
````

### Build with cx_Freeze:
* Requires cx_Freeze:

 ````
$ pip install cx_Freeze
$ python setup.py build
````
