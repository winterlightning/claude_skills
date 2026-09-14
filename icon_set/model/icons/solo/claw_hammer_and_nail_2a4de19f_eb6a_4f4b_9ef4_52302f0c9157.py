"""A diagonal claw hammer beside an upright nail; claw silhouette and separate nail retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a4de19f-eb6a-4f4b-9ef4-52302f0c9157'
SOURCE_PATH = 'pictographic-primitives/tools/hardware hammer nail_2a4de19f-eb6a-4f4b-9ef4-52302f0c9157.svg'
AUTHOR = 'gpt-6'

class ClawHammerAndNail(Solo48):
    icon_id = 'claw-hammer-and-nail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('hammer', 'claw hammer', 'nail', 'hardware', 'construction', 'carpentry', 'build', 'tool')

    def build(self) -> None:
        self.add_polyline('head',(10,6),(24,6),(36,18),(28,26),(23,21),(6,38),(6,26),(17,15),(10,6))
        self.add_line('nail-head',(32,34),(42,34))
        self.add_line('nail-shank',(37,34),(37,42))
        self.relate('connect','nail-head','nail-shank')
