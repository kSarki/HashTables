from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str

    def print(self) -> None:
        print(f"{self.subject:4} {self.catalog:6} {self.section:6} {self.component:8} "
              f"{self.session:4} {self.units:3} {self.tot_enrl:6} {self.cap_enrl:6} {self.instructor}")
