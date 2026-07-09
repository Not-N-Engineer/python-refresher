import numpy as np
import unittest
import physics as up
import numpy.testing as npt

class TestAuv2(unittest.TestCase):
    testTorque = [12.3, 32.5, 20, 8.4]
    def test_calculate_auv_acceleration(self):
        npt.assert_array_almost_equal(up.AUV2.calculate_auv2_acceleration(self.testTorque, 0, np.pi / 4, 15),[0.7731034, 0.7731034],  decimal = 7)
        npt.assert_array_almost_equal(up.AUV2.calculate_auv2_acceleration(self.testTorque, np.pi/4 , np.pi / 4, 15),[0, 1.0933333],  decimal = 7)
        testTorque1 = [-13.2, 12.76, 10, -18.4]
        npt.assert_array_almost_equal(up.AUV2.calculate_auv2_acceleration(testTorque1, np.pi/5 , np.pi / 3, 15),[-0.0554698, 0.5277596],  decimal = 7)

    def test_calculate_auv_angular_accelration(self):
        self.assertAlmostEqual(up.AUV2.calculate_auv2_angular_acceleration(self.testTorque, np.pi/4, 0.5, 0.3, 12.27), -0.3964869,  places = 7)
        self.assertAlmostEqual(up.AUV2.calculate_auv2_angular_acceleration(self.testTorque, 2.6011732, 0.5, 0.3, 12.27), 0,  places = 7)
        testTorque1 = [12.27, 3.27, 3.8, 5.15]
        self.assertAlmostEqual(up.AUV2.calculate_auv2_angular_acceleration(testTorque1, 1.09, 0.516, 0.3, 12.27), 0.3717421,  places = 7)

test = TestAuv2()
test.test_calculate_auv_acceleration()