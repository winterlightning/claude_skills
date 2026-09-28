"""Hands Shaping Pottery.

Plan: Central rounded pot touched by mirrored cupped hands. Remove finger separations and rim ellipse; preserve open vessel lip. Bounds (6,6)-(42,42). Shared human reference proportions; mirrored hands.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '20339a75-190c-4916-aca5-b1978d81d7c4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-shaping-pottery/20260927T135945Z-thuan-mac-1/reference/crafts pottery_20339a75-190c-4916-aca5-b1978d81d7c4.svg'
AUTHOR = 'gpt-6'

class HandsShapingPottery(Solo48):
    icon_id = 'hands-shaping-pottery'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('hands', 'shaping', 'pottery')

    def build(self):
        self.add_arc('lip-1',(16,6),(32,6),radius_x=8,radius_y=3,sweep=False)
        self.add_arc('pot-right',(32,6),(34,20),radius_x=14,radius_y=14)
        self.add_arc('pot-bottom-r',(34,20),(30,28),radius_x=10)
        self.add_arc('pot-br',(30,28),(24,30),radius_x=10)
        self.add_arc('pot-bl',(24,30),(18,28),radius_x=10)
        self.add_arc('pot-bottom-l',(18,28),(14,20),radius_x=10)
        self.add_arc('pot-left',(14,20),(16,6),radius_x=14,radius_y=14)
        self.add_contour('pot','lip-1','pot-right','pot-bottom-r','pot-br','pot-bl','pot-bottom-l','pot-left',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='lip']
        for side in [-1,1]:
         def p(x,y):return (24+side*x,y)
         name='left' if side<0 else 'right'
         self.add_polyline(name,p(14,42),p(18,32),p(18,26))
         self.add_line(name+'-thumb',p(6,42),p(6,28))
        self.relate('connect','pot','left-thumb')
        self.relate('connect','pot','right-thumb')
