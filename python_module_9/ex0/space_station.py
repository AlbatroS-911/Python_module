from datetime import datetime
from typing import Optional
import sys
try:
    from pydantic import BaseModel, Field, ValidationError  # type: ignore
except ImportError:
    print("Error in importing library, maybe it doesn't exist")
    sys.exit(1)


class SpaceStation(BaseModel):  # type: ignore
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    try:
        print("========================================")
        print("Valid station created:")
        valid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
        )

    except ValidationError as err:
        for error in err.errors():
            print(error['msg'])
    else:
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        space_status = ("Operational" if valid_station.is_operational
                        else "Standby")
        print(f"Status: {space_status}")
    print()
    try:
        print("========================================")
        print("Expected validation error:")
        invalid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=100,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
        )
    except ValidationError as err:
        for error in err.errors():
            print(error['msg'])
    else:
        print(f"ID: {invalid_station.station_id}")
        print(f"Name: {invalid_station.name}")
        print(f"Crew: {invalid_station.crew_size} people")
        print(f"Power: {invalid_station.power_level}")
        print(f"Oxygen: {invalid_station.oxygen_level}")
        space_status = ("Operational" if invalid_station.is_operational
                        else "Standby")
        print(f"Status: {space_status}")


if __name__ == "__main__":
    print("Space Station Data Validation")
    main()
