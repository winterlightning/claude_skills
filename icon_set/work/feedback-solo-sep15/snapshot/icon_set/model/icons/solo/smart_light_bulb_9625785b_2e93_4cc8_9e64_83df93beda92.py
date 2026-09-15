"""Smart Light Bulb. Retains the identifying silhouette and visible features.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide lightbulb: round glass with narrowed lower neck; source determines the two wireless arcs and rounded base.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9625785b-2e93-4cc8-9e64-83df93beda92'
SOURCE_PATH = 'pictographic-primitives/symbol/electric waves bulb_9625785b-2e93-4cc8-9e64-83df93beda92.svg'
AUTHOR = 'gpt-6'


class SmartLightBulb(Solo48):
    icon_id = 'smart-light-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('smart-bulb', 'light', 'bulb', 'wireless', 'iot', 'smart-home', 'lamp', 'connected')

    def build(self) -> None:
        self.add_arc('glass-top', (8, 20), (40, 20), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('glass-right', (40, 20), (30, 34), radius_x=10, radius_y=14, sweep=True)
        self.add_line('neck-right', (30, 34), (30, 38))
        self.add_arc('base', (30, 38), (18, 38), radius_x=6, radius_y=6, sweep=True)
        self.add_line('neck-left', (18, 38), (18, 34))
        self.add_arc('glass-left', (18, 34), (8, 20), radius_x=10, radius_y=14, sweep=True)
        self.add_contour('bulb', 'glass-top', 'glass-right', 'neck-right', 'base', 'neck-left', 'glass-left', closed=True)
        self.add_line('base-top', (18, 34), (30, 34))
        self.relate("connect", 'bulb', 'base-top')
        self.add_arc('signal-outer', (18, 16), (30, 16), radius_x=6, radius_y=3, sweep=True)
        self.add_arc('signal-inner', (20, 25), (28, 25), radius_x=4, radius_y=1, sweep=True)
