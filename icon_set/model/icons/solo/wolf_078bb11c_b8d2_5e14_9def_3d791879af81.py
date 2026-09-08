"""Wolf head in profile with pointed ear and long muzzle; open neck follows the reference. Lucide dog informs rounded cheek transitions."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '078bb11c-b8d2-5e14-9def-3d791879af81'
SOURCE_PATH = 'pictographic-primitives/animals/wolf_078bb11c-b8d2-5e14-9def-3d791879af81.svg'
AUTHOR = 'gpt-6'


class WolfHeadProfile(Solo48):
    icon_id = 'wolf-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('wolf', 'head', 'profile', 'ears', 'snout', 'canine', 'dog', 'wild')

    def build(self) -> None:
        self.add_arc('nape', (2, 34), (17, 16), radius_x=42, radius_y=42, sweep=True)
        self.add_arc('ear-back', (17, 16), (26, 2), radius_x=15, radius_y=15, sweep=True)
        self.add_line('ear-1', (26, 2), (25, 12))
        self.add_arc('brow', (25, 12), (35, 20), radius_x=11, radius_y=11, sweep=True)
        self.add_line('muzzle', (35, 20), (46, 25))
        self.add_arc('nose', (46, 25), (39, 33), radius_x=7, radius_y=8, sweep=True)
        self.add_line('jaw', (39, 33), (30, 32))
        self.add_arc('throat', (30, 32), (24, 38), radius_x=6, radius_y=6, sweep=False)
        self.add_line('chest', (24, 38), (24, 46))
        self.add_contour('outline', 'nape', 'ear-back', 'ear-1', 'brow', 'muzzle', 'nose', 'jaw', 'throat', 'chest', closed=False)
