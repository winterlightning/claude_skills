"""A left-facing fish sits beside a J-shaped fishing hook. HRECT_L centerline extremes (6,8)-(42,40) fit the scene. Lucide fish-symbol informs the open tail and pointed lens body. Omit the line break and intermediate tiny dot; retain the fish eye and hook. Deliberate asymmetry preserves the fish direction and the physical scene."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'baa1fd0f-249e-41b9-9925-8471559e72c2'
SOURCE_PATH = 'pictographic-primitives/symbol/fish with a line_baa1fd0f-249e-41b9-9925-8471559e72c2.svg'
AUTHOR = 'gpt-6'


class FishAndHook(Solo48):
    icon_id = 'fish-and-hook'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('fishing', 'fish', 'hook', 'angling', 'sea', 'catch', 'hobby', 'line')

    def build(self) -> None:
        self.add_line('line', (6,8), (6,36))
        self.add_arc('hook', (6,36), (12,36), radius_x=4, sweep=False)
        self.add_contour('fishing-line', 'line', 'hook')
        self.add_arc('fish-back', (18,28), (42,28), radius_x=15, radius_y=25)
        self.add_arc('fish-belly', (42,28), (18,28), radius_x=15, radius_y=25)
        self.add_contour('fish', 'fish-back', 'fish-belly', closed=True)
        self.add_polyline('tail', (42,18), (42,28), (42,38))
        self.relate('connect', 'fish', 'tail')
        self.add_dot('eye', (30,28))
