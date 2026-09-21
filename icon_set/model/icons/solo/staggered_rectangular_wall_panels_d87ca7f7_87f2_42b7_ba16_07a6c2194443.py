"""Staggered Rectangular Wall Panels
Plan: Three horizontal wall courses with alternating masonry joints; shared grid intersection nodes.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide brick-wall: staggered grid and joined wall outline.
Reduction: Kept all seven blocks; squared outer corners.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd87ca7f7-87f2-42b7-ba16-07a6c2194443'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/siding_d87ca7f7-87f2-42b7-ba16-07a6c2194443.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'staggered-rectangular-wall-panels'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/construction'
    aliases = ()
    keywords = ('siding', 'wall', 'panel', 'brick', 'course', 'construction')

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
        xs=[4,16,24,32,44]; ys=[8,19,29,40]
        for j,y in enumerate(ys):
            self.add_polyline(f'row-{j}',*((x,y) for x in xs))
        for side,x in [('left',4),('right',44)]:
            self.add_polyline(side,*((x,y) for y in ys))
        for j,columns in enumerate([[24],[16,32],[24]]):
            for x in columns:self.add_line(f'joint-{j}-{x}',(x,ys[j]),(x,ys[j+1]))
        # Every declared join is an exactly shared masonry intersection.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}:self.relate('connect',a.element_id,b.element_id)

SOURCE_REFERENCES = (('09a317f7-f2a4-41c5-9e0a-3739286ec396', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stucco_09a317f7-f2a4-41c5-9e0a-3739286ec396.svg'),)
