"""Single Natural Leaf Symbol.

Plan: Organic upper-right leaf and short curved stem. Bounds6,6,42,42. Preserve asymmetry, simplify vein into attached sweeping stem.
Construction reference: leaf.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6fdfd401-d05a-46a2-a4d7-4cc5b8329462'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf right_6fdfd401-d05a-46a2-a4d7-4cc5b8329462.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'natural-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('natural', 'leaf')

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

        path('leaf',(12,36),[('C',(42,6),(0,16),(34,22)),('C',(12,36),(42,34),(30,46))],True)
        path('vein',(6,42),[('L',(12,36)),('C',(25,24),(16,30),(20,26))]);join('vein','leaf')
