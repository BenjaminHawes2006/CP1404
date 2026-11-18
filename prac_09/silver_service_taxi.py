"""
CP1404 Practical 9
Silver service taxi subclass of taxi
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.5
    def __init__(self, fanciness: float, **kwargs):
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return (self.price_per_km * self.current_fare_distance) + self.flagfall