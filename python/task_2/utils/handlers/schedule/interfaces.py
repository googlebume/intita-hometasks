from typing import Tuple, Dict, Protocol

DaySchedule = Dict[str, int]

WeekSchedule = Dict[str, DaySchedule]

AllHours = Dict[str, Dict[str, int] | int]

class SchadleInterface(Protocol):
    def get_all_days(self) -> Tuple[str, str, str, str, str, str, str]:
        ...
    
    def get_all_schadle(self) -> WeekSchedule:
        ...
    
    def calc_all_hours(self) -> AllHours:
        ...
    
    def clac_longest_day(self) -> int:
        ...
    
    def get_schadle_load(self) -> None:
        ...
