"""Layered Pinecone on Stem
Plan: Axial pinecone with layered pointed scales and bottom stem.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Reduced overlap network into two broad rows."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7eb9b49-84dd-4eea-9f75-a357ae86c92a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pinecone_e7eb9b49-84dd-4eea-9f75-a357ae86c92a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'layered-pinecone-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pinecone', 'cone', 'scales', 'seed', 'plant', 'stem')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('cone',(24,4),[('C',(35,14),(29,6),(33,12)),('L',(40,21)),('C',(24,36),(40,32),(33,36)),('C',(8,21),(15,36),(8,32)),('L',(13,14)),('C',(24,4),(15,12),(19,6))],True)
        poly('scales',(8,21),(24,29),(40,21));join('scales','cone')
        poly('upper-scales',(13,14),(24,19),(35,14));join('upper-scales','cone')
        line('stem',(24,36),(24,44));join('stem','cone')
