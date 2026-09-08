"""Rounded carved post with paired eyes and broad wings; repeated feather blades omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b09e3b5-da0d-5455-8cea-f2bea6fe2da4'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/totem pole_1b09e3b5-da0d-5455-8cea-f2bea6fe2da4.svg'
AUTHOR = 'gpt-6'

class WingedTotemPole(Solo48):
    icon_id = 'winged-totem-pole'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('totem', 'pole', 'carving', 'wings', 'indigenous', 'monument', 'tribal', 'landmark')

    def build(self) -> None:
        # Centerline extremes (2, 2, 46, 46).
        self.add_arc("head", (14,12), (34,12), radius_x=10)
        self.add_line("post-1", (34, 12), (34, 18))
        self.add_line("post-2", (34, 18), (34, 32))
        self.add_line("post-3", (34, 32), (34, 46))
        self.add_line("post-4", (34, 46), (14, 46))
        self.add_line("post-5", (14, 46), (14, 32))
        self.add_line("post-6", (14, 32), (14, 18))
        self.add_line("post-7", (14, 18), (14, 12))
        self.add_contour("body", "head", "post-1", "post-2", "post-3", "post-4", "post-5", "post-6", "post-7", closed=True)
        self.add_dot("eye-left", (21,13))
        self.add_dot("eye-right", (27,13))
        self.add_polyline("wing-left", (14,18), (2,18), (2,25), (14,32))
        self.add_polyline("wing-right", (34,18), (46,18), (46,25), (34,32))
        self.relate("connect", "body", "wing-left")
        self.relate("connect", "body", "wing-right")
