"""Carving a Wooden Bowl.

Plan: Rounded grip and angled shaft carve a wide bowl; a large curved shaving rises from rim. Reduce foot and tight inner shaving turn. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f746fcda-f75b-56bc-8b21-d20b11cd104f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/wood carving bowl_f746fcda-f75b-56bc-8b21-d20b11cd104f.svg'
AUTHOR = 'gpt-6'


class CarvingAWoodenBowl(Solo48):
    icon_id = 'carving-a-wooden-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hobbies'
    aliases = ()
    keywords = ('carving', 'a', 'wooden', 'bowl')

    def build(self):
        self.add_arc('handle-top',(6,11),(16,11),radius_x=5)
        self.add_line('handle-r',(16,11),(16,16))
        self.add_arc('handle-br',(16,16),(11,21),radius_x=5)
        self.add_arc('handle-bl',(11,21),(6,16),radius_x=5)
        self.add_line('handle-l',(6,16),(6,11))
        self.add_contour('handle','handle-top','handle-r','handle-br','handle-bl','handle-l',closed=True)
        self.add_line('shaft',(11,21),(24,30))
        self.add_polyline('rim',(6,30),(24,30),(34,30),(42,30))
        self.add_arc('bowl-bottom',(42,30),(6,30),radius_x=18,radius_y=12)
        self.add_contour('bowl','rim-1','rim-2','rim-3','bowl-bottom',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='rim']
        self.add_arc('shaving',(34,30),(34,14),radius_x=8,sweep=False)
        self.relate('connect','handle','shaft')
        self.relate('connect','shaft','bowl')
        self.relate('connect','shaving','bowl')
