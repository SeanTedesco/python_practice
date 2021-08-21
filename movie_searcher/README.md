# Movie Searcher App

## For MACS
1.0 Create a virtual environment and activate it.

```
$ python -m venv searcher-venv
$ . searcher-venv/bin/activate
```

1.1 Ensure the environment was activated succesfully.

```
$ which python
```
Should read:
```
    ... movie_searcher/searcher-venv/bin/python
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

1.5 Run the src/interface.py main file. *Note you have to be in the src directory to copy and paste this command directly.* 
```
python3 -m interface.py
```

## For Windows
1.0 Create a virtual environment and activate it. 

```
$ python -m venv searcher-venv
$ . searcher-venv\Scripts\activate
```

1.1 Ensure the environment was activated succesfully.

```
$ where python
```

Should read:
```
    .../searcher_app/searcher-venv/bin/python
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

1.5 Run the src/interface.py main file. *Note you have to be in the src directory to copy and paste this command directly.* 
```
python3 -m interface.py
```

# RESTFul API
the api (used in this example)[https://movieservice.talkpython.fm/] has limied functionality. There is an open movie database found at (the open movie database)[http://www.omdbapi.com/] that has more selction. 


# Take Aways
## Keyword Arguements 

We can pass any arbitrary list of parameters into a function beyond what is identified in the function definition by including **kwargs. 
The parameters that get passed into the keyword arguement will be held in a dictionary called kwargs. (kwargs is actually just a conventional name)
Example: 
```
def method(x, y, z, **kwargs):
    print("kwargs= ", kwargs)

method(3, 7, z=2, format=True, age=7)
> kwargs = {'format': True, 'age': 7}
```

We can also go the other direction provided that the names in the dictionary explicitly match our named tuble. So instead of going from keywords to dictionary, we can create create keywords from a dictionary. 
Example: 
md = dict()
m = MovieResult(**md)
