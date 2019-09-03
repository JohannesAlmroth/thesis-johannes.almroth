# Implementation of NB-IoT Communication with Scales
### Specification - Draft

**Student:** Johannes Almroth, **Advisor:** Per Smedsrud, **Reviewer:** Per Gunningberg

## 1. Background
NB-IoT (Narrowband IoT) is a relatively new LPWAN (Low Power Wide Area) radio technology developed by the 3GPP organization. The primary focus areas of NB-IoT are indoor coverage, low cost, long battery life as well as high connection density. Vetek, a Swedish scale supplier, wants to examine the potential applications this technology could bring to their business model. As a first step in this endeavour the cost and complexity to enable online data communications with a loading cell unit needs to be investigated, which would be the aim of this thesis. 
**[Discuss hardware?]**


## 2. Problem Description and Approach
Since NB-IoT is new and emerging technology within the IoT field, limited documentation and knowledge is readily available. Some previous work and examples are available from the Computer Communications Group at Uppsala university, but simply getting a NB-IoT component integrated with a loading cell should pose enough of a challenge within the framework of a bachelor thesis.

The necessary components for this projects includes a SIM-card connected to a NB-IoT network, a NB-IoT relay component, as well as a micro-controller in the form of an arduino. Uppsala university will provide the NB-IoT SIM-card as well as the relay component. Vetek will provide the arduino as well as the loading cell (including the necessary parts for the communication between the devices). 

Additionally, code to coordinate the data from the loading cell and sending it via the NB-IoT device needs to be written. 

The thesis will outline and describe the working process from start to finish, and serve as a reference point for similar future work regarding NB-IoT. Problems and challenges that inevitably will arise in the implementation will be investigated and analyzed.

### Limitation
The project will primarily aim at enabling a basic communication channel between a loading cell and the internet using the NB-IoT technology. Any business aspects such as automation, presentation and efficiency will only be considered and worked upon if time allows for it. 

### 4. Relevant courses
* Computer Networks and Distributed Systems
* Imperative and Object-Oriented Programming Methodology (?)
* Operating Systems I (?)

### 5. Time plan
The project will start in the beginning of September and proceed until the end of October. The presentation will be held in the start of December. The project will start with researching previous literature, but hands-on work with the hardware will be done as soon as possible.

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
