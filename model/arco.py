from dataclasses import dataclass
@dataclass
class Arco:
    id1: str
    id2: str
    peso: float

    def __hash__(self):
        return hash(f"{self.id1} {self.id2}")