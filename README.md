# Overview for memorable-password
This command line script can generate up to 100 memorable passwords with lengths from 8 to 32. It uses the Unix / Linux web2 file, often located at /usr/share/dict. It generates passwords with symbols and numbers along with two memorable words to use as the password.

Example of output is below

```
witting119+touts
wealthy887%Goren
stalks2724%boars
recur1894=riddle
shrews65=sodding
asylum1567&serve
touch193&fortune
Steuben2~equaled
Brooks49?powdery
Tudor97277~thymi
homer85631$musty
unused72^enzymes
revered438&brand
densely6^saddles
orphan96.Barbary
forges567*italic
pikes1345?pebbly
coffers3#profess
toehold2+contain
```

There are some common names which results in some passwords with uppercase and lowercase. One can simply make a word uppercase if needed.

## License
This code is licensed under MIT License. See LICENSE

## Dependencies
Python3

## Run script
At a minimum copy the dist folder, rename it to what you want, change directory into this folder and run the commands below. A Makefile is available for those that want to tinker with the code and regenerate the dist folder contents.

For Non-Windows
```
python3 memorable-password.py
```

For Windows
```
python memorable-password.py
```

## Make steps
There are 3 make steps
```
make clean
make test
make dist
```

### GitHub
The project is located at https://github.com/devdog66/memorable-password

