"""Candle with Leaves.

Plan: Centered candle and small flame above two pointed curved leaves. Shared mirror axis and genuine leaf-to-candle nodes. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23a0ec04-eeff-5a25-ae7b-7217f7994eb7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/advent_23a0ec04-eeff-5a25-ae7b-7217f7994eb7.svg'
AUTHOR = 'gpt-6'

class CandleWithLeaves(Solo48):
    icon_id = 'candle-with-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('candle', 'with', 'leaves')

    def build(self):
        self.add_arc('flame-r',(24,4),(28,12),radius_x=4,radius_y=8)
        self.add_arc('flame-br',(28,12),(24,16),radius_x=4)
        self.add_arc('flame-bl',(24,16),(20,12),radius_x=4)
        self.add_arc('flame-l',(20,12),(24,4),radius_x=4,radius_y=8)
        self.add_contour('flame','flame-r','flame-br','flame-bl','flame-l',closed=True)
        self.add_line('wick',(24,16),(24,24))
        self.add_polyline('candle',(18,34),(18,24),(24,24),(30,24),(30,34))
        self.add_polyline('leaf-left-top',(8,28),(18,34),(24,44))
        self.add_arc('leaf-left-bottom',(24,44),(8,28),radius_x=16)
        self.add_contour('leaf-left','leaf-left-top-1','leaf-left-top-2','leaf-left-bottom',closed=True)
        self.add_polyline('leaf-right-top',(24,44),(30,34),(40,28))
        self.add_arc('leaf-right-bottom',(40,28),(24,44),radius_x=16)
        self.add_contour('leaf-right','leaf-right-top-1','leaf-right-top-2','leaf-right-bottom',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['leaf-left-top','leaf-right-top']]
        for a,b in [('flame','wick'),('wick','candle'),('candle','leaf-left'),('candle','leaf-right'),('leaf-left','leaf-right')]:self.relate('connect',a,b)
