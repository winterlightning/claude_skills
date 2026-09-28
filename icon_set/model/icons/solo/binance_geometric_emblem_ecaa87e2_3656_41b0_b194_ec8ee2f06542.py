"""Binance Cryptocurrency Logo.
Plan: Mirrored opposing chevrons and two small side diamonds around an open center. Circular ink envelope radius22 about (24,24).
Reference: Supplied original; no useful exact local Lucide match. Shared axes and simple geometric construction.
Reduction: Outlined chevron bands reduced to strokes; side diamonds retain open interiors.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ecaa87e2-3656-41b0-b194-ec8ee2f06542'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/virtual coin crypto binance_ecaa87e2-3656-41b0-b194-ec8ee2f06542.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'binance-geometric-emblem'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance"
    categories = ("primitives", "finance")
    aliases = ()
    keywords = ('binance', 'cryptocurrency', 'logo')

    def build(self):

        self.add_polyline('upper',(16,12),(24,4),(32,12))
        self.add_polyline('lower',(16,36),(24,44),(32,36))
        for n,x in (('left',10),('right',38)):
            self.add_polyline(n,(x-6,24),(x,18),(x+6,24),(x,30),(x-6,24))
