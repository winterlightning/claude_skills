"""Open-jawed tyrannosaurus head facing left. Centerlines (6,6)-(42,42). Lucide bird informs rounded skull; one broad tooth replaces the small tooth row."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8371995-6344-4666-a182-7a41835781ce'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur trex head_e8371995-6344-4666-a182-7a41835781ce.svg'
AUTHOR = 'gpt-6'


class TrexHead(Solo48):
    icon_id = 'trex-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('trex', 'tyrannosaurus', 'dinosaur', 'head', 'jaws', 'teeth', 'prehistoric', 'roar')

    def build(self) -> None:
        self.add_line('snout-rise', (6,23), (6,16))
        self.add_bezier('snout-round', (6, 16), *(((6, 12.7674284), (7.16125546, 9.60262661), (10, 8)),))
        self.add_line('brow', (10,8), (22,8))
        self.add_bezier('skull', (22, 8), *(((24.71565121, 6.40504862), (27.86443068, 6), (31, 6)),))
        self.add_arc('cranium', (31,6), (42,20), radius_x=15)
        self.add_line('back', (42,20), (42,42))
        self.add_contour('outer', 'snout-rise', 'snout-round', 'brow','skull','cranium','back')
        self.add_polyline('upper-jaw', (6,23), (10,23), (10,28), (16,23), (24,23))
        self.add_arc('mouth', (24,23), (15,34), radius_x=12)
        self.add_line('lower-lip', (15,34), (9,34))
        self.add_arc('chin', (9,34), (9,42), radius_x=5, radius_y=5, sweep=False)
        self.add_line('jaw-bottom', (9,42), (30,42))
        self.add_bezier('jaw-hinge',(30,42),((33,42),(33,39),(33,35)))
        self.add_contour('lower-jaw', 'mouth','lower-lip','chin','jaw-bottom','jaw-hinge')
        self.relate('connect','outer','upper-jaw')
        self.relate('connect','upper-jaw','lower-jaw')
        self.add_dot('eye', (30,16))
