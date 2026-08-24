import random
from falcon import FalconMonitor, FalconConfig, latency_metrics

def generate(seed=42, nominal=80, event_len=40):
    rng = random.Random(seed)
    xs = [rng.gauss(0,0.45) for _ in range(nominal)]
    for i in range(event_len):
        shift = min(2.5, 0.12*i)
        xs.append(rng.gauss(shift,0.45))
    event_time = nominal
    hazard_time = nominal + 30
    return xs,event_time,hazard_time

def run(seed=42):
    xs,event,hazard = generate(seed)
    m = FalconMonitor(
        baseline_mean=0.0,
        baseline_std=0.5,
        config=FalconConfig(alpha=0.02,accumulator_rho=0.25,alarm_score=2.2)
    )

    false = 0
    alarm = None
    for t,x in enumerate(xs):
        out = m.update(x)
        if out["alarm"]:
            if t < event:
                false += 1
            elif alarm is None:
                alarm = t

    metrics = latency_metrics(event,hazard,alarm,control_delay=2)
    metrics["false_alarms"] = false
    metrics["false_alarm_rate_nominal"] = false/max(1,event)
    metrics["alarm_time"] = alarm
    metrics["event_time"] = event
    metrics["hazard_time"] = hazard
    return metrics

if __name__ == "__main__":
    for seed in [11,23,42,46,59]:
        print(seed, run(seed))
