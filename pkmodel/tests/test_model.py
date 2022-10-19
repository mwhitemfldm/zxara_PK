import unittest
import pkmodel as pk
import pytest
class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """

    @pytest.mark.parametrize(
    "Centrals, Peripherals, Dosings",
    [
        ([5.5, 6.1], [[1,2],[0.001, 2]], []),
    ])
    def test_create(self, Centrals, Peripherals, Dosings):
        """
        Tests Model creation.
        """
        model = pk.model.Model(central=Centrals, peripherals=Peripherals, dosing=Dosings)
        self.assertEqual(model.central, Centrals)
        self.assertEqual(model.peripherals, Peripherals)
        self.assertEqual(model.dose, Dosings)
        



