from dataclasses import dataclas

@dataclass
class BoardGameFeatures:
    averageweight: float
    playingtime: int
    family: str,
    rule_count: int
    average_rule_len: float