"""A Dutch windmill with four diagonal sails, tapered base and arched door. Broad sail outlines reduce to four clear spokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95c449a5-8e44-5a99-9486-caf1e3e38105'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/netherlands windmill_95c449a5-8e44-5a99-9486-caf1e3e38105.svg'
AUTHOR = 'gpt-6'


class Windmill(Solo48):
    icon_id = 'windmill'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('windmill', 'netherlands', 'dutch', 'mill', 'sails', 'landmark', 'countryside', 'energy')

    def build(self) -> None:
        # Centerline extremes (5,2)-(43,46).
        self.add_polyline("sail-down", (5,2), (24,16), (43,30))
        self.add_polyline("sail-up", (5,30), (24,16), (43,2))
        self.relate("connect", "sail-down", "sail-up")
        self.add_polyline("body", (15,33), (8,46), (18,46))
        self.add_line("door-left", (18,46), (18,40))
        self.add_arc("door-arch", (18,40), (30,40), radius_x=6)
        self.add_line("door-right", (30,40), (30,46))
        self.add_polyline("body-right", (30,46), (40,46), (33,33))
        self.add_contour("door", "door-left", "door-arch", "door-right")
        self.relate("connect", "body", "door")
        self.relate("connect", "body-right", "door")
