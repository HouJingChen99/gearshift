import unittest

from Gearshift import main

class Test_Gearshift(unittest.TestCase):
  def test_Gearshift_main_runs(self):
    # Preliminary test - does main run?
    root, controls_o = main()
    controls_o.stop()
    assert root != None

if __name__ == '__main__':
  unittest.main(exit=False)