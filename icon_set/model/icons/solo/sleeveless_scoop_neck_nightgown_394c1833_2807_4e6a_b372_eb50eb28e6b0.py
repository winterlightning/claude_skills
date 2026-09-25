"""Sleeveless Scoop-Neck Nightgown
Plan: Scoop neckline, short shoulder straps and flared gown.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '394c1833-2807-4e6a-b372-eb50eb28e6b0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nightgown_394c1833-2807-4e6a-b372-eb50eb28e6b0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sleeveless-scoop-neck-nightgown'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('nightgown', 'dress', 'sleeveless', 'clothing', 'nightwear', 'garment')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('nightgown',(18,4),[('A',(30,4),6,4,False),('L',(40,4)),('C',(36,18),(40,10),(36,14)),('L',(40,41)),('C',(24,44),(34,43),(29,44)),('C',(8,41),(19,44),(14,43)),('L',(12,18)),('C',(8,4),(12,14),(8,10)),('L',(18,4))],True)
