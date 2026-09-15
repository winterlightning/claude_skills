"""Upright spoon and knife as a dining pair. Lucide utensils informs shared handle baseline and coherent knife contour; source spoon bowl retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='6046ac0b-bf44-4b83-b72a-c006127eaef4'
SOURCE_PATH='pictographic-primitives/symbol/spoon folk vertical_6046ac0b-bf44-4b83-b72a-c006127eaef4.svg'
AUTHOR='gpt-6'

class SpoonAndKnife(Solo48):
    icon_id='spoon-and-knife'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('cutlery', 'spoon', 'knife', 'restaurant', 'dining', 'food', 'eat', 'utensils')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.oval('spoon-bowl',14,16,8,10)
        self.add_line('spoon-handle',(14,26),(14,42))
        self.relate('connect','spoon-bowl','spoon-handle')
        self.path('knife-spine',[(34,42),(34,30),(34,6)])
        self.add_arc('knife-blade',(34,6),(42,30),radius_x=40,sweep=True)
        self.add_line('knife-base',(42,30),(34,30))
        self.relate('connect','knife-spine','knife-blade')
        self.relate('connect','knife-spine','knife-base')
        self.relate('connect','knife-blade','knife-base')
