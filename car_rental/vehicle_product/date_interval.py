from datetime import date

class DateInterval:
    def __init__(self, from_date: date, to_date: date):
        if to_date < from_date:
            raise ValueError("End date cannot be before start date...")
        self.from_date = from_date
        self.to_date = to_date

    def overlaps(self, other: "DateInterval") -> bool:
        return not(self.to_date < other.from_date or self.from_date > other.to_date)