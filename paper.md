# FALCON: Fast Adaptive Latency and Control Observation Network

## Abstract

FALCON is an experimental framework for latency-sensitive detection and control. It evaluates detection delay, intervention delay, reaction margin, false alarms, and adaptive-threshold behavior under real-time constraints.

## 1. Motivation

Some monitors detect failure correctly but too late.

In control systems, the decisive variable may be:

`time remaining before hazard`

rather than eventual classification accuracy.

## 2. Model

Normalized residual:

`z_t = |y_t-mu_t|/(sigma_t+eps)`

Fast recursive score:

`S_t=rho*S_{t-1}+(1-rho)*z_t`

Detection latency:

`L_detect=T_alarm-T_event`

Intervention latency:

`L_control=T_action-T_alarm`

Reaction margin:

`M=T_hazard-T_action`

## 3. Metrics

- detection latency
- intervention latency
- total response latency
- reaction margin
- false-alarm rate
- missed-event rate
- control outcome

## 4. Baselines

- CUSUM
- EWMA
- SPRT
- Bayesian online change-point detection
- Kalman residual thresholding
- static z-score thresholding

## 5. Ablations

- slow accumulator
- static threshold
- no adaptive baseline
- no freeze-on-alarm
- detector-only without control latency
- no reaction-margin analysis

## 6. Falsification

If standard sequential detectors achieve equal or better latency at matched false-alarm rate and compute, FALCON's added structure is not justified.

## 7. Claim boundary

FALCON is a research timing framework. Synthetic lead-time results do not establish deployment-grade real-time safety.
