"""Tooth with Trailing Floss.

Plan: Tall molar with a single strand leaving upper-right edge and curling below. Simplified rounded roots; floss is physical attached thread. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '638d5134-5ea9-476e-996b-afb066e33fd9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/tooth_638d5134-5ea9-476e-996b-afb066e33fd9.svg'
AUTHOR = 'gpt-6'


class ToothWithTrailingFloss(Solo48):
    icon_id = 'tooth-with-trailing-floss'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('tooth', 'with', 'trailing', 'floss')

    def build(self):
        self.add_arc('crown-l',(6,14),(14,6),radius_x=8)
        self.add_arc('crown-top',(14,6),(22,6),radius_x=4,radius_y=2,sweep=False)
        self.add_arc('crown-r',(22,6),(30,14),radius_x=8)
        self.add_line('right',(30,14),(30,38))
        self.add_arc('root-r',(30,38),(22,38),radius_x=4)
        self.add_arc('cleft-r',(22,38),(18,30),radius_x=4,radius_y=8,sweep=False)
        self.add_arc('cleft-l',(18,30),(14,38),radius_x=4,radius_y=8,sweep=False)
        self.add_arc('root-l',(14,38),(6,38),radius_x=4)
        self.add_line('left',(6,38),(6,14))
        self.add_contour('tooth','crown-l','crown-top','crown-r','right','root-r','cleft-r','cleft-l','root-l','left',closed=True)
        self.add_arc('floss-top',(30,14),(42,26),radius_x=12)
        self.add_line('floss-down',(42,26),(42,36))
        self.add_contour('floss','floss-top','floss-down')
        self.relate('connect','floss','tooth')
