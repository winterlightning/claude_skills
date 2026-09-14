"""Bell. Retains the identifying silhouette and visible features.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide bell: dome, flared skirt and curved clapper; supplied source retains a top stem.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '38611f4f-3f62-41bf-9674-e8579ef5b0a0'
SOURCE_PATH = 'pictographic-primitives/symbol/bell_38611f4f-3f62-41bf-9674-e8579ef5b0a0.svg'
AUTHOR = 'gpt-6'

class BellVariant2(Solo48):
    icon_id = 'bell-v2'
    variant_of = 'bell'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/standalone'
    aliases = ()
    keywords = ('bell', 'notification', 'alert', 'alarm', 'ring', 'reminder', 'sound')

    def build(self) -> None:
        self.add_arc('dome-right', (24, 8), (36, 20), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('flare-right', (36, 20), (40, 32), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('lip-right', (40, 32), (38, 34), radius_x=2, radius_y=2, sweep=True)
        self.add_line('lip-1', (38, 34), (30, 34))
        self.add_line('lip-2', (30, 34), (18, 34))
        self.add_line('lip-3', (18, 34), (10, 34))
        self.add_arc('lip-left', (10, 34), (8, 32), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('flare-left', (8, 32), (12, 20), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('dome-left', (12, 20), (24, 8), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('bell-body', 'dome-right', 'flare-right', 'lip-right', 'lip-1', 'lip-2', 'lip-3', 'lip-left', 'flare-left', 'dome-left', closed=True)
        self.add_line('top-stem', (24, 4), (24, 8))
        self.relate('connect', 'bell-body', 'top-stem')
        self.add_arc('clapper', (30, 34), (18, 34), radius_x=6, radius_y=10, sweep=True)
        self.relate('connect', 'bell-body', 'clapper')
