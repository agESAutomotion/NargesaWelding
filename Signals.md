# Signals from the original system

## Signal Interface 1

- Air pressure alarm signal: pressure outside range [low P ; high P]
- Water-cooler alarm signal
- Safety lock
- Welding head light switch 1/2

## Signal Interface 2 

- Temperature measurement 1/2
- Protection Gas Valve +/- : 24V = Open / 0V = Closed
- Wire feed +/-

## Signal Interface 3

- Laser abnormal signal
- The laser enables light
- analog quantity + : 0-10V
- PWM +/- 

# Driver for the LASER (Registers)
 
* Scanning Frequency : 
    * Welding Mode 5 - 150 Hz. Note: When the width is greater than 3mm, it is recommended to control within 150Hz to reduce motor failure rate;
    * Cleaning Mode: 10 - 50 Hz
* Scanning Width : 
    * Welding Mode : 0.0 - 5.0 mm
    * Cleaning Mode : 10 - 90.0 mm
* Swing Range Mode : Table 9
* Drive Type : 
    * 0 = Handheld Welding
    * 1 = Handheld Cleaning
    cannot be switched between each other. Initialization occurs only once at the factory; the driver program will restrict the selection of swing range modes based on this configuration.
* RS485 Address Configuration : Default Address: 0x09, range 1-247
* Alarm Detection: 
    * 0 Disable alarm detection (Reset alarms?)
    * 1 Enable alarm detection
* Restore Factory Settings: Home page, parameters, and processes are restored to factory default values (excluding swing range mode, drive type, RS485).
* Save Parameters and Processes
* Indicator Red Light
    * 0 = Point
    * 1 = Line
* **Scanning Calibration (Coefficient) - (Y-axis)** : 0.01～4.00
* **Motor Zero Point Offset - (Y-axis)** : 
    * Welding Mode: -3.00～3.00mm 
    * Cleaning Mode: -75.00～+75.00mm
* **Driver Temperature Alarm Threshold** : 0.0～100.0. Note: Setting to 0 will not trigger an alarm.
* **Protective Lens Temperature Alarm Threshold**: 0.0～100.0. Note: Setting to 0 will not trigger an alarm. 
* **Collimating Lens Temperature Alarm Threshold**: 0.0～100.0. Note: Setting to 0 will not trigger an alarm. 
