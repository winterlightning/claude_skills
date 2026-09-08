"""Open-jawed tyrannosaurus head facing left. Centerlines (2,5)-(46,43). Lucide bird informs rounded skull; one broad tooth replaces the small tooth row."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8371995-6344-4666-a182-7a41835781ce'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur trex head_e8371995-6344-4666-a182-7a41835781ce.svg'
AUTHOR = 'gpt-6'


class TrexHead(Solo48):
    icon_id = 'trex-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('trex', 'tyrannosaurus', 'dinosaur', 'head', 'jaws', 'teeth', 'prehistoric', 'roar')

    def build(self) -> None:
        self.add_line('snout-rise', (2,23), (2,16))
        self.add_arc('snout-round', (2,16), (10,8), radius_x=8)
        self.add_line('brow', (10,8), (22,8))
        self.add_arc('skull', (22,8), (31,5), radius_x=15, sweep=True)
        self.add_arc('cranium', (31,5), (46,20), radius_x=15)
        self.add_line('back', (46,20), (46,43))
        self.add_contour('outer', 'snout-rise', 'snout-round', 'brow','skull','cranium','back')
        self.add_polyline('upper-jaw', (2,23), (10,23), (10,28), (16,23), (24,23))
        self.add_arc('mouth', (24,23), (15,34), radius_x=12)
        self.add_line('lower-lip', (15,34), (9,34))
        self.add_arc('chin', (9,34), (9,43), radius_x=5, radius_y=5, sweep=False)
        self.add_line('jaw-bottom', (9,43), (30,43))
        self.add_arc('jaw-hinge', (30,43), (38,35), radius_x=8,sweep=False)
        self.add_contour('lower-jaw', 'mouth','lower-lip','chin','jaw-bottom','jaw-hinge')
        self.relate('connect','outer','upper-jaw')
        self.relate('connect','upper-jaw','lower-jaw')
        self.add_dot('eye', (30,16))
