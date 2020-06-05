from challenges.test_phone_bill_calc import convert_string_to_number, PhoneBillCalculator


"""
A phone bill should have:

* ID
* Base Cost
* Number of allotted minutes
* Number of minutes used

Based off the Phone Bill, one should be able to calculate
the overage, tax, and total on a phone bill. (Print it too)

Create a class that instantiates the phone bill and prints
the itemized bill.
"""


def phone_bill_calculator():
    plan_cost = input('Enter the plan cost: ')
    overage_minutes = input('Enter the overage minutes: ')
    calc = PhoneBillCalculator()

    print('\n--\nPhone Bill Statement')

    num_plan_cost = convert_string_to_number(plan_cost)
    print(f'Plan: ${plan_cost}')

    num_overages = convert_string_to_number(overage_minutes)
    print(f'Overage: ${calc.calculate_overages(num_overages)}')

    tax = calc.calculate_tax(num_plan_cost, num_overages)
    print(f'Tax: ${tax}')

    total = calc.calculate_final_total(num_plan_cost, num_overages)
    print(f'Total: ${total}')


if __name__ == '__main__':
    phone_bill_calculator()
