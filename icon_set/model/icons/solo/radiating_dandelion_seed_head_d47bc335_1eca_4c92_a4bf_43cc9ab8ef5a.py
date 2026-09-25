"""Simple Dandelion Seed Head.

Plan: Radiating seedhead and curved stem retained with seven clear spokes. Removed the tiny hooked endpoint. Keyshape SQUARE uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd47bc335-1eca-4c92-a4bf-43cc9ab8ef5a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/dandelion_d47bc335-1eca-4c92-a4bf-43cc9ab8ef5a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'radiating-dandelion-seed-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('radiating', 'dandelion', 'seed', 'head')

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

        ends=[(6,20),(10,9),(23,6),(36,9),(42,20),(37,32),(11,31)]
        for j,end in enumerate(ends):
         line(f'spoke{j}',(24,22),end)
         for k in range(j):join(f'spoke{j}',f'spoke{k}')
        path('stem',(24,22),[('C',(18,42),(24,31),(21,38))])
        for j in range(len(ends)):join('stem',f'spoke{j}')
