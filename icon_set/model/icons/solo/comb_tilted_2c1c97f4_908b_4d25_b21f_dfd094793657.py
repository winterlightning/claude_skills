"""Comb. Retains three parallel teeth and the tilted spine with end feet.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c1c97f4-908b-4d25-b21f-dfd094793657'
SOURCE_PATH = 'pictographic-primitives/symbol/comb_2c1c97f4-908b-4d25-b21f-dfd094793657.svg'
AUTHOR = 'gpt-6'


class CombTilted(Solo48):
    icon_id = 'comb-tilted'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('comb', 'hair', 'grooming', 'barber', 'beauty', 'brush', 'salon', 'care')

    def build(self) -> None:
        self.add_polyline('spine', (20, 4), (40, 12), (37, 20), (34, 28), (31, 36), (28, 44), (8, 36))
        self.add_line('tooth-one', (37, 20), (21, 14))
        self.relate("connect", 'spine', 'tooth-one')
        self.add_line('tooth-two', (34, 28), (18, 22))
        self.relate("connect", 'spine', 'tooth-two')
        self.add_line('tooth-three', (31, 36), (15, 30))
        self.relate("connect", 'spine', 'tooth-three')
