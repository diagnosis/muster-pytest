from dataclasses import dataclass, field


@dataclass
class Outing:
    title: str
    seats: int
    rider: list[str] = field(default_factory=list)

    def add_rider(self, name: str) -> None: ...
    def seats_left(self) -> int: ...


@dataclass
class Hiker:
    name: str
    experience: str = "beginner"
