"""A rounded bear face with two ears and a broad round muzzle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d5b656b-3421-5a09-b55b-b470ebf0175b'
SOURCE_PATH = 'pictographic-primitives/animals/tiger_8d5b656b-3421-5a09-b55b-b470ebf0175b.svg'
AUTHOR = 'gpt-6'


class BearMuzzleFace(Solo48):
    icon_id = 'bear-muzzle-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('bear', 'face', 'head', 'muzzle', 'nose', 'animal', 'cute', 'wildlife')

    def build(self) -> None:
        # Visible keyshape extremes: (0, 0, 48, 48).
        self.add_arc("ear-left", (2,10), (18,10), radius_x=8)
        self.add_arc("forehead", (18,10), (30,10), radius_x=20)
        self.add_arc("ear-right", (30,10), (46,10), radius_x=8)
        self.add_line("cheek-right", (46,10), (46,26))
        self.add_arc("chin-right", (46,26), (24,46), radius_x=22, radius_y=20)
        self.add_arc("chin-left", (24,46), (2,26), radius_x=22, radius_y=20)
        self.add_line("cheek-left", (2,26), (2,10))
        self.add_contour("head", "ear-left", "forehead", "ear-right", "cheek-right", "chin-right", "chin-left", "cheek-left")
        self.add_dot("eye-left", (15,20))
        self.add_dot("eye-right", (33,20))
        self.add_arc("muzzle-bottom", (14,31), (34,31), radius_x=10, radius_y=7, sweep=False)
        self.add_arc("muzzle-top", (34,31), (14,31), radius_x=10, radius_y=7, sweep=False)
        self.add_contour("muzzle", "muzzle-bottom", "muzzle-top", closed=True)
        self.add_dot("nose", (24,31))
