# Cisco DNA Center Device List, and Network Health

This script is designed to show simple REST API operation and print Cisco DNAC device list and network health

# Deploy in Cisco Exchange Dev environment

If you run this project using the Cisco Exchange Dev environment

![automation-scripts-exchange-devenv](https://raw.githubusercontent.com/CiscoDevNet/code-exchange-repo-template/master/manual-sample-repo/img/automation-scripts-exchange-devenv.png)

Scripts using [Cisco DNA Center Always-on sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology)

In the Cisco Exchange Dev environment, you can try with the following commands:

Install Python packages

```
pip install -r requirements.txt
```

Run `simple_api_operation_dnac.py`

```
python simple_api_operation_dnac.py

```

Sample output:
```
 Extract related information from JSON:

ID:  6b741b27-f7e7-4470-b6fc-d5168cc59502  Hostname  c3504.abc.inc  Management IP Address  10.10.20.51  Serial Number  FOL25040021
ID:  aa0a5258-3e6f-422f-9c4e-9c196db115ae  Hostname  leaf1.abc.inc  Management IP Address  10.10.20.81  Serial Number  FCW2220G09V
ID:  f0cb8464-1ce7-4afe-9c0d-a4b0cc5ee84c  Hostname  leaf2.abc.inc  Management IP Address  10.10.20.82  Serial Number  FCW2211G0MA
ID:  f16955ae-c349-47e9-8e8f-9b62104ab604  Hostname  spine1.abc.inc  Management IP Address  10.10.20.80  Serial Number  FOC2135Z00T


Health Score 75, Total Count: 4
Category Access, Health Score: 100
Category Distribution, Health Score: 100
Category WLC, Health Score: 0
```

# For deploy on your local machine

```
Terminal command here
```
You will copy this text and paste it into the terminal. 

For Linux:

### Copy - CTRL+INSERT
### Paste - SHIFT+INSERT

Clone the repo

```
git clone https://github.com/oborys/DNAC-simple-script
```

Work with Python:

```
cd DNAC-simple-script
```

### Setup virtualenvironment

**Install the virtualenv package**

The virtualenv package is required to create virtual environments. You can install it with pip:
```
pip install virtualenv
```
**Create the virtual environment**

To create a virtual environment, you must specify a path. For example to create one in the local directory called `py3-venv`, type the following:
```
python3 -m venv py3-venv
```

**"Activate" the environment**

Mac OS / Linux
```
source py3-venv/bin/activate
```

Windows
```
py3-venv\Scripts\activate
```

**Install packages (list of packages in file `requirements.txt`) into the current python environment**
```
pip install -r requirements.txt 
```

**Run script**

```
python simple_api_operation_http_errors.py
```

**Deactivate the virtual environment**

To decativate the virtual environment and use your original Python environment, simply type `deactivate`.

```
deactivate
```
