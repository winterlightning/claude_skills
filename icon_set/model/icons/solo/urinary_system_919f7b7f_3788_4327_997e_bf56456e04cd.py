"""Urinary System.

Plan: Mirrored bean kidneys, descending ureters and a round bladder; shared anatomical attachment nodes. Bounds (8,4)-(40,44). No useful Lucide organ match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '919f7b7f-3788-4327-997e-bf56456e04cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/urinary system_919f7b7f-3788-4327-997e-bf56456e04cd.svg'
AUTHOR = 'gpt-6'


class UrinarySystem(Solo48):
    icon_id = 'urinary-system'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('urinary', 'system')

    def build(self):
        for p,x,s in [('left',13,1),('right',35,-1)]:
            self.add_arc(p+'-outer',(x,4),(x,24),radius_x=5,radius_y=10,sweep=(s<0))
            self.add_arc(p+'-lower',(x,24),(x+6*s,18),radius_x=6,sweep=(s<0))
            self.add_arc(p+'-notch',(x+6*s,18),(x+6*s,10),radius_x=1,radius_y=4,sweep=(s>0))
            self.add_arc(p+'-upper',(x+6*s,10),(x,4),radius_x=6,sweep=(s<0))
            self.add_contour(p+'-kidney',p+'-outer',p+'-lower',p+'-notch',p+'-upper',closed=True)
            self.add_polyline(p+'-ureter',(x+6*s,18),(x+6*s,26),(24,30))
            self.relate('connect',p+'-kidney',p+'-ureter')
        self.add_arc('bladder-r',(24,30),(24,42),radius_x=6)
        self.add_arc('bladder-l',(24,42),(24,30),radius_x=6)
        self.add_contour('bladder','bladder-r','bladder-l',closed=True)
        for p in ['left','right']:self.relate('connect',p+'-ureter','bladder')
        self.relate('connect','left-ureter','right-ureter')
        self.add_line('outlet',(24,42),(24,44))
        self.relate('connect','outlet','bladder')
