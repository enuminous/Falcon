import unittest
from falcon import FalconMonitor, FalconConfig, latency_metrics

class TestFalcon(unittest.TestCase):
    def test_nominal_low_signal_no_immediate_alarm(self):
        m = FalconMonitor(0,1,FalconConfig(alarm_score=3.0))
        out = m.update(0.1)
        self.assertFalse(out["alarm"])

    def test_large_shift_raises_score(self):
        m = FalconMonitor(0,1,FalconConfig(accumulator_rho=0.0,alarm_score=2.0))
        out = m.update(3.0)
        self.assertTrue(out["alarm"])

    def test_latency_metrics(self):
        out = latency_metrics(10,20,13,2)
        self.assertEqual(out["detection_latency"],3)
        self.assertEqual(out["reaction_margin"],5)
        self.assertFalse(out["missed"])

if __name__ == "__main__":
    unittest.main()
