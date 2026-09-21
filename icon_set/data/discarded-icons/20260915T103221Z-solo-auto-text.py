"""AUTO Text. Stacks AU above TO to preserve the complete word and readable counters.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide type, inspected earlier: coherent monoline lettering.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46e5998f-10dd-4ed4-a1d2-36de7f900099'
SOURCE_PATH = 'pictographic-primitives/symbol/auto (text)_46e5998f-10dd-4ed4-a1d2-36de7f900099.svg'
AUTHOR = 'gpt-6'


class AutoText(Solo48):
    icon_id = 'auto-text'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('auto', 'automatic', 'mode', 'setting', 'label', 'camera', 'text')

    def build(self) -> None:
        self.add_polyline('a-arch', (6, 20), (6, 14), (6, 6), (20, 6), (20, 14), (20, 20))
        self.add_line('a-bar', (6, 14), (20, 14))
        self.relate("connect", 'a-arch', 'a-bar')
        self.add_line('u-left', (30, 6), (30, 14))
        self.add_arc('u-bottom', (30, 14), (42, 14), radius_x=6, radius_y=6, sweep=False)
        self.add_line('u-right', (42, 14), (42, 6))
        self.add_contour('u', 'u-left', 'u-bottom', 'u-right')
        self.add_polyline('t-top', (6, 30), (13, 30), (20, 30))
        self.add_line('t-stem', (13, 30), (13, 42))
        self.relate("connect", 't-top', 't-stem')
        self.add_arc('o-right', (36, 30), (36, 42), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('o-left', (36, 42), (36, 30), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('o', 'o-right', 'o-left', closed=True)
