from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac736fb4-930d-5099-ae75-efdc2b2a7f88'
SOURCE_PATH = 'pictographic-primitives/animals/snail shell_ac736fb4-930d-5099-ae75-efdc2b2a7f88.svg'
AUTHOR = 'gpt-6'


class SnailShellSpiral(Solo48):
    icon_id = 'snail-shell-spiral'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('snail', 'shell', 'spiral', 'swirl', 'coil', 'whorl', 'mollusc', 'curl')

    def build(self) -> None:
        # Open spiral with tangent semicircles; extremes (2,2)-(46,46).
        self.add_arc('outer-upper', (2, 28), (46, 28), radius_x=22, radius_y=26, sweep=True)
        self.add_arc('outer-lower', (46, 28), (10, 28), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('middle-upper', (10, 28), (34, 28), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('inner-lower', (34, 28), (22, 28), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('spiral', 'outer-upper', 'outer-lower', 'middle-upper', 'inner-lower', closed=False)
