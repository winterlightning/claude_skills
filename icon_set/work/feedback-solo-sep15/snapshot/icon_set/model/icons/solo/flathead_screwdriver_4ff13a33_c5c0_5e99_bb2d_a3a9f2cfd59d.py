"""A diagonal flathead screwdriver with chamfered grip and a broad transverse tip; tiny collar and handle marks omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ff13a33-c5c0-5e99-bb2d-a3a9f2cfd59d'
SOURCE_PATH = 'pictographic-primitives/tools/tools screwdriver_4ff13a33-c5c0-5e99-bb2d-a3a9f2cfd59d.svg'
AUTHOR = 'gpt-6'

class FlatheadScrewdriver(Solo48):
    icon_id = 'flathead-screwdriver'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('screwdriver', 'flathead', 'screw', 'hardware', 'repair', 'fix', 'shaft', 'tool')

    def build(self) -> None:


        self.add_polyline('handle',(6,18),(6,6),(18,6),(26,14),(26,22),(22,26),(14,26),closed=True)
        self.add_line('shaft',(24,24),(38,38))
        self.add_line('flat-tip',(34,42),(42,34))
        self.relate('connect','shaft','handle')
        self.relate('connect','shaft','flat-tip')
