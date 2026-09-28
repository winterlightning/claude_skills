"""Cheerful face with matching arched eyes and open smiling mouth. Circular geometry replaces wobbly fitted paths; shared x24 axis and equal eye radii. No useful exact Lucide expression match. No omissions.
Keyshape CIRCLE: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c7cf76c8-ffda-5a5f-b891-db7de9398c9c'
SOURCE_PATH = 'pictographic-primitives/smileys/cheerful_c7cf76c8-ffda-5a5f-b891-db7de9398c9c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='cheerful'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases=()
    keywords=('cheerful',)

    def build(self):
        self.circle('face',24,24,20)
        for n,x in [('left',17),('right',31)]:self.add_arc(n+'-eye',(x-2,17),(x+2,17),radius_x=2,sweep=True)
        self.path('mouth',(15,26),[('L',(33,26)),('A',(15,26),9,9,True)],True)

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
