import sys
from enum import Enum
from datetime import datetime
from typing import List

try:
    from pydantic import (BaseModel, Field, ValidationError,  # type: ignore
                          model_validator)
except ImportError:
    print("Error in importing library, maybe it doesn't exist")
    print("Try: pip install pydantic")
    sys.exit(1)


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):  # type: ignore
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):  # type: ignore
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')  # type: ignore
    def validation_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")
        required_rank = False
        for crew in self.crew:
            if crew.rank == Rank.COMMANDER or crew.rank == Rank.CAPTAIN:
                required_rank = True
        if not required_rank:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            crew_experience = 0
            for crew in self.crew:
                if crew.years_experience > 5:
                    crew_experience += 1
            if crew_experience / ((len(self.crew))) < 0.5:
                raise ValueError(" Long missions (> 365 days) need 50% "
                                 "experienced crew (5+ years)")
        if not all(crew.is_active for crew in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    try:
        print("=========================================")
        print("Valid mission created:")
        crew_member: List[CrewMember] = [
            CrewMember(
                member_id="HS-W40",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=55,
                specialization="Mission Command",
                years_experience=25,
            ),
            CrewMember(
                member_id="DV-P212",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=10,
            ),
            CrewMember(
                member_id="KF-00",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=30,
                specialization="Engineering",
                years_experience=5,
            )
        ]
        valid_space_mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mission: Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=crew_member,
            budget_millions=2500.0,
        )
    except ValidationError as err:
        for error in err.errors():
            message = (error['msg'].split(',')[1].strip()
                       if ',' in error['msg'] else error['msg'])
            print(message)
    else:
        print(f"Mission: {valid_space_mission.mission_name}")
        print(f"ID: {valid_space_mission.mission_id}")
        print(f"Destination: {valid_space_mission.destination}")
        print(f"Duration: {valid_space_mission.duration_days} days")
        print(f"Budget: ${valid_space_mission.budget_millions}M")
        print(f"Crew size: {len(crew_member)}")
        print("Crew members:")
        for crew in crew_member:
            print(f"- {crew.name} ({crew.rank.value}) - {crew.specialization}")
    print()
    try:
        print("=========================================")
        print("Expected validation error:")
        invalid_crew_member: List[CrewMember] = [
            CrewMember(
                member_id="HS-W40",
                name="Sarah Conor",
                rank=Rank.OFFICER,
                age=55,
                specialization="Mission command",
                years_experience=15,
            ),
            CrewMember(
                member_id="DV-P212",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=2,
            ),
            CrewMember(
                member_id="KF-00",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=30,
                specialization="Engineering",
                years_experience=5,
            )
        ]
        invalid_space_mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mission: Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=invalid_crew_member,
            budget_millions=3500.0,
        )
    except ValidationError as err:
        for error in err.errors():
            message = (error['msg'].split(',')[1].strip()
                       if ',' in error['msg'] else error['msg'])
            print(message)

    else:
        print(f"Mission: {invalid_space_mission.mission_name}")
        print(f"ID: {invalid_space_mission.mission_id}")
        print(f"Destination: {invalid_space_mission.destination}")
        print(f"Duration: {invalid_space_mission.duration_days} days")
        print(f"Budget: ${invalid_space_mission.budget_millions}M")
        print(f"Crew size: {len(invalid_crew_member)}")
        print("Crew members:")
        for crew in invalid_crew_member:
            print(f"- {crew.name} ({crew.rank.value}) - {crew.specialization}")


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    main()
