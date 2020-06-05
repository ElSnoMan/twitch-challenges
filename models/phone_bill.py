"""
A phone bill should have:

* ID
* Base Cost
* Number of allotted minutes
* Number of minutes used
"""
from pydantic.main import BaseModel


class PhoneBill:
    def __init__(self, _id, base_cost, alloted_minutes, minutes_used):
        self.id = _id
        self.base_cost = base_cost
        self.allotted_minutes = alloted_minutes
        self.minutes_used = minutes_used


class PhoneBillModel(BaseModel):
    id: int
    base_cost: float
    alloted_minutes: int
    minutes_used: int
