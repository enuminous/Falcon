from dataclasses import dataclass
from typing import Optional
import math

@dataclass
class FalconConfig:
    alpha: float = 0.05
    threshold_k: float = 3.0
    accumulator_rho: float = 0.3
    alarm_score: float = 2.0
    freeze_on_alarm: bool = True

class FalconMonitor:
    def __init__(self, baseline_mean=0.0, baseline_std=1.0, config: Optional[FalconConfig]=None):
        self.mean = float(baseline_mean)
        self.std = max(1e-6, float(baseline_std))
        self.config = config or FalconConfig()
        self.score = 0.0
        self.t = -1
        self.first_alarm = None

    def update(self, y: float):
        self.t += 1
        z = abs((y-self.mean)/(self.std+1e-9))
        self.score = (
            self.config.accumulator_rho*self.score +
            (1-self.config.accumulator_rho)*z
        )

        alarm = self.score >= self.config.alarm_score
        if alarm and self.first_alarm is None:
            self.first_alarm = self.t

        if not (alarm and self.config.freeze_on_alarm):
            old_mean = self.mean
            a = self.config.alpha
            self.mean = (1-a)*self.mean + a*y
            dev = abs(y-old_mean)
            self.std = max(1e-6, (1-a)*self.std + a*dev)

        return {
            "time": self.t,
            "z": z,
            "score": self.score,
            "alarm": alarm,
            "mean": self.mean,
            "std": self.std
        }

def latency_metrics(event_time, hazard_time, alarm_time, control_delay=0):
    if alarm_time is None:
        return {
            "detection_latency": None,
            "intervention_latency": None,
            "reaction_margin": None,
            "missed": True
        }

    control_time = alarm_time + control_delay
    return {
        "detection_latency": alarm_time-event_time,
        "intervention_latency": control_delay,
        "reaction_margin": hazard_time-control_time,
        "missed": control_time >= hazard_time
    }
