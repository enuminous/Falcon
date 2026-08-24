from falcon import FalconMonitor, FalconConfig

monitor = FalconMonitor(
    baseline_mean=0.0,
    baseline_std=1.0,
    config=FalconConfig(
        alpha=0.02,
        accumulator_rho=0.25,
        alarm_score=1.8
    )
)

stream = [0.1,-0.2,0.0,0.2,0.1,0.3,0.8,1.2,2.0,2.5]

for x in stream:
    print(monitor.update(x))
