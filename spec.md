# Implementation of NB-IoT Communication with Scales
### Specification - Draft

**Student:** Johannes Almroth, **Advisor:** Per Smedsrud, **Reviewer:** Per Gunningberg

## 1. Background
NB-IoT (Narrowband IoT) is a relatively new LPWAN (Low Power Wide Area) radio technology developed by the 3GPP organization. The primary focus areas of NB-IoT are indoor coverage, low cost, long battery life as well as high connection density. Vetek, a Swedish scale supplier, wants to examine the potential applications this technology could bring to their business model. As a first step in this endeavor the complexity to enable online data communications with a loading cell unit needs to be investigated, which would be the aim of this thesis. The end-goal is to enable communications from the data readings of a load cell to an online platform via the use of NB-IoT.


## 2. Problem Description and Approach
Since NB-IoT is a new and emerging technology within the IoT field, limited documentation and knowledge is readily available. Some previous work and examples are available from the Computer Communications Group at Uppsala university, but simply getting a NB-IoT component integrated with a loading cell should pose enough of a challenge within the framework of a bachelor thesis.

The necessary components for this projects includes a SIM-card connected to a NB-IoT network, a NB-IoT compatible micro-controller, as well as a load cell. Uppsala university will provide the NB-IoT SIM-card, and Vetek will provide the rest of the hardware. The specific models and functions of the needed components are outlined below:

* FiPy: a development board that gives access to all major LPWAN technologies. FiPy is developed by PyCom and equipped with an expansion board to enable integration with other components via GPIO pinouts, as well as an LTE-antenna to enable LTE CAT M1 or NB1. MicroPython is enabled on the board, and as such is programmed via the Python programming language. The available protocols on the FiPy are:
	* WiFi
	* Bluetooth
	* LoRa
	* SigFox
	* Dual LTE-M (LTE CAT M1 / NB1)

* Tedea Huntleigh - Model 1022: a single point load cell ideally suited for low cost weighing platforms. This specific model has the capacity of 30 kg, which should be more than enough to run tests of data transfer from the load cell via the FiPy.

* HX711: a breakout board that amplifies the signal from a load cell so that the data can be read more easily. Several libraries are readily available online, including some MicroPython variants. 

Additionally, code to coordinate the data from the loading cell and sending it via the NB-IoT device needs to be written. This will be done in the Python programming language, specifically Python 3. 

The thesis will outline and describe the working process from start to finish, and serve as a reference point for similar future work regarding NB-IoT. Problems and challenges that inevitably will arise in the implementation will be investigated and analyzed. The workflow and prioritization will be oriented after a agile philosophy, focusing on incrementally implementing various parts of the project. The prioritization of the project currently follows this rough outline.

1. Enable communication from the FiPy via another common protocol, such as WiFi.
2. Enable the reading of data from the load cell via the HX711 to the FiPy.
3. Upload this data to a suitable online platform such as ThingSpeak or PyBytes.
4. Enable communications from the FiPy via NB-IoT via a SIM-card from Telia. 

This last point regarding NB-IoT doesn't necessarily need to be done as the last step, and may be implemented earlier.

### Limitation
The project will primarily aim at enabling a basic communication channel between a loading cell and the internet using the NB-IoT technology. Any business aspects such as automation, presentation and efficiency will only be considered and worked upon if time allows for it. 

### 4. Relevant courses
* Computer Networks and Distributed Systems
* Computer Architecture
* Operating Systems I

### 5. Time plan
The project will start in the beginning of September and proceed until the beginning of November. The presentation will be held in the start of December. The project will start with researching previous literature, but hands-on work on the hardware will be done as soon as possible, and follow the rough time-plan given earlier on.

Below is a rough outline of the time plan:

```
+----------------------------------------------------------------------+
|Week             1    2    3    4    5    6    7    8    9    10      |
+----------------------------------------------------------------------+
|Related work     +---------+                                          |                                    
|                                                                      |
|Implementation   +----------------------------------+                 |
|                                                                      |
|Documentation                          +-----------------+            |
|                                                                      |
|Report           +--------------------------------------------------+ |
|                                                                      |
|Presentation                                             +----------+ |
+----------------------------------------------------------------------+
'''
