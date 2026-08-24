from benchmark import generate
from falcon import FalconMonitor, FalconConfig, latency_metrics

def run(rho):
    xs,event,hazard = generate(42)
    m = FalconMonitor(
        baseline_mean=0.0,
        baseline_std=0.5,
        config=FalconConfig(alpha=0.02,accumulator_rho=rho,alarm_score=2.2)
    )
    alarm = None
    for t,x in enumerate(xs):
        out = m.update(x)
        if t >= event and out["alarm"] and alarm is None:
            alarm = t
    return latency_metrics(event,hazard,alarm,2)

if __name__ == "__main__":
    print("fast accumulator:", run(0.2))
    print("slow accumulator:", run(0.9))
