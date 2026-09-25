"""Pitched-Roof Pavilion
Plan: Triangular roof, two supports and divided lower plinth.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide house: joined roof and facade.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2df6fcde-99c0-436d-bab7-1961113e7c69'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pavilion_2df6fcde-99c0-436d-bab7-1961113e7c69.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pitched-roof-pavilion'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pavilion', 'roof', 'shelter', 'building', 'structure', 'outdoors')

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
        self.add_polyline('roof',(6,20),(24,6),(42,20),closed=True)
        self.add_polyline('walls',(10,20),(10,42),(38,42),(38,20))
        self.add_line('base-division',(10,33),(38,33))
        self.relate('connect','roof','walls');self.relate('connect','walls','base-division')
