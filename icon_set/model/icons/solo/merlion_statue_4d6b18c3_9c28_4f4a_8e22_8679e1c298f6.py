"""Profile lion muzzle and rounded fish body with tail band. Reference faces left; deliberate asymmetry retained. Tiny facial details omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d6b18c3-9c28-4f4a-8e22-8679e1c298f6'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/merlion statue_4d6b18c3-9c28-4f4a-8e22-8679e1c298f6.svg'
AUTHOR = 'gpt-6'

class MerlionStatue(Solo48):
    icon_id = 'merlion-statue'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('merlion', 'singapore', 'statue', 'lion', 'fish', 'landmark', 'monument', 'mascot')

    def build(self) -> None:
        # Centerline extremes (5, 2, 43, 46).
        self.add_arc("crown", (19,10), (31,2), radius_x=12, radius_y=8)
        self.add_arc("back-top", (31,2), (43,14), radius_x=12)
        self.add_line("back", (43,14), (43,30))
        self.add_arc("tail", (43,30), (11,30), radius_x=16, radius_y=16)
        self.add_line("chest-1", (11, 30), (17, 22))
        self.add_line("chest-2", (17, 22), (11, 22))
        self.add_arc("muzzle-bottom", (11,22), (11,10), radius_x=6, sweep=True)
        self.add_line("muzzle-top", (11,10), (19,10))
        self.add_contour("outline", "crown", "back-top", "back", "tail", "chest-1", "chest-2", "muzzle-bottom", "muzzle-top", closed=True)
        self.add_polyline("fish-band", (11,30), (21,36), (31,30), (43,30))
        self.relate("connect", "outline", "fish-band")
        self.add_arc("mane", (29,12), (29,24), radius_x=6, sweep=True)
