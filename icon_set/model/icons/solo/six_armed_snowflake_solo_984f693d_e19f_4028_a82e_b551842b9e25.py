"""Six-Armed Snowflake
Plan: Six spokes, each with two short branches; mirrored pairs around center.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide snowflake: repeated forked arms; source central spoke layout preserved.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '984f693d-e19f-4028-a82e-b551842b9e25'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/frost_984f693d-e19f-4028-a82e-b551842b9e25.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'six-armed-snowflake-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('snowflake', 'snow', 'ice', 'winter', 'branches', 'crystal', 'weather')

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
        center=(24,24)
        ends=[(24,6),(42,14),(42,34),(24,42),(6,34),(6,14)]
        joints=[(24,13),(35,18),(35,30),(24,35),(13,30),(13,18)]
        prongs=[((18,7),(30,7)),((35,10),(42,21)),((42,27),(35,38)),((30,41),(18,41)),((13,38),(6,27)),((6,21),(13,10))]
        for i,(end,joint,pair) in enumerate(zip(ends,joints,prongs)):
         self.add_polyline(f'spoke-{i}',center,joint,end)
         self.add_polyline(f'fork-{i}',pair[0],joint,pair[1]);self.relate('connect',f'spoke-{i}',f'fork-{i}')
        for a in range(6):
         for b in range(a+1,6):self.relate('connect',f'spoke-{a}',f'spoke-{b}')
