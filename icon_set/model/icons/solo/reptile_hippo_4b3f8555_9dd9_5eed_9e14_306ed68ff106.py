"""Left-facing crocodile with open wedge jaws and scalloped body. Extrema (2,8)-(46,40). Tiny teeth omitted to keep the open jaw readable; profile asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b3f8555-9dd9-5eed-9e14-306ed68ff106'
SOURCE_PATH = 'pictographic-primitives/animals/reptile hippo_4b3f8555-9dd9-5eed-9e14-306ed68ff106.svg'
AUTHOR = 'gpt-6'


class OpenMouthCrocodile(Solo48):
    icon_id = 'open-mouth-crocodile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/reptiles'
    aliases = ()
    keywords = ('crocodile', 'alligator', 'mouth', 'jaws', 'open', 'reptile', 'teeth', 'bite')

    def build(self) -> None:
        # Left-facing crocodile with open wedge jaws and scalloped body. Extrema (2,8)-(46,40). Tiny teeth omitted to keep the open jaw readable; profile asymmetry retained.
        self.add_arc('skull', (4, 16), (12, 8), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('brow', (12, 8), (22, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('ridge', (22, 18), (32, 18), radius_x=5, radius_y=4, sweep=True)
        self.add_arc('back', (32, 18), (46, 32), radius_x=14, radius_y=14, sweep=True)
        self.add_line('tail', (46, 32), (46, 40))
        self.add_arc('belly-right', (46, 40), (32, 35), radius_x=14, radius_y=5, sweep=True)
        self.add_arc('belly-left', (32, 35), (18, 35), radius_x=9, radius_y=8, sweep=True)
        self.add_arc('jaw-lower', (18, 35), (2, 36), radius_x=12, radius_y=10, sweep=True)
        self.add_line('mouth-lower', (2, 36), (15, 29))
        self.add_arc('mouth-hinge', (15, 29), (15, 23), radius_x=4, radius_y=4, sweep=False)
        self.add_line('mouth-upper', (15, 23), (4, 16))
        self.add_contour('outline', 'skull', 'brow', 'ridge', 'back', 'tail', 'belly-right', 'belly-left', 'jaw-lower', 'mouth-lower', 'mouth-hinge', 'mouth-upper')
        self.add_dot('eye', (26, 25))
