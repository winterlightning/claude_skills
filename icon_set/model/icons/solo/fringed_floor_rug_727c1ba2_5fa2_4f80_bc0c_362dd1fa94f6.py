"""Floor Carpet with Fringe.

Plan: Perspective floor rug with broad panels and repeated fringe; bounds8,4,40,44. Four evenly spaced fringe strands.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '727c1ba2-5fa2-4f80-bc0c-362dd1fa94f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/carpeting_727c1ba2-5fa2-4f80-bc0c-362dd1fa94f6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fringed-floor-rug'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('fringed', 'floor', 'rug')

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

        poly('rug',(12,4),(36,4),(36,20),(40,36),(8,36),(12,20),closed=True)
        line('fold',(12,20),(36,20));join('fold','rug')
        for j,x in enumerate([8,18,30,40]):line(f'fringe-{j}',(x,36),(x,44));join(f'fringe-{j}','rug')
