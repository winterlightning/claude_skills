"""Right-facing perched bird; extremes (8,2)-(40,46). Lucide bird informs head arc, hanging wing and attached straight legs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '222f755f-6e1c-48fe-a3c3-327c5cc80423'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird eagle_222f755f-6e1c-48fe-a3c3-327c5cc80423.svg'
AUTHOR = 'gpt-6'


class PerchedBird(Solo48):
    icon_id = 'perched-bird'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('bird', 'perched', 'standing', 'beak', 'wing', 'legs', 'wildlife', 'simple')

    def build(self) -> None:
        self.add_arc('crown', (18, 12), (28, 2), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('forehead', (28, 2), (38, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_line('beak-upper', (38, 12), (40, 18))
        self.add_line('beak-lower', (40, 18), (32, 16))
        self.add_arc('breast', (32, 16), (32, 34), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('belly', (32, 34), (24, 38), radius_x=8, radius_y=6, sweep=True)
        self.add_arc('belly-left', (24, 38), (18, 36), radius_x=12, radius_y=8, sweep=True)
        self.add_line('back', (18, 36), (18, 19))
        self.add_line('back-top', (18, 19), (18, 12))
        self.add_contour('body', 'crown', 'forehead', 'beak-upper', 'beak-lower', 'breast', 'belly', 'belly-left', 'back', 'back-top', closed=True)
        self.add_arc('wing-top', (18, 19), (8, 29), radius_x=10, radius_y=10, sweep=False)
        self.add_line('wing-edge', (8, 29), (8, 38))
        self.add_arc('wing-tip', (8, 38), (18, 19), radius_x=10, radius_y=22, sweep=False)
        self.add_contour('wing', 'wing-top', 'wing-edge', 'wing-tip', closed=True)
        self.relate("connect", 'wing', 'body')
        self.add_line('left-leg', (24, 38), (24, 46))
        self.add_line('right-leg', (32, 34), (32, 46))
        self.relate("connect", 'left-leg', 'body')
        self.relate("connect", 'right-leg', 'body')
