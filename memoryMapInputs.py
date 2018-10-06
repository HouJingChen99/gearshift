# Reading the clutch and shifter from rF2 using k3nny's Python 
# mapping of The Iron Wolf's rF2 Shared Memory Tools
# https://github.com/TheIronWolfModding/rF2SharedMemoryMapPlugin
# https://forum.studio-397.com/index.php?members/k3nny.35143/

from threading import Timer

from Mmap_for_DSPS_V22 import SimInfo

tickInterval = 0.1 # seconds

class Controls:
  def __init__(self):
    self.info = SimInfo()
    self.clutchState = self.__readClutch()
    self.currentGear = self.__readGear()
  def __readClutch(self):
    _c = self.info.Rf2Tele.mVehicles[0].mUnfilteredClutch # 1.0 clutch down, 0 clutch up
    # We want 100 clutch released, 0 clutch pressed
    return -(_c-1)*100
  def __readGear(self):
    return self.info.Rf2Tele.mVehicles[0].mGear  # -1 to number of gears, 0 is neutral
  def monitor(self):
    # Run every tickInterval
    if self.currentGear != self.__readGear():
      self.currentGear   = self.__readGear()
      self.callback(gearEvent=self.currentGear)
    if self.clutchState != self.__readClutch():
      self.clutchState   = self.__readClutch()
      self.callback(clutchEvent=self.clutchState)
    #print('tick')
    Timer(tickInterval, self.monitor, ()).start()

  def run(self, callback):
    """ Event loop """
    self.callback = callback
    Timer(tickInterval, self.monitor, ()).start()

def callback(clutchEvent=None, gearEvent=None):
    clutch = controls_o.clutchState
    gear   = controls_o.currentGear
    #TBD driver = info.Rf2Scor.mVehicles[0].mDriverName
    driver = 'Max Snell'
    print('Driver %s, Gear: %d, Clutch position: %d' % (driver, gear, clutch))

if __name__ == '__main__':
    controls_o = Controls()
    callback()  # show initial state
    controls_o.run(callback)


