"""Ergonomic Shoe Horn Tool.

Plan: Diagonal ergonomic shoehorn, round ends and concave waist. Bounds6,6,42,42. Omit tiny hanging puncture.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6aea8bdb-fb8d-4eaf-aedc-68cf46a16a2c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shoe horn_6aea8bdb-fb8d-4eaf-aedc-68cf46a16a2c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-curved-shoehorn'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('long', 'curved', 'shoehorn')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('horn',(9,27),[('C',(30,9),(19,19),(23,17)),('C',(36,6),(32,7),(34,6)),('A',(42,12),6,6,True),('C',(38,19),(42,15),(40,17)),('C',(21,39),(29,27),(25,36)),('C',(15,42),(19,42),(17,42)),('C',(6,34),(9,42),(6,40)),('C',(9,27),(6,31),(7,29))],True)
