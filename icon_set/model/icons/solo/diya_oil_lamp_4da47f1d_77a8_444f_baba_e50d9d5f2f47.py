"""Diya Oil Lamp.

Plan: Pointed flame over a broad oil bowl with central rim notch. Remove the nested flame. Lucide flame informs teardrop construction. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4da47f1d-77a8-444f-baba-e50d9d5f2f47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/diwali_4da47f1d-77a8-444f-baba-e50d9d5f2f47.svg'
AUTHOR = 'gpt-6'

class DiyaOilLamp(Solo48):
    icon_id = 'diya-oil-lamp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('diya', 'oil', 'lamp')

    def build(self):
        self.add_arc('flame-r',(24,6),(30,16),radius_x=6,radius_y=10)
        self.add_arc('flame-br',(30,16),(24,22),radius_x=6)
        self.add_arc('flame-bl',(24,22),(18,16),radius_x=6)
        self.add_arc('flame-l',(18,16),(24,6),radius_x=6,radius_y=10)
        self.add_contour('flame','flame-r','flame-br','flame-bl','flame-l',closed=True)
        self.add_line('wick',(24,22),(24,34))
        self.add_polyline('rim',(6,30),(12,30),(24,34),(36,30),(42,30))
        self.add_arc('bowl',(42,30),(6,30),radius_x=18,radius_y=12)
        self.add_contour('lamp','rim-1','rim-2','rim-3','rim-4','bowl',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='rim']
        self.relate('connect','wick','flame');self.relate('connect','wick','lamp')
