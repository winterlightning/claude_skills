'Left-facing Merlion with projecting muzzle, cheek arc and rounded body. Deliberate profile asymmetry; pointed mane band omitted to open the interior.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d6b18c3-9c28-4f4a-8e22-8679e1c298f6'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/merlion statue_4d6b18c3-9c28-4f4a-8e22-8679e1c298f6.svg'
AUTHOR = 'gpt-6'

class MerlionStatue(Solo48):
    icon_id = 'merlion-statue'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('merlion', 'singapore', 'statue', 'lion', 'fish', 'landmark', 'monument', 'mascot')

    def build(self) -> None:
        # VRECT_L centerline extremes (8,6)-(40,42).
        self.add_arc("crown", (20,12), (28,6), radius_x=8)
        self.add_arc("back-top", (28,6), (40,16), radius_x=12)
        self.add_line("back", (40,16), (40,30))
        self.add_arc("body-bottom", (40,30), (12,30), radius_x=14)
        self.add_line("chest-1", (12,30), (16,24))
        self.add_line("chest-2", (16,24), (14,24))
        self.add_arc("muzzle", (14,24), (14,12), radius_x=6)
        self.add_line("brow", (14,12), (20,12))
        self.add_contour("outline", "crown", "back-top", "back", "body-bottom", "chest-1", "chest-2", "muzzle", "brow", closed=True)
        self.add_arc("cheek", (27,17), (27,29), radius_x=4, radius_y=6)
