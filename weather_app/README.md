# Weather App

## Learning Objectives and Running Application
This is a big tkinter learning exersice. Tkinter is used to create a GUI to collect weather information from the resources [weather.gov](http://www.weather.gov) and [Open Weather Map](http://api.openweathermap.org). 

To run this application follow the setup steps and then run the `interface.py` program by changing into the weather_app directory and executing the interface script: 

```
cd weather_app/
python src/interface.py
``` 

## Open Weather Map Setup 
1.0 Register for an acount at [Open Weather Map](https://openweathermap.org/) and generate your individul API key. 
2.0 create a file called API_KEY.py and insert the line `OWM_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'` where the x's are your API key. 
2.1 Place this file into the weather_app/src directory. 


## Setup for MACS
1.0 Create a virtual environment and activate it.

```
$ python -m venv weather-venv
$ . weather-venv/bin/activate
```

1.1 Ensure the environment was activated succesfully.

```
$ which python
```
Should read:
```
    .../weather_app/weather-venv/bin/python
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

## Setup for Windows
1.0 Create a virtual environment and activate it. 

```
$ python -m venv weather-venv
$ . weather-venv\Scripts\activate
```

1.1 Ensure the environment was activated succesfully.

```
$ where python
```

Should read:
```
    .../weather_app/weather-venv/bin/python
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
