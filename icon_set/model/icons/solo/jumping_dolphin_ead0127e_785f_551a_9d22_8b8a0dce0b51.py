"""Jumping dolphin with arched back, beak, dorsal and pectoral fins and tail flukes. Lucide fish informs coherent organic outline. Natural asymmetry retained; omit eye at native scale.
Keyshape SQUARE: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ead0127e-785f-551a-9d22-8b8a0dce0b51'
SOURCE_PATH = 'pictographic-primitives/animals/dolphin_ead0127e-785f-551a-9d22-8b8a0dce0b51.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='jumping-dolphin'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases=()
    keywords=('jumping', 'dolphin')

    def build(self):
        self.path('dolphin',(6,26),[('L',(8,22)),('C',(20,12),(8,16),(14,12)),('C',(30,6),(22,8),(26,6)),('L',(28,14)),('C',(38,30),(34,16),(38,22)),('C',(42,42),(38,34),(42,36)),('L',(34,39)),('L',(26,42)),('C',(30,34),(26,38),(28,35)),('C',(24,22),(28,28),(25,24)),('L',(20,32)),('L',(14,24)),('C',(6,26),(11,26),(6,28))],True)

    def path(self,name,start,commands,closed=False):
        members=[];here=start
        for j,(kind,end,*args) in enumerate(commands):
            eid=f'{name}-{j}'
            if kind=='L':self.add_line(eid,here,end)
            elif kind=='A':self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C':self.add_bezier(eid,here,(args[0],args[1],end))
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
