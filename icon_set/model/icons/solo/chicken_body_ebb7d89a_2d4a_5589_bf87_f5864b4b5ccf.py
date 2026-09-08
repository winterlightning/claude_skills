"""Crested bird with a continuous scooped back, rounded belly and integrated beak. Lucide bird informs circular head and coherent contour; crest remains directional."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebb7d89a-2d4a-5589-bf87-f5864b4b5ccf'
SOURCE_PATH = 'pictographic-primitives/animals/chicken body_ebb7d89a-2d4a-5589-bf87-f5864b4b5ccf.svg'
AUTHOR = 'gpt-6'


class CrestedBird(Solo48):
    icon_id = 'crested-bird'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('chicken', 'hen', 'bird', 'crest', 'beak', 'perch', 'farm', 'poultry')

    def build(self) -> None:
        # SQUARE visible (0,0)-(48,48); centerlines (2,2)-(46,46).
        self.add_line('tail', (2,22), (8,22))
        self.add_arc('tail-turn', (8,22), (12,26), radius_x=4)
        self.add_line('tail-root', (12,26), (12,28))
        self.add_contour('tail-shape', 'tail', 'tail-turn', 'tail-root')
        self.add_arc('belly-left', (12,28), (26,40), radius_x=14, radius_y=12, sweep=False)
        self.add_arc('belly-right', (26,40), (40,28), radius_x=14, radius_y=12, sweep=False)
        self.add_line('breast', (40,28), (40,23))
        self.add_line('bill-bottom', (40,23), (46,23))
        self.add_line('bill-top', (46,23), (40,17))
        self.add_arc('head-right', (40,17), (31,8), radius_x=9, sweep=False)
        self.add_arc('head-left', (31,8), (22,17), radius_x=9, sweep=False)
        self.add_line('back', (22,17), (22,22))
        self.add_arc('back-turn', (22,22), (16,28), radius_x=6)
        self.add_line('back-bottom', (16,28), (12,28))
        self.add_contour('body', 'belly-left', 'belly-right', 'breast', 'bill-bottom', 'bill-top', 'head-right', 'head-left', 'back', 'back-turn', 'back-bottom', closed=True)
        self.relate('connect', 'tail-shape', 'body')
        self.add_arc('crest', (31,8), (25,2), radius_x=6, sweep=False)
        self.relate('connect', 'crest', 'body')
        self.add_line('leg', (26,40), (26,46))
        self.relate('connect', 'leg', 'body')
