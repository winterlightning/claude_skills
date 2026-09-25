"""Pound sterling with a curved crown, crossbar and hooked foot. Lucide pound-sterling informs the minimal open construction.

SOLO48 VRECT_L; geometry authored from its exact centerline extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '239fd06e-dd89-43b8-9208-df64a89cf9c1'
SOURCE_PATH = 'pictographic-primitives/symbol/pound_239fd06e-dd89-43b8-9208-df64a89cf9c1.svg'
AUTHOR = 'gpt-6'

class PoundSign(Solo48):
    icon_id = 'pound-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pound', 'sterling', 'gbp', 'currency', 'money', 'uk', 'finance', 'sign')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('crown', (40, 16), (16, 16), radius_x=12, sweep=False)
        self.add_line('stem-upper', (16, 16), (16, 26))
        self.add_line('stem-lower', (16, 26), (16, 34))
        self.add_arc('foot', (16, 34), (8, 44), radius_x=13)
        self.add_contour('stem', 'crown', 'stem-upper', 'stem-lower', 'foot')
        self.add_polyline('bar', (8, 26), (16, 26), (30, 26))
        self.add_line('base', (8, 44), (40, 44))
        self.relate('connect', 'bar', 'stem')
        self.relate('connect', 'base', 'stem')
