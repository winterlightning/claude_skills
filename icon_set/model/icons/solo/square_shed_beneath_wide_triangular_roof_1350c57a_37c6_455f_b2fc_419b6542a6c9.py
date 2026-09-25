"""Square Shed beneath Wide Triangular Roof
Plan: Symmetric gabled house with overhanging eaves and central doorway.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide house: open doorway shares lower boundary.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1350c57a-37c6-455f-b2fc-419b6542a6c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shed_1350c57a-37c6-455f-b2fc-419b6542a6c9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-shed-beneath-wide-triangular-roof'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('shed', 'building', 'roof', 'door', 'house', 'storage')

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
        self.add_polyline('walls',(10,20),(10,42),(20,42),(20,29),(28,29),(28,42),(38,42),(38,20))
        self.add_line('eaves',(6,20),(42,20))
        self.relate('connect','roof','eaves');self.relate('connect','walls','eaves');self.relate('connect','walls','roof')
