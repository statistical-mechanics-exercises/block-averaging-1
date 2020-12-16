import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_mean(self) : 
        self.assertTrue( "average" in globals(), "there is no variable called average" )
        myeng = sum( eng ) / len( eng )
        self.assertTrue( np.abs(myeng - average) < 1e-7, "The average value you have calculated is incorrect" )
