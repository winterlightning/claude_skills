"""A left-facing fish sits beside a J-shaped fishing hook. HRECT_L centerline extremes (4,8)-(44,40) fit the scene. Lucide fish-symbol informs the open tail and pointed lens body. Omit the line break and intermediate tiny dot; retain the fish eye and hook. Deliberate asymmetry preserves the fish direction and the physical scene."""
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
    category = "symbol"
    aliases = ()
    keywords = ('fishing', 'fish', 'hook', 'angling', 'sea', 'catch', 'hobby', 'line')

    def build(self) -> None:
        self.add_line('line', (4,8), (4,36))
        self.add_arc('hook', (4,36), (12,36), radius_x=4, sweep=False)
        self.add_contour('fishing-line', 'line', 'hook')
        self.add_arc('fish-back', (20,28), (44,28), radius_x=15, radius_y=25)
        self.add_arc('fish-belly', (44,28), (20,28), radius_x=15, radius_y=25)
        self.add_contour('fish', 'fish-back', 'fish-belly', closed=True)
        self.add_polyline('tail', (44,18), (44,28), (44,40))
        self.relate('connect', 'fish', 'tail')
        self.add_dot('eye', (32,28))
