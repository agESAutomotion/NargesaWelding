# Parameters used by the system

*   **Sacan Speed (mm/s)**: 2-6000 mm/s
*   **Sacan Width mm**: 0-6 mm, constrained to 

$$
10 \leq \frac{\textrm{scan speed}}{2 * \textrm{scan width}} \leq 1000
$$

If the value is set outside of this range, it will be overwriten with the closest limit
*   **Duty Cycle (%)**: Percentage of time of laser on in a pulse cycle
*   **Frequecy (Hz)**: number of pulse cycles per second
*   **Opening Gas Delay (ms)**: Delay for the opening of the gas valve after triggering the laser gun
*   **Closing Gas Delay (ms)**: Delay for the closing of the gas valve after the laser has turend off. Absolute range is $[0, 3000]$ ms, recomended range is $[200, 500]$ ms
*   **Welding wire delay (ms)**: Wire feeding advance time relative to the light emitting signal. Absolute range is $[0, 3000]$ ms, recomended range is $[200, 500]$ ms
*   **Scan correction**: Scanning correction coeficient given by
$$
\textrm{Scan correction} = \frac{\textrm{Target Linewidth}}{\textrm{Measured Linewidth}}
$$
Absolute range is $[0.01, 4]$
*   **Laser center offset (mm)**: Laser centering offset. Absolute range is $[-3, 3]$ mm (negative implies offset to the left)
*   **Motor drive temperature threshold (ºC)**: Min/max value of the motor's drive temperature for the alarm, depending if the alarm is set to low/high level
*   **Protective mirror temperature threshold (ºC)**: Min/max value of the protective mirror temperature for the alarm, depending if the alarm is set to low/high level
*   **Collimator temperature threshold (ºC)**: Min/max value of the collimator temperature for the alarm, depending if the alarm is set to low/high level
*   **Laser alarm level**: TBD
*   **Chiller alarm level**: TBD
*   **Pressure alarm level**: TBD

## Laser Power Curve
![LaserPowerCurve](.\LaserPowerCurve.png)

*   **Laser Power (W)**: Stable power after the progressive ON time
*   **Peak Power (W)**: must be less that or equal to the `Laser Power` parameter
*   **Laser Starting Power (% Laser Power)**: percentage of `Laser Power` that is applied when the laser is triggered (N1 on graph)
*   **Laser On Progressive time (ms)**: Time to go from the `Laser Starting Power` to the `Laser Power` (T1 on graph)
*   **Laser Off Power (% Laser Power)**: percentage of `Laser Power` that is applied before the laser turns off (N2 on graph)
*   **Laser Off progressive time (ms)**: Time to go from the `Laser Power` to the `Laser Off Power` (T2 on graph)

## Spot Welding Mode Only

*   **Spot welding type**: Type of spot weldig (continuous / fish scale)
*   **Spot Welding duration (ms)**: TBD (the amount of time the laser is active)
*   **Spot Welding interval (ms)**: TBD (amount of time the laser is off before turning back on)
*   **Wire(s) Feed (cm/min)**: speed for soldering wires

---
# Signals / Indicators
*   **Laser Enable**: Enable/disable laser emision
*   **Indication of red light**: Type of laser guide (dot / line)
*   **Welding Mode**: Welding mode operation (continuous / spot)
*   **Secure Lock**: TBD (probably some kind of sequrity measurment)
*   **