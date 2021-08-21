# Journal - Python App

In this module I focused on imports, file loads/saves, handling switch cases (kind of), and abstraction layers. 

The seperation of journal.py and program.py was used to split the functionality of the overall program into 
user interation and handling the journal provide a more organized approach to this problem. This seperation made
development easier as I could focus on one task at a time. For example I could handle error from user input in
programs.py to ease the amount of edge cases that much be dealt with handling the journal functions. Going forward,
it would make sense to keep the journal module as a class, increasing the modularity of the code. 

The imports and loading and saving a file were basic steps but it was a good introduction to understanding os 
independicies and structuring a project. Going forward it will be easier to revisit handling image files for
the CROS-Sat implementation. 

## Setup for MACS
1.0 Create a virtual environment and activate it.

```
$ python -m venv journal-venv
$ . journal-venv/bin/activate
```

1.1 Ensure the environment was activated succesfully.

```
$ which python
```
Should read:
```
    .../journal_app/journal-venv/bin/python
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

1.5 Run the program.py main file. *Note you have to be in the journal_app/ directory to copy and paste this command directly.* 
```
python program.py
```

## Setup for Windows
1.0 Create a virtual environment and activate it. 

```
$ python -m venv journal-venv
$ . journal-venv\Scripts\activate
```

1.1 Ensure the environment was activated succesfully.

```
$ where python
```

Should read:
```
    .../journal_app/journal-venv/bin/python
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

1.5 Run the program.py main file. *Note you have to be in the journal_app/ directory to copy and paste this command directly.* 
```
python program.py
```
