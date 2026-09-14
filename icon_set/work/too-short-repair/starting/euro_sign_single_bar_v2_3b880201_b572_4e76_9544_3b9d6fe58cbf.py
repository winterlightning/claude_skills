# Variant of euro-sign-single-bar; parent file remains unchanged.
"""Euro Sign. Preserves exactly one horizontal bar, as shown in the supplied source.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b880201-b572-4e76-9544-3b9d6fe58cbf'
SOURCE_PATH = 'pictographic-primitives/symbol/cent_3b880201-b572-4e76-9544-3b9d6fe58cbf.svg'
AUTHOR = 'gpt-6'

class EuroSignSingleBarVariant2(Solo48):
    icon_id = 'euro-sign-single-bar-v2'
    variant_of = 'euro-sign-single-bar'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/standalone'
    aliases = ()
    keywords = ('euro', 'currency', 'money', 'sign', 'eur', 'finance', 'symbol', 'cent')

    def build(self) -> None:
        self.add_line('c-top', (40, 6), (32, 6))
        self.add_arc('c-upper', (32, 6), (16, 24), radius_x=16, radius_y=20, sweep=False)
        self.add_arc('c-lower', (16, 24), (32, 42), radius_x=16, radius_y=20, sweep=False)
        self.add_line('c-bottom', (32, 42), (40, 42))
        self.add_contour('c', 'c-top', 'c-upper', 'c-lower', 'c-bottom')
        self.add_polyline('bar', (8, 24), (16, 24), (30, 24))
        self.relate('connect', 'c', 'bar')
