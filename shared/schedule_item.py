"""ScheduleItem dataclass representing a course in the schedule."""

from dataclasses import dataclass


@dataclass
class ScheduleItem:
    """
    Represents a single course entry in the schedule.
    
    Attributes:
        subject: Course subject code (e.g., 'CS', 'MATH')
        catalog: Course catalog number (e.g., '101', '201')
        section: Section number (e.g., '001', '002')
        component: Course component type (e.g., 'LEC', 'LAB')
        session: Session number
        units: Credit units for the course
        tot_enrl: Total enrollment count
        cap_enrl: Enrollment capacity
        instructor: Instructor name (format: 'Last, First')
    """
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str

    def get_key(self) -> tuple:
        """Return composite key (subject, catalog, section) for tree ordering."""
        return (self.subject, self.catalog, self.section)

    def print(self) -> None:
        """Print formatted course information."""
        print(f"{self.subject:4} {self.catalog:6} {self.section:6} {self.component:8} "
              f"{self.session:4} {self.units:3} {self.tot_enrl:6} {self.cap_enrl:6} {self.instructor}")
