"""A crossed tool emblem with open wrench ends, diagonal screwdriver grip and flat tip; double shaft outlines are reduced to single crossing strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b935d53-8cae-4d27-b6e5-0fed82d9789e'
SOURCE_PATH = 'pictographic-primitives/tools/tools wrench screwdriver_8b935d53-8cae-4d27-b6e5-0fed82d9789e.svg'
AUTHOR = 'gpt-6'

class CrossedWrenchAndScrewdriver(Solo48):
    icon_id = 'crossed-wrench-and-screwdriver'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('wrench', 'screwdriver', 'tools', 'repair', 'settings', 'maintenance', 'service', 'fix')

    def build(self) -> None:


        self.add_polyline('upper-jaw',(6,6),(6,18),(18,18),(18,6))
        self.add_line('wrench-shaft',(18,18),(30,30))
        self.add_polyline('lower-jaw',(30,42),(30,30),(42,30))
        self.relate('connect','upper-jaw','wrench-shaft')
        self.relate('connect','lower-jaw','wrench-shaft')
        self.add_polyline('grip',(6,34),(14,26),(22,34),(14,42),closed=True)
        self.add_line('driver-shaft',(18,30),(42,6))
        self.add_polyline('tip',(34,6),(42,6),(42,14))
        self.relate('connect','driver-shaft','grip')
        self.relate('connect','driver-shaft','wrench-shaft')
        self.relate('connect','driver-shaft','tip')
