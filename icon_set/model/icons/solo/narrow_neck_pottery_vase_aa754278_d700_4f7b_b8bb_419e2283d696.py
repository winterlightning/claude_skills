"""Simple Ceramic Pottery Vase.

Plan: Flared lip, narrow neck, rounded shoulders and short flat base retained. Keyshape VRECT_M uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa754278-d700-4f7b-b8bb-419e2283d696'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/ceramics_aa754278-d700-4f7b-b8bb-419e2283d696.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'narrow-neck-pottery-vase'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('narrow', 'neck', 'pottery', 'vase')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('vase',(16,4),[('L',(32,4)),('C',(30,12),(29,8),(28,9)),('C',(38,24),(30,16),(38,17)),('C',(30,44),(38,32),(33,40)),('L',(18,44)),('C',(10,24),(15,40),(10,32)),('C',(18,12),(10,17),(18,16)),('C',(16,4),(20,9),(19,8))],True)
