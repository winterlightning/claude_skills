"""Face-on triceratops with mirrored inward horns and broad snout. Centerlines (2,2)-(46,46). Circular frill and snout with mirrored dot eyes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34e9ab02-0d15-4c63-8afd-4744cb5da9cf'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur triceratop head_34e9ab02-0d15-4c63-8afd-4744cb5da9cf.svg'
AUTHOR = 'gpt-6'


class TriceratopsHead(Solo48):
    icon_id = 'triceratops-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('triceratops', 'dinosaur', 'head', 'horns', 'frill', 'prehistoric', 'reptile', 'jurassic')

    def build(self) -> None:
        # Mirrored closed face: horn tips and cheeks share exact endpoints.
        self.add_arc('crown-left', (16,15), (24,5), radius_x=8, radius_y=10)
        self.add_arc('crown-right', (24,5), (32,15), radius_x=8, radius_y=10)
        self.add_arc('right-horn-tip', (32,15), (40,19), radius_x=5, sweep=False)
        self.add_arc('right-frill', (40,19), (46,33), radius_x=6, radius_y=14)
        self.add_arc('right-cheek', (46,33), (42,37), radius_x=4)
        self.add_line('right-jowl', (42,37), (36,37))
        self.add_arc('snout-right', (36,37), (24,46), radius_x=12, radius_y=9)
        self.add_arc('snout-left', (24,46), (12,37), radius_x=12, radius_y=9)
        self.add_line('left-jowl', (12,37), (6,37))
        self.add_arc('left-cheek', (6,37), (2,33), radius_x=4)
        self.add_arc('left-frill', (2,33), (8,19), radius_x=6, radius_y=14)
        self.add_arc('left-horn-tip', (8,19), (16,15), radius_x=5, sweep=False)
        self.add_contour('face', 'crown-left', 'crown-right', 'right-horn-tip',
                         'right-frill', 'right-cheek', 'right-jowl', 'snout-right',
                         'snout-left', 'left-jowl', 'left-cheek', 'left-frill',
                         'left-horn-tip', closed=True)
        self.add_line('left-horn-inner', (16,15), (3,2))
        self.add_arc('left-horn-outer', (3,2), (8,19), radius_x=24, sweep=False)
        self.add_contour('left-horn', 'left-horn-inner', 'left-horn-outer')
        self.add_arc('right-horn-outer', (40,19), (45,2), radius_x=24, sweep=False)
        self.add_line('right-horn-inner', (45,2), (32,15))
        self.add_contour('right-horn', 'right-horn-outer', 'right-horn-inner')
        self.relate('connect', 'face', 'left-horn')
        self.relate('connect', 'face', 'right-horn')
        self.add_dot('eye-left', (16,27))
        self.add_dot('eye-right', (32,27))
