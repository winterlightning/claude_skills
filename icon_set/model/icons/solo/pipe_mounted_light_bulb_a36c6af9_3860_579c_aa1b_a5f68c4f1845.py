"""Exposed light bulb on a bent pipe and flat foot. VRECT_L (8,2)-(40,46). Lucide lightbulb informs broad rounded glass with a narrow socket. Filament loop reduced to a single upright mark; bent support preserves asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a36c6af9-3860-579c-aa1b-a5f68c4f1845'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/steampunk decoration lamp_a36c6af9-3860-579c-aa1b-a5f68c4f1845.svg'
AUTHOR = 'gpt-6'


class PipeMountedLightBulb(Solo48):
    icon_id = 'pipe-mounted-light-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('lamp', 'bulb', 'pipe', 'light', 'filament', 'steampunk', 'fixture')

    def build(self) -> None:
        self.add_arc('dome', (16, 14), (40, 14), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('shoulder-r', (40, 14), (34, 26), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_line('socket-r', (34, 26), (34, 32))
        self.add_line('socket-base', (34, 32), (22, 32))
        self.add_line('socket-l', (22, 32), (22, 26))
        self.add_arc('shoulder-l', (22, 26), (16, 14), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_contour('bulb', 'dome', 'shoulder-r', 'socket-r', 'socket-base', 'socket-l', 'shoulder-l', closed=True)
        self.add_line('filament', (28, 13), (28, 22))
        self.add_line('pipe-top', (28, 32), (28, 35))
        self.add_arc('pipe-bend-r', (28, 35), (23, 40), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('pipe-run', (23, 40), (17, 40))
        self.add_arc('pipe-bend-l', (17, 40), (12, 45), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('pipe-end', (12, 45), (12, 46))
        self.add_contour('pipe', 'pipe-top', 'pipe-bend-r', 'pipe-run', 'pipe-bend-l', 'pipe-end', closed=False)
        self.relate('connect', 'pipe', 'bulb')
        self.add_line('foot', (8, 46), (20, 46))
        self.relate('connect', 'pipe', 'foot')
