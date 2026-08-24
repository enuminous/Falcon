# FALCON Theory

## 1. Problem

In some systems, a monitor that is accurate but slow is operationally useless.

Relevant domains include:
- real-time control,
- robotics,
- network defense,
- high-frequency operations,
- industrial protection,
- fast human-in-the-loop intervention.

FALCON evaluates detection speed under explicit false-alarm constraints.

## 2. Observation process

Let measurements be:

`y_t`

with nominal distribution:

`y_t ~ P_0`

and changed distribution after event time `T_e`:

`y_t ~ P_1`.

## 3. Detection latency

If the first alarm occurs at `T_a`:

`L_detect = T_a - T_e`

Lower is better, subject to matched false-alarm rate.

## 4. Intervention latency

If a control action is issued at `T_c`:

`L_control = T_c - T_a`

Total response latency:

`L_total = L_detect + L_control`

## 5. Reaction margin

If harmful transition occurs at `T_h`:

`Margin = T_h - T_c`

Positive margin means the system intervened before the hazard.

## 6. Adaptive threshold

A candidate dynamic threshold:

`theta_t = mu_t + k*sigma_t`

where baseline estimates update only during nominal periods or with bounded adaptation.

Unconstrained threshold adaptation can hide true anomalies.

## 7. Fast score

For normalized residual:

`z_t = |y_t - mu_t| / (sigma_t + eps)`

FALCON may maintain a short accumulator:

`S_t = rho*S_{t-1} + (1-rho)*z_t`

with small `rho` for fast response.

## 8. Control quality

Fast intervention is not useful if the action is unstable.

Candidate control score:

`Q = benefit_of_action - overshoot_penalty - false_intervention_cost`

## 9. EFMW interpretation

The EFMW-inspired element is recursive coupling among:
- observed deviation,
- latency,
- threshold state,
- intervention,
- resulting system state.

## 10. Falsifiable prediction

FALCON should add value where:
- response time matters materially,
- short-lived precursors exist,
- adaptive thresholds help under nonstationarity,
- intervention timing changes outcome.

If standard sequential detection methods match performance at equal false-alarm rate and compute, FALCON adds no justified complexity.
