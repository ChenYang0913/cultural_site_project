import heapq
from enum import Enum

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class VisitorGroup:
    def __init__(self, group_ID, arrival_time, priority):
        self.group_ID = group_ID
        self.arrival_time = arrival_time
        self.priority = priority

    def __lt__(self, other):
        if self.priority.value == other.priority.value:
            return self.arrival_time < other.arrival_time
        return self.priority.value < other.priority.value
