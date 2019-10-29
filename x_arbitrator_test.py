# pylint: skip-file
"""
Testfil for arbitrator-klassen
"""
import unittest
from arbitrator import Arbitrator
from bbcon import BBCON
from behavior import Behavior


class TestArbitrator(unittest.TestCase):

    def test_choose_action(self):
        bbcon = BBCON([])
        b1 = Behavior(bbcon, None, [("m1", 20), ("m2", 30)], True, False, 0.5, 0.6)
        b2 = Behavior(bbcon, None, [("m1", 30), ("m2", 15)], True, False, 0.3, 0.9)
        b3 = Behavior(bbcon, None, [("m1", 40), ("m2", 10)], True, False, 0.7, 0.8)
        bbcon.add_behavior(b1)
        bbcon.add_behavior(b2)
        bbcon.add_behavior(b3)
        for b in bbcon.behaviors:
            bbcon.active_behavior(b)
        arb = Arbitrator(bbcon)
        print(arb.choose_action())


if __name__ == '__main__':
    unittest.main()