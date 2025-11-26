from dataclasses import dataclass

@dataclass
class ScheduleItem:
    date: str
    time: str
    title: str
    description: str
    location: str

    def print(self) -> None:
        print(f"{self.date}  {self.time}  {self.title:20}  {self.location}")
