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

    def get_key(self) -> str:
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self) -> None:
        print(f"{self.subject:4} {self.catalog:6} {self.section:6} "
              f"{self.component:8} {self.session:4} {self.units:3} "
              f"{self.tot_enrl:6} {self.cap_enrl:6} {self.instructor}")
