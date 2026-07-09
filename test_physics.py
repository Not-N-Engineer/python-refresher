import unittest
import physics as p 
import numpy as np


class TestAUVPhysics(unittest.TestCase):
    def test_calculate_bouyancy(self):
        self.assertEqual(p.AUVPhysics.calculate_bouyancy(1, 1000), 9810.0)
        self.assertEqual(p.AUVPhysics.calculate_bouyancy(0, 1000), 0)         # zero volume
        self.assertEqual(p.AUVPhysics.calculate_bouyancy(-1, 1000), -9810.0)  # negative volume
        self.assertAlmostEqual(p.AUVPhysics.calculate_bouyancy(2, 1000), p.AUVPhysics.calculate_bouyancy(1, 2000), places=5)  # scales same either way

        with self.assertRaises(TypeError):
            p.AUVPhysics.calculate_bouyancy("a", 1000)
        with self.assertRaises(TypeError):
            p.AUVPhysics.calculate_bouyancy([1], 1000)

    def test_will_it_float(self):
        self.assertEqual(p.AUVPhysics.will_it_float(1, 500), True)   # should float (500 kg < 1000 kg displaced)
        self.assertEqual(p.AUVPhysics.will_it_float(1, 1500), False)  # should sink

    def test_calculate_pressure(self):
        self.assertAlmostEqual(p.AUVPhysics.calculate_pressure(10), 98100.0, places=5)
        self.assertEqual(p.AUVPhysics.calculate_pressure(0), 0)
        self.assertAlmostEqual(p.AUVPhysics.calculate_pressure(-5), -49050.0, places=5)  # negative depth

        with self.assertRaises(TypeError):
            p.AUVPhysics.calculate_pressure("a")

    def test_calculate_acceleration(self):
        self.assertAlmostEqual(p.AUVPhysics.calculate_acceleration(10, 2), 5.0, places=5)
        self.assertAlmostEqual(p.AUVPhysics.calculate_acceleration(-10, 2), -5.0, places=5)

        with self.assertRaises(ValueError):
            p.AUVPhysics.calculate_acceleration(10, 0)  # zero mass

        with self.assertRaises(TypeError):
            p.AUVPhysics.calculate_acceleration("a", 2)
        with self.assertRaises(TypeError):
            p.AUVPhysics.calculate_acceleration(10, "a")

    def test_calculate_angular_acceleration(self):
        self.assertAlmostEqual(p.AUVPhysics.calculate_angular_acceleration(10, 2), 5.0, places=5)
        self.assertAlmostEqual(p.AUVPhysics.calculate_angular_acceleration(-10, 2), -5.0, places=5)

        with self.assertRaises(ValueError):
            p.AUVPhysics.calculate_angular_acceleration(10, 0), -1  # zero inertia

        with self.assertRaises(TypeError):
            p.AUVPhysics.calculate_angular_acceleration("a", 2)
        with self.assertRaises(TypeError):
            p.AUVPhysics.calculate_angular_acceleration(10, "a")

    def test_calculate_torque(self):
        self.assertAlmostEqual(p.AUVPhysics.calculate_torque(10, 0, 2), 20.0, places=5)  # cos(0) = 1
        self.assertEqual(p.AUVPhysics.calculate_torque(10, 0, 0), 0)                     # zero radius

        # cos(pi/2) ~ 0, so torque blows up toward infinity
        result = p.AUVPhysics.calculate_torque(10, np.pi / 2, 1)
        self.assertGreater(abs(result), 1e10)

        with self.assertRaises(TypeError):
            p.AUVPhysics.calculate_torque("a", 0, 1)

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(p.AUVPhysics.calculate_moment_of_inertia(2, 3), 18)
        self.assertEqual(p.AUVPhysics.calculate_moment_of_inertia(5, 0), 0)    # zero radius
        self.assertEqual(p.AUVPhysics.calculate_moment_of_inertia(2, -3), 18)  # r is squared, sign shouldn't matter

        with self.assertRaises(TypeError):
            p.AUVPhysics.calculate_moment_of_inertia("a", 2)


class TestAUV1(unittest.TestCase):
    def test_calculate_auv_acceleration(self):
        # F_x = F_magnitude / cos(F_angle); accel = F_x / m
        self.assertAlmostEqual(p.AUV1.calculate_auv_acceleration(10, 0.1, 50), 0.2010041836800911, places=8)

        with self.assertRaises(ValueError):
            p.AUV1.calculate_auv_acceleration(10, 0.1, 0)

        with self.assertRaises(TypeError):
            p.AUV1.calculate_auv_acceleration("a", 0.1, 50)

    def test_calculate_auv_angular_acceleration(self):
        self.assertAlmostEqual(p.AUV1.calculate_auv_angular_acceleration(10, 0.1), -9.344294837591955, places=8)

        with self.assertRaises(ValueError):
            p.AUV1.calculate_auv_angular_acceleration(10, 0.1, 0)

        with self.assertRaises(TypeError):
            p.AUV1.calculate_auv_angular_acceleration("a", 0.1)


class TestAUV2(unittest.TestCase):
    def test_calculate_AUV2_acceleration(self):
        result = p.AUV2.calculate_auv2_acceleration(np.array([1.0, 2.0, 3.0, 4.0]), 0.5, 0.3)
        self.assertIsInstance(result, np.ndarray)

        result = p.AUV2.calculate_auv2_acceleration([1.0, 2.0, 3.0, 4.0], 0.5, 0.3)
        self.assertIsInstance(result, np.ndarray)

    def test_calculate_AUV2_angular_acceleration(self):
        result = p.AUV2.calculate_auv2_angular_acceleration(np.array([1.0, 2.0, 3.0, 4.0]), 0.5, 1.0, 1.0)
        self.assertIsInstance(result, np.float64)


if __name__ == "__main__":
    unittest.main()