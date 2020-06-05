"""
Calculate the final total of someone's phone bill.
Allow the operator to input the plan fee and the number of overage minutes.
Charge the user 0.25 for every minute they were over their plan,
and 15% tax on the subtotal.

Create the separate methods to calculate the tax, overage fees, and final total.
Print the itemized bill.
"""
import pytest

from models.phone_bill import PhoneBillModel

""" Example Output
Enter base cost of the plan:
82.45

Enter overage minutes:
9
--
Phone Bill Statement
Plan: $82.45
Overage: $2.25
Tax: $12.71
Total: $97.41
"""


PLAN_COST = 82.45
OVERAGE_MIN = 9


def convert_float_to_dollars(number: float):
    return f'${number}'


def convert_string_to_number(string: str):
    return float(string)


class PhoneBillCalculator:
    def __init__(self, phone_bill: PhoneBillModel):
        self.phone_bill = phone_bill

    def calculate_overages(self):
        minutes_over = self.phone_bill.minutes_used - self.phone_bill.alloted_minutes
        if minutes_over <= 0:
            return 0
        return minutes_over * 0.25

    def calculate_tax(self):
        subtotal = self.phone_bill.base_cost + self.calculate_overages()
        return round(subtotal * 0.15, 2)

    def calculate_final_total(self):
        tax = self.calculate_tax()
        overage = self.calculate_overages()
        return round(self.phone_bill.base_cost + tax + overage, 2)


@pytest.fixture
def calculator():
    phone_bill = PhoneBillModel(id=1, base_cost=82.45, alloted_minutes=100, minutes_used=109)
    return PhoneBillCalculator(phone_bill)


def test_convert_float_to_dollars():
    dollars = convert_float_to_dollars(PLAN_COST)
    assert dollars == '$82.45'


def test_convert_string_to_number():
    number = convert_string_to_number('82.45')
    assert number == 82.45
    ten = convert_string_to_number('10')
    assert ten == 10.0 == 10


def test_overage_fees():
    phone_bill = PhoneBillModel(id=1, base_cost=82.45, alloted_minutes=100, minutes_used=109)
    overages = PhoneBillCalculator(phone_bill).calculate_overages()
    assert overages == 2.25


def test_no_overage_fees():
    phone_bill = PhoneBillModel(id=1, base_cost=82.45, alloted_minutes=100, minutes_used=100)
    overages = PhoneBillCalculator(phone_bill).calculate_overages()
    assert overages == 0


def test_no_overages_if_minutes_used_is_under_alloted_minutes():
    phone_bill = PhoneBillModel(id=1, base_cost=82.45, alloted_minutes=100, minutes_used=95)
    overages = PhoneBillCalculator(phone_bill).calculate_overages()
    assert overages == 0


def test_calculate_tax(calculator):
    assert calculator.calculate_tax() == 12.71


def test_final_total(calculator):
    total = calculator.calculate_final_total()
    assert total == 97.41
