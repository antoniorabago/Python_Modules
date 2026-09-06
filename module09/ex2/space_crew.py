#!/usr/bin/env python3

from enum import Enum
from datetime import datetime

from pydantic import BaseModel, Field, ValidationError, model_validator


class CrewRanks(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def safety_requirements(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            member.rank in (CrewRanks.COMMANDER, CrewRanks.CAPTAIN)
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_members = sum(
                member.years_experience >= 5
                for member in self.crew
            )
            if experienced_members / len(self.crew) < 0.5:
                raise ValueError(
                    "At least 50% of the crew must be experienced (5+ years)"
                )

        if not all(
            member.is_active
            for member in self.crew
        ):
            raise ValueError("All members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    crew = [
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=CrewRanks.COMMANDER,
                age=55,
                specialization="Mission Command",
                years_experience=20,
                is_active=True
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=CrewRanks.LIEUTENANT,
                age=30,
                specialization="Navigation",
                years_experience=10,
                is_active=True
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=CrewRanks.OFFICER,
                age=25,
                specialization="Engineering",
                years_experience=3,
                is_active=True
            )
    ]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 1, 1, 12, 0, 0),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0
    )
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}"
            )

    print("=========================================")
    print("Expected validation error:")
    try:
        crew = [
                    CrewMember(
                        member_id="CM002",
                        name="John Smith",
                        rank=CrewRanks.LIEUTENANT,
                        age=30,
                        specialization="Navigation",
                        years_experience=10,
                        is_active=True
                    ),
                    CrewMember(
                        member_id="CM003",
                        name="Alice Johnson",
                        rank=CrewRanks.OFFICER,
                        age=25,
                        specialization="Engineering",
                        years_experience=3,
                        is_active=True
                    )
            ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 1, 12, 0, 0),
            duration_days=900,
            crew=crew,
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
