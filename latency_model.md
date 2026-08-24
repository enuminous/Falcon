# Latency Model

## Event schema

```json
{
  "event_time": 120,
  "hazard_time": 145,
  "alarm_time": 128,
  "control_time": 131
}
```

## Metrics

Detection latency:

`L_detect = alarm_time - event_time`

Control latency:

`L_control = control_time - alarm_time`

Reaction margin:

`M = hazard_time - control_time`

## False-alarm rate

For nominal horizon `T`:

`FAR = false_alarms / T`

Comparisons must match false-alarm rate.

## Missed event

An event is missed if:
- no alarm occurs before the hazard, or
- the control action arrives too late to affect the outcome.

## Adaptive baseline

Baseline updates should be gated so large anomalies do not immediately redefine "normal."

## Fast/slow tradeoff

Lower thresholds reduce detection delay but increase false alarms.

FALCON evaluates the full operating curve rather than a single threshold.
