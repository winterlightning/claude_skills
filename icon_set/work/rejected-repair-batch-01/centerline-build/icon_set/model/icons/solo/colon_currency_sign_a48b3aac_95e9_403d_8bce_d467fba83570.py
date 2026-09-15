"""Colón Sign. Preserves the source single diagonal slash through the open C.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a48b3aac-95e9-403d-8bce-d467fba83570'
SOURCE_PATH = 'pictographic-primitives/symbol/colon sign_a48b3aac-95e9-403d-8bce-d467fba83570.svg'
AUTHOR = 'gpt-6'


class ColonCurrencySign(Solo48):
    icon_id = 'colon-currency-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('colon', 'currency', 'money', 'costa-rica', 'sign', 'finance', 'symbol', 'crc')

    def build(self) -> None:
        self.add_line('top', (40, 4), (28, 4))
        self.add_arc('upper', (28, 4), (8, 24), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('lower-a', (8, 24), (12, 36), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('lower-b', (12, 36), (28, 44), radius_x=20, radius_y=20, sweep=False)
        self.add_line('bottom', (28, 44), (40, 44))
        self.add_contour('c', 'top', 'upper', 'lower-a', 'lower-b', 'bottom')
        self.add_polyline('slash', (8, 40), (12, 36), (40, 8))
        self.relate("connect", 'c', 'slash')
