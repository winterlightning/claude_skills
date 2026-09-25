"""Simple Eagle Bird Profile.

Plan: Right-facing hooked beak, rounded head, broad breast and pointed wing retained. Omitted the tiny eye and widened the wing opening. Keyshape SQUARE uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ea98f2c-77cb-4838-b4c3-330b98bee82d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/condor_7ea98f2c-77cb-4838-b4c3-330b98bee82d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hooked-beak-bird-bust'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hooked', 'beak', 'bird', 'bust')

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

        path('bird',(20,42),[('C',(36,29),(31,42),(36,36)),('C',(34,19),(36,24),(32,22)),('C',(42,20),(36,17),(39,18)),('C',(34,11),(41,14),(38,11)),('C',(24,6),(32,7),(29,6)),('C',(14,16),(17,6),(15,10)),('L',(6,42)),('C',(21,29),(13,38),(21,33)),('C',(12,25),(21,25),(17,24))])
