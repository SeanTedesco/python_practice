# ASYNC Tutorial

## For MACS
1.0 Create a virtual environment and activate it.

```
$ python -m venv async-venv
$ . async-venv/bin/activate
```

1.1 Ensure the environment was activated succesfully.

```
$ which python
```
Should read:
```
    ... async/async-venv/bin/python
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
$ python install --upgrade pip setuptools
```

1.4 Install all the required dependencies with pip. 

```
$ pip install -r requirements.txt
```

1.5 Run the src/program.py main file. *Note you have to be in the src directory to copy and paste this command directly.* 
```
python program.py
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
    ... file_searcher/searcher-venv/bin/python
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
python program.py
```

# Notes

## Definitions 
Asynchronous: the occurrence of events independent of the main program flow and ways to deal with such events. These may be "outside" events such as the arrival of signals, or actions instigated by a program that take place concurrently with program execution, without the program blocking to wait for results.

- can be used to do things faster 
- can be used to do more things at once

Thread: is a separate flow of execution. Threads may run on different processors, but they will only be running one at a time. Threads live inside processes and share the same memory space. 

Process: is an instance of program which spawn threads (sub-processes) to handle subtasks. Processes are created by the OS, and two processes can execute code simultaneously in the same python program. Sharing information between processes is slower than sharing between threads as processes do not share memory space. In python they share information by pickling data structures like arrays which requires IO time.

GIL: Python Global Interpreter Lock: allows only one thread to hold the control of the Python interpreter. This means that attempting to use multiple threads, the interpreter can still only execute one instruction at a time. 

## Typical Mltithreading and Multiprocessing Snippet 

-- sean, insert the photo on your desktop here. 

## Asyncio
- runs on an event loop.
- work gets queued into an event loop and we wait until all that work is finished. 
- troublesome to do work outside of that loop
- 'async def' methods always execute in the loop (not thread or process based)

Asyncio is useful for programs with long waiting periods, such as http requests and scrapers. 

## Threads

## Multiprocessing

Multiprocessing is useful for programs with heavy computation as it spreads out the work done in a list across different processes. 

## Unsync

This is a wrapper that ties together the functionality of asyncio, threads, and multiprocessing. It is a clean way to group together all three of these async techniques, but setting only a few parameters including: "cpu_bound=True" for multiprocessing, and including the "async def" for asyncio awaits. 

-- sean, insert the photo on your desktop here. 

## Cython
Cython is an optimising static compiler for both the Python programming language and the extended Cython programming language (based on Pyrex). It makes writing C extensions for Python as easy as Python itself.

To build a cython module from a setup file:
```
$ python setup.py build_ext --inplace
```