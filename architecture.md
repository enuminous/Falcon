# FALCON Architecture

## Pipeline

1. Fast Observation Ingestor
2. Baseline Estimator
3. Residual Normalizer
4. Short-Horizon Accumulator
5. Adaptive Threshold Controller
6. Alarm Gate
7. Intervention Trigger
8. Latency Recorder
9. Stability/False-Alarm Evaluator
10. Audit Reporter

## Inputs

- real-time observations
- nominal calibration data
- event/hazard labels for benchmark use
- threshold configuration
- intervention delay
- control outcome

## Outputs

```json
{
  "alarm": true,
  "score": 2.31,
  "detection_latency": 5,
  "intervention_latency": 2,
  "reaction_margin": 11,
  "false_alarm_rate": 0.01
}
```

## Design principle

FALCON never reports speed without false-alarm context.

A detector that fires instantly on everything is not fast; it is unusable.

## Integration

MANTIS can identify slower nonlinear precursor structure.

WOLF can aggregate distributed weak signals into FALCON's fast path.

BEAVER can evaluate candidate interventions.

BISON can test whether fast control still behaves safely under overload.
