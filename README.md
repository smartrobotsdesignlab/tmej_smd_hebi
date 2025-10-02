# HEBI Motor Virtual Spring-Mass-Damper Demo

This repository contains code and exercises for the **hands-on session** with HEBI motors.  
You will implement and test a **virtual spring–mass–damper (SMD) system** on a real motor.  

---

## 🚀 Requirements

- Python **3.9+**
- HEBI Python API (`hebi-py`)
- `matplotlib` (for plotting)
- `scipy` (for simulations)
- `numpy` (pinned to **1.26.0** for compatibility)

---

## 🔧 Installation

1. Clone this repository and move into the folder:

   ```bash
   git clone https://github.com/smartrobotsdesignlab/tmej_smd_hebi.git
   cd tmej_smd_hebi
   ```
2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

This will ensure numpy==1.26.0 is used.

4. ⚠️ NumPy Compatibility Note
If you see an error like:
```bash
A module that was compiled using NumPy 1.x cannot be run in NumPy 2.x
```

It means your environment upgraded to NumPy 2.x.
Fix it by forcing NumPy 1.26.0:
```bash
pip install numpy==1.26.0
```
---
## ▶️ Usage

- Open one of the example scripts (e.g. SMDStepSim.py).
- Adjust parameters (k, c, m) 
- Run the script and observe behaviour:
```bash
python SMDStepSim.py
```
---
## ✅ Notes

- The motor initializes with its current position as the zero reference.
- Safety limits (max torque, max displacement) are included to protect hardware.

Always keep one hand near the E-stop or power switch.

🎉 Have fun experimenting with the virtual spring–mass–damper system and comparing theory vs. practice!
