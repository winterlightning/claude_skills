"""Candle in Holder.

Plan: Centered teardrop flame, short candle and wide shallow holder. Reduce doubled holder lines. Lucide flame informed the silhouette. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7549823-5dcb-579f-a225-564c7651dc81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/christmas candle_a7549823-5dcb-579f-a225-564c7651dc81.svg'
AUTHOR = 'gpt-6'

class CandleInHolder(Solo48):
    icon_id = 'candle-in-holder'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('candle', 'in', 'holder')

    def build(self):
        self.add_arc('flame-r',(24,4),(30,14),radius_x=6,radius_y=10)
        self.add_arc('flame-br',(30,14),(24,20),radius_x=6)
        self.add_arc('flame-bl',(24,20),(18,14),radius_x=6)
        self.add_arc('flame-l',(18,14),(24,4),radius_x=6,radius_y=10)
        self.add_contour('flame','flame-r','flame-br','flame-bl','flame-l',closed=True)

        self.add_line('wick',(24,20),(24,28))
        self.add_polyline('candle',(16,36),(16,28),(24,28),(32,28),(32,36))
        self.add_polyline('holder',(8,36),(16,36),(32,36),(40,36),(34,44),(14,44),closed=True)
        for a,b in [('flame','wick'),('wick','candle'),('candle','holder')]:self.relate('connect',a,b)
