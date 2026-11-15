from datetime import datetime
from typing import Literal

from pydantic import BaseModel

Difficulty = Literal["easy", "moderate", "hard"]
Pace = Literal["relaxed", "moderate", "fast"]
RequestStatus = Literal["requested", "accepted", "declined", "withdrawn", "removed"]
Role = Literal["rider", "driver"]
Experience = Literal["beginner", "intermediate", "experienced"]


class Capacity(BaseModel):
    people_count: int
    seat_capacity: int
    seats_short: int
    spots_left: int
    waiting_count: int


class Outing(BaseModel):
    id: str
    host_id: str
    title: str
    destination: str
    meet_label: str
    starts_at: datetime
    max_size: int
    host_seats: int
    cost_per_seat_cents: int
    difficulty: Difficulty
    pace: Pace
    conversation_id: str
    ends_at: datetime | None = None
    phase: str
    status: str
    capacity: Capacity | None = None


class Page(BaseModel):
    items: list[Outing]
    next_cursor: str | None = None


class JoinRequest(BaseModel):
    id: str
    outing_id: str
    hiker_id: str
    status: RequestStatus
    role: Role
    seats_offered: int
    guests: int
    requested_at: datetime


class Member(BaseModel):
    hiker_id: str | None = None
    request_id: str | None = None
    name: str
    experience: str


class ListHiker(BaseModel):
    name: str
    role: Role
    seats_offered: int
    guests: int
    is_me: bool


class Detail(BaseModel):
    outing: Outing
    host: Member
    roster: list[Member]
    waiting: list[ListHiker]
    waiting_count: int
    withdrawn: list[ListHiker]
    my_request: JoinRequest | None = None
    seat_capacity: int
    people_count: int
    seats_short: int
    spots_left: int


class MessageResponse(BaseModel):
    message: str


class Hiker(BaseModel):
    id: str
    email: str
    name: str
    experience: Experience
    home_area: str | None = None
    bio: str | None = None
    gender: str | None = None
    created_at: datetime
    updated_at: datetime
    verified_at: datetime | None = None
