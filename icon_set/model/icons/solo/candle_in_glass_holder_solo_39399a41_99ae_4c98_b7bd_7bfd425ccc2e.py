"""Candle in glass holder.

Construction reference: flame.
Open glass rim keeps the flame readable; candle joins the glass base.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '39399a41-99ae-4c98-b7bd-7bfd425ccc2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/bottle candle_39399a41-99ae-4c98-b7bd-7bfd425ccc2e.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'candle-in-glass-holder-solo-39399a41'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('combination', 'other', 'primitives-generate')
    aliases = ('candle-in-glass-holder',)
    keywords = ('candle', 'in', 'glass', 'holder')

    def build(self):
        # A flared, open glass surrounds the candle; no seam through the flame.
        path(self,'glass',(8,4),[('L',(11,14)),('L',(8,32)),('A',(20,44),12,12,False),('L',(28,44)),('A',(40,32),12,12,False),('L',(37,14)),('L',(40,4))])
        path(self,'flame',(24,5),[('A',(28,14),10,10,True),('A',(20,14),4,4,True),('A',(24,5),10,10,True)],True)
        self.add_polyline('candle',(20,44),(20,28),(28,28),(28,44))
        self.relate('connect','glass','candle')
