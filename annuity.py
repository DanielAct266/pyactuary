""" 
    In development: Open Source Library that will include all financial and statistical 
    elements for computing common actuarial utilities, like annuities, bonds, financial
    instruments and premium values for several insurance classical models.
"""

from abc import ABCMeta, abstractmethod


class Annuity(metaclass=ABCMeta):
    """
        Class for representing a general Annuity structure
    """
    def __init__(self, interest, periods):
        self._interest = interest
        self._periods = periods
        self._discount = 1 / (1 + interest)

    @abstractmethod
    def present_value(self):
        pass

    @abstractmethod
    def future_value(self):
        pass

    @property
    @abstractmethod
    def interest(self):
        pass

    @interest.setter
    @abstractmethod
    def interest(self, value):
        pass
    
    @property
    @abstractmethod
    def discount(self):
        pass

    @discount.setter
    @abstractmethod
    def discount(self, value):
        pass

    @property
    @abstractmethod
    def periods(self):
        pass

    @periods.setter
    @abstractmethod
    def periods(self, value):
        pass

class ImmediateAnnuity(Annuity):
    """
        Some Docstring
    """
    def present_value(self):
        return (1 - self._discount ** self._periods) / self._interest
    def future_value(self):
        return ((1 + self._interest) ** self._periods - 1)/ self._interest

    @property
    def interest(self):
        return self._interest

    @property
    def periods(self):
        return self._periods

    @property
    def discount(self):
        return self._discount

    @interest.setter
    def interest(self, value):
        self._interest = value

    @periods.setter
    def periods(self, value):
        self._periods = value

class DueAnnuity(Annuity):
    """
        Some Docstring
    """
    def present_value(self):
        return (1 - self._discount ** self._periods) / (self._interest * self._discount)
    def future_value(self):
        return ((1 + self._interest) ** self._periods - 1)/ (self._interest * self._discount)

    @property
    def interest(self):
        return self._interest

    @property
    def periods(self):
        return self._periods

    @property
    def discount(self):
        return self._discount

    @interest.setter
    def interest(self, value):
        self._interest = value

    @periods.setter
    def periods(self, value):
        self._periods = value

class ImmediatePerpetuity(ImmediateAnnuity):
    """
        Some docstring
    """
    def present_value(self):
        return 1 / self._interest
    def future_value(self):
        return None

    @property
    def periods(self):
        return self._periods

    @periods.setter
    def periods(self, value):
        self._periods = None

class Bond:
    """
        Represents a Financial Bond
    """
    def __init__(self, par_value, redemption_value, coupon_rate, yield_rate, periods):
        self._par_value = par_value
        self._redemption_value = redemption_value
        self._coupon_rate = coupon_rate
        self._yield_rate = yield_rate
        self._periods = periods
        self._annuity = DueAnnuity(yield_rate, periods)

    @property
    def par_value(self):
        """
            Par Value of the Bond
        """
        return self._par_value

    @property
    def redemption_value(self):
        """
            Redemption Value
        """
        return self._redemption_value

    @property
    def coupon_rate(self):
        """
            Coupon Rate 
        """
        return self._coupon_rate

    @property
    def yield_rate(self):
        """
            Yield Rate
        """
        return self._yield_rate

    @property
    def periods(self):
        """
            Number of periods for the given bond.
        """
        return self._periods

    def price(self):
        """
            Price at present value of a bond
        """
        price = (
            self._par_value * self._coupon_rate * self._annuity.present_value()
            + self._redemption_value * (1 / 1 + self._yield_rate) ** self._periods
        )

        return price

if __name__ == "__main__":

    annuity = ImmediateAnnuity(
        0.1, 10
    )

    print(annuity.present_value())
    print(annuity.future_value())

    annuity = ImmediatePerpetuity(
        0.1, 10
    )

    annuity.periods = 10
    print(annuity.present_value())

    bond = Bond(
        100, 100, .05, .1, 100)

    print(bond.price())
