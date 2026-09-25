"""Couple under Full Moon.

Plan: Two touching shoulder silhouettes below a full moon. Remove fine hairstyle and bun. Shared human references: head radius 4, centers y28, shoulders y40 give exactly 8 centerline gap. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46c2e428-1adc-45b9-94af-8f84b6abfeda'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/qiqiao festival_46c2e428-1adc-45b9-94af-8f84b6abfeda.svg'
AUTHOR = 'gpt-6'

class CoupleUnderFullMoon(Solo48):
    icon_id = 'couple-under-full-moon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('couple', 'under', 'full', 'moon')

    def build(self):
        for name,x,y,r in [('moon',24,10,6),('left-head',14,28,4),('right-head',34,28,4)]:
         self.add_arc(name+'-r',(x,y-r),(x,y+r),radius_x=r)
         self.add_arc(name+'-l',(x,y+r),(x,y-r),radius_x=r)
         self.add_contour(name,name+'-r',name+'-l',closed=True)
        self.add_arc('left-outer',(8,44),(14,40),radius_x=6,radius_y=4)
        self.add_arc('left-inner',(14,40),(24,44),radius_x=10,radius_y=4)
        self.add_contour('left-shoulders','left-outer','left-inner')
        self.add_arc('right-inner',(24,44),(34,40),radius_x=10,radius_y=4)
        self.add_arc('right-outer',(34,40),(40,44),radius_x=6,radius_y=4)
        self.add_contour('right-shoulders','right-inner','right-outer')
        self.relate('connect','left-shoulders','right-shoulders')
