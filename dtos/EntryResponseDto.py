from dataclasses import dataclass, asdict

@dataclass
class EntryResponseDto:

    year: int
    country :str
    artistName: str
    songName: str
    runningOrder: int
    points: int
    place: int

    def to_json(self):
        # converting dictionary for json serialisation
        return asdict(self)
