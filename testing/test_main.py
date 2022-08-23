try:
    from AutoFeedback.varchecks import check_vars
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.varchecks import check_vars

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_mean(self) : 
        myeng = sum( eng ) / len( eng )
        assert(check_vars("average",myeng))
