"""Exit target -> required ARR -> members needed. Standard library only."""
import math
from dataclasses import dataclass


@dataclass
class Segment:
    name: str
    members: int
    annual_price: float
    pays: bool


def required_arr(exit_value: float, revenue_multiple: float) -> float:
    if exit_value <= 0 or revenue_multiple <= 0:
        raise ValueError("exit_value and revenue_multiple must be > 0")
    return exit_value / revenue_multiple


def arr(segments: list[Segment]) -> float:
    """Sum of members * annual_price for paying segments; free segments count as zero."""
    return sum(s.members * s.annual_price for s in segments if s.pays)


def members_needed(target_arr: float, annual_price: float) -> int:
    if annual_price <= 0:
        raise ValueError("annual_price must be > 0")
    return math.ceil(target_arr / annual_price)
