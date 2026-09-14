# Bounds-only review variant; parent preserved.
"""Move every authored point down by 2 units together. Keep dimensions, arcs, shared endpoints and spacing unchanged. VRECT_L centerline box (8,4)-(40,44), ink (6,2)-(42,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a36c6af9-3860-579c-aa1b-a5f68c4f1845'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/steampunk decoration lamp_a36c6af9-3860-579c-aa1b-a5f68c4f1845.svg'
AUTHOR = 'gpt-6'

class PipeMountedLightBulbVariant3(Solo48):
    icon_id = 'pipe-mounted-light-bulb-v3'
    variant_of = 'pipe-mounted-light-bulb'
    variant_label = 'Exact keyshape bounds'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('lamp', 'bulb', 'pipe', 'light', 'filament', 'steampunk', 'fixture')

    def build(self) -> None:
        self.add_arc('dome', (16, 16), (40, 16), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('shoulder-r', (40, 16), (34, 28), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_line('socket-r', (34, 28), (34, 34))
        self.add_line('socket-base', (34, 34), (22, 34))
        self.add_line('socket-l', (22, 34), (22, 28))
        self.add_arc('shoulder-l', (22, 28), (16, 16), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_contour('bulb', 'dome', 'shoulder-r', 'socket-r', 'socket-base', 'socket-l', 'shoulder-l', closed=True)
        self.add_line('filament', (28, 15), (28, 24))
        self.add_line('pipe-top', (28, 34), (28, 37))
        self.add_arc('pipe-bend-r', (28, 37), (23, 42), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('pipe-run', (23, 42), (17, 42))
        self.add_arc('pipe-bend-l', (17, 42), (12, 44), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('pipe-end', (12, 44), (12, 44))
        self.add_contour('pipe', 'pipe-top', 'pipe-bend-r', 'pipe-run', 'pipe-bend-l', 'pipe-end', closed=False)
        self.relate('connect', 'pipe', 'bulb')
        self.add_line('foot', (8, 44), (20, 44))
        self.relate('connect', 'pipe', 'foot')
