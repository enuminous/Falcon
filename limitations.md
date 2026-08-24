# Limitations and Falsification

FALCON is an experimental latency-sensitive monitoring framework.

## Limitations

- Faster detection usually increases false alarms.
- Ground-truth event time may be ambiguous.
- Adaptive thresholds can normalize away failures.
- Control delays may dominate detector latency.
- Real-time compute budgets may constrain model complexity.
- Synthetic event shapes may not match deployment.

## Falsification criteria

FALCON's central hypothesis is weakened if:

1. CUSUM, EWMA, SPRT, or change-point detectors match latency.
2. Gains disappear at matched false-alarm rate.
3. Adaptive thresholds add no robustness.
4. Faster alarms do not improve control outcomes.
5. Results fail on held-out event shapes.
6. Compute overhead offsets the latency benefit.

## Claim boundary

FALCON evaluates detection and response timing under specified signals, thresholds, and control delays. It does not guarantee real-time safety in unseen systems.
