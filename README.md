# Bachelor Thesis - NB-IoT: Communications with a Load Cell
This is a bachelor thesis written by Johannes Almroth for the bachelor program of computer science at Uppsala University during the fall of '19.

## The report


## The code

### Structure
The code consists of three main classes:

#### The reader class
Responsible for:
* Modifying the reading rate
* Detecting sensor failure
* Call on the transmission class to send data

#### The transmission class
Responsible for:
* Sending data to the outside world
* Handling both Wifi and NB-IoT

#### The logger class
Responsible for:
* Logging the actions of both the transmission and reader class
* Displaying logs through visual means
* Comparing action logs with actual data logs



## The hardware
FiPy
Expansion Board 3.1
[Tutorial] (https://docs.pycom.io/gettingstarted/)
**Don't start radio communications without antenna connected, since this may permanently damage the device**
HX711 Load Cell Amplifier
Load Cell **check model**

When running into  
`>>> Can't run conf files, please run only python files`  
make sure you're "standing" in the file you want to run.

When using the FiPY, keep in mind that not all functions of MicroPython are available. @micropython.
When modifying code via pybytes/flash, things can get real funky real quick. Indentation doesn't really work in the online code editor, which really funks up the python interpreter.