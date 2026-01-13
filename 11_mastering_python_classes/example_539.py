# file name: example_539.py

from dataclasses import dataclass, field

@dataclass
class Team:
    
    members: list = field(default_factory=list)
