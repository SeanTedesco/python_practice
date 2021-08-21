# Real Estate Data Miner App

## Learning Objectives
This is a csv, lamda function, and list comprehension learning opportunity. In general these core concepts operate as follows. 

lambda functions: (lambda) (input variables): (statement)
```
data.sort(key=lambda x: x % 2 == 1)
```

list comprehension: (projection / items) (the set to process) (possible condition)
```
two_beds = [home for home in data if home.beds == 2]
```

csv reader: use with a csc file and able to go row by row extracting the data in each of the columns by used of a dictionary. 
```
with open(filename, 'r', encoding='utf-8', errors='ignore') as fin:
        reader = csv.DictReader(fin)
```

## Setup for MACS
1.0 Create a virtual environment and activate it.

```
$ python -m venv miner-venv
$ . miner-venv/bin/activate
```

1.1 Ensure the environment was activated succesfully.

```
$ which python
```
Should read:
```
    ... real_estate_miner_app/miner-venv/bin/python
```

1.2  And check pip that it is relatively empty. 

```
$ pip list
    Package     Version
    ----------  -------
    pip         20.2.3
    setuptools  49.2.1
```

1.3 Update pip and setup tools

```
$ pip install --upgrade pip setuptools
```

1.4 Install all the required dependencies with pip. 

```
$ pip install -r requirements.txt
```

1.5 Run the src/program.py main file. *Note you have to be in the src directory to copy and paste this command directly.* 
```
python program.py
```

## Setup for Windows
1.0 Create a virtual environment and activate it. 

```
$ python -m venv miner-venv
$ . miner-venv\Scripts\activate
```

1.1 Ensure the environment was activated succesfully.

```
$ where python
```

Should read:
```
    ... miner_app miner-venv/bin/python
```

1.2  And check pip that it is relatively empty. 

```
$ pip list
    Package     Version
    ----------  -------
    pip         20.2.3
    setuptools  49.2.1
```

1.3 Update pip and setup tools

```
$ pip install --upgrade pip setuptools
```

1.4 Install all the required dependencies with pip. 

```
$ pip install -r requirements.txt
```

1.5 Run the src/program.py main file. *Note you have to be in the src directory to copy and paste this command directly.* 
```
python program.py
```



