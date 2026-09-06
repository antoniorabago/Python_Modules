#!/usr/bin/env python3

from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def business_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact must be verified")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contact must "
                             "have at least 3 witnesses")
        if (
            self.signal_strength > 7.0
            and self.message_received is None
        ):
            raise ValueError("Strong signals should include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    contact_report = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2026, 1, 1, 12, 0, 0),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="'Greetings from Zeta Reticuli'")
    print(f"ID: {contact_report.contact_id}")
    print(f"Type: {contact_report.contact_type.value}")
    print(f"Location: {contact_report.location}")
    print(f"Signal: {contact_report.signal_strength}/10")
    print(f"Duration: {contact_report.duration_minutes} minutes")
    print(f"Witnesses: {contact_report.witness_count}")
    print(f"Message: {contact_report.message_received}")

    print("\n======================================")
    print("Expected validation error:")
    try:
        contact_report = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2026, 1, 1, 12, 0, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="'Greetings from Zeta Reticuli'")
        print(contact_report)
    except ValidationError as e:
        print(e.errors()[0]["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
