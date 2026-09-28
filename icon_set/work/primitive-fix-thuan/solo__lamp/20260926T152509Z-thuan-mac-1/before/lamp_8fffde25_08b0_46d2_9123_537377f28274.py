"""Articulated desk lamp with tilted shade, circular pivot and semicircular base. Lucide lamp-desk informs crisp shade edges and straight arms. Source shade orientation retained; small neck detail simplified.
Keyshape SQUARE: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8fffde25-08b0-46d2-9123-537377f28274'
SOURCE_PATH = 'pictographic-primitives/office/lamp_8fffde25-08b0-46d2-9123-537377f28274.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='lamp'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('lamp',)

    def build(self):
        self.path('shade',(6,12),[('L',(18,24)),('A',(22,20),4,4,False),('L',(20,12)),('A',(20,6),3,3,False),('L',(14,10)),('L',(6,12))],True)
        self.add_line('upper-arm',(20,12),(34,24));self.relate('connect','shade','upper-arm')
        self.circle('pivot',38,24,4);self.relate('connect','upper-arm','pivot')
        self.add_line('lower-arm',(34,24),(28,34));self.relate('connect','lower-arm','pivot');self.relate('connect','lower-arm','upper-arm')
        self.path('base',(20,42),[('A',(28,34),8,8,True),('A',(36,42),8,8,True),('L',(20,42))],True);self.relate('connect','lower-arm','base')

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
