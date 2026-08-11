import sys
from enum import Enum
from datetime import datetime
from typing import Optional


try:
    from pydantic import (BaseModel, Field, ValidationError,  # type: ignore
                          model_validator)
except ImportError:
    print("Error in importing library, maybe it doesn't exist")
    print("Try: pip install pydantic")
    sys.exit(1)


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):  # type: ignore
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')  # type: ignore
    def validation_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic and \
                self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 "
                             "witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(" Strong signals (> 7.0) should include "
                             "received messages")
        return self


def main() -> None:
    try:
        print("======================================")
        print("Valid contact report:")
        valid_alien: AlienContact = AlienContact(
            contact_id="AC-2024-01",
            timestamp=datetime.now(),
            location=" Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )

    except ValidationError as err:
        for error in err.errors():
            message = (error['msg'].split(',')[1].strip()
                       if ',' in error['msg'] else error['msg'])
            print(message)
    else:
        print(f"ID: {valid_alien.contact_id}")
        print(f"Type: {valid_alien.contact_type.value}")
        print(f"Location: {valid_alien.location}")
        print(f"Signal: {valid_alien.signal_strength}/10")
        print(f"Duration: {valid_alien.duration_minutes} minutes")
        print(f"Witnesses: {valid_alien.witness_count}")
        print(f"Message: {valid_alien.message_received!r}")
    print()
    try:
        print("======================================")
        print("Expected validation error:")
        invalid_alien: AlienContact = AlienContact(
            contact_id="AC-2024-01",
            timestamp=datetime.now(),
            location=" Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )

    except ValidationError as err:
        for error in err.errors():
            message = (error['msg'].split(',')[1].strip()
                       if ',' in error['msg'] else error['msg'])
            print(message)
    else:
        print(f"ID: {invalid_alien.contact_id}")
        print(f"Type: {invalid_alien.contact_type.value}")
        print(f"Location: {invalid_alien.location}")
        print(f"Signal: {invalid_alien.signal_strength}/10")
        print(f"Duration: {invalid_alien.duration_minutes} minutes")
        print(f"Witnesses: {invalid_alien.witness_count}")
        print(f"Message: {invalid_alien.message_received!r}")


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    main()
