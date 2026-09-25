"""Birdhouse with Round Entrance and Perch
Plan: Gabled birdhouse, round entrance and lower perch.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide house: simple joined facade and roof.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1dc3cd8-4582-487d-8dfe-97078ca035bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/cuckoo_a1dc3cd8-4582-487d-8dfe-97078ca035bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'birdhouse-with-round-entrance-and-perch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('birdhouse', 'bird', 'house', 'entrance', 'roof', 'perch', 'nesting')

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
        self.add_polyline('roof',(6,20),(24,6),(42,20))
        path('house',(10,17),[('L',(10,35)),('A',(13,38),3,3,False),('L',(35,38)),('A',(38,35),3,3,False),('L',(38,17))])
        circle('entrance',24,24,5)
        self.add_line('perch',(24,38),(24,42))
        self.relate('connect','roof','house');self.relate('connect','perch','house')
