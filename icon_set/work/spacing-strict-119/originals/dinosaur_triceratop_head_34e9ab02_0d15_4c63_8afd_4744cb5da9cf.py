"""Face-on triceratops with mirrored inward horns and broad snout. Centerlines (6,6)-(42,42). Circular frill and snout with mirrored dot eyes."""
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
        self.add_bezier('crown-left', (16, 15), *(((16.41233585, 9.87098707), (19.87617545, 6), (24, 6)),))
        self.add_bezier('crown-right', (24, 6), *(((28.12382455, 6), (31.58766415, 9.87098707), (32, 15)),))
        self.add_arc('right-horn-tip', (32,15), (40,19), radius_x=5, sweep=False)
        self.add_bezier('right-frill', (40, 19), *(((41.75220913, 22.40144024), (42, 27.82575502), (42, 33)),))
        self.add_bezier('right-cheek', (42, 33), *(((42, 34.23760431), (42, 35.76239569), (42, 37)),))
        self.add_line('right-jowl', (42,37), (36,37))
        self.add_bezier('snout-right', (36, 37), *(((33.79152696, 40.38747008), (29.00161226, 42), (24, 42)),))
        self.add_bezier('snout-left', (24, 42), *(((18.99838774, 42), (14.20847304, 40.38747008), (12, 37)),))
        self.add_line('left-jowl', (12,37), (6,37))
        self.add_bezier('left-cheek', (6, 37), *(((6, 35.76239569), (6, 34.23760431), (6, 33)),))
        self.add_bezier('left-frill', (6, 33), *(((6, 27.82575502), (6.24779087, 22.40144024), (8, 19)),))
        self.add_arc('left-horn-tip', (8,19), (16,15), radius_x=5, sweep=False)
        self.add_contour('face', 'crown-left', 'crown-right', 'right-horn-tip',
                         'right-frill', 'right-cheek', 'right-jowl', 'snout-right',
                         'snout-left', 'left-jowl', 'left-cheek', 'left-frill',
                         'left-horn-tip', closed=True)
        self.add_line('left-horn-inner', (16,15), (6,6))
        self.add_bezier('left-horn-outer', (6, 6), *(((6, 10.4350282), (6.13575397, 14.93746009), (8, 19)),))
        self.add_contour('left-horn', 'left-horn-inner', 'left-horn-outer')
        self.add_bezier('right-horn-outer', (40, 19), *(((41.86424603, 14.93746009), (42, 10.4350282), (42, 6)),))
        self.add_line('right-horn-inner', (42,6), (32,15))
        self.add_contour('right-horn', 'right-horn-outer', 'right-horn-inner')
        self.relate('connect', 'face', 'left-horn')
        self.relate('connect', 'face', 'right-horn')
        self.add_dot('eye-left',(17,28))
        self.add_dot('eye-right',(31,28))
