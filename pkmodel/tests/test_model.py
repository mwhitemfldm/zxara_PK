import unittest
import pkmodel as pk
class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_create(self):
        """
        Tests Model creation.
        """
        model = pk.model.Model([5.5, 6.1], [[1,2],[0.001, 2]], [])
        self.assertEqual(model.central, [5.5, 6.1])
        self.assertEqual(model.peripherals, [[1,2],[0.001, 2]])
        self.assertEqual(model.dose, [])
    
    def test_pcount(self):
        """
        Tests Model counts peripheral compartments.
        """
        model = pk.model.Model([5.5, 6.1], [[1,2],[0.001, 2]], [])
        self.assertEqual(model.pcount, 2)
    
        



