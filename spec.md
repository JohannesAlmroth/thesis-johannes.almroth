# Implementation of NB-IoT Communication with Scales
### Specification - Draft

**Student:** Johannes Almroth, **Advisor:** Per Smedsrud, **Reviewer:** Per Gunningberg

## 1. Background
NB-IoT (Narrowband IoT) is a relatively new LPWAN (Low Power Wide Area) radio technology developed by the 3GPP organization. The primary focus areas of NB-IoT are indoor coverage, low cost, long battery life as well as high connection density. Vetek, a Swedish scale supplier, wants to examine the potential applications this technology could bring to their business model. As a first step in this endeavour the cost and complexity to enable online data communications with a loading cell unit needs to be investigated, which would be the aim of this thesis. 
**[Discuss hardware?]**


## 2. Problem Description and Approach
Since NB-IoT is new and emerging technology within the IoT field, limited documentation and knowledge is readily available. Some previous work and examples are available from the Computer Communications Group at Uppsala university, 


The necessary components for this projects includes a SIM-card connected to a NB-IoT network, a NB-IoT relay component(?), as well as a micro-controller in the form of an arduino. Uppsala university will provide the NB-IoT SIM-card as well as the relay component. Vetek will provide the arduino as well as the loading cell (including the necessary parts for the communication between the devices). 

Här beskrivs mer detaljerat innehållet i examensarbetet: vad som skall göras och vilka moment ingår. Speciellt skall det beskriva vad som är den intressanta delen i problemet, samt hur detta skall analyseras och lösas. Här bör det alltså framgå att arbetet uppfyller kraven som universitetet har på ett exjobb på denna nivå.

### Limitation
The project will primarily aim at enabling a basic communication channel between a loading cell and the internet(?) using the NB-IoT technology. Any business aspects such as automation, presentation and efficiency will only be considered and worked upon if time allows for it. 

### 4. Relevant courses
* Computer Networks and Distributed Systems
* Imperative and Object-Oriented Programming Methodology (?)

### 5. Time plan

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
