"""Five Staggered Masonry Blocks
Plan: Five masonry blocks in three staggered courses, with side recesses.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide brick-wall: shared grid joints.
Reduction: No blocks omitted; mortar joins expressed as shared edges.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5052672d-b690-4f47-83cc-e9462c05b2dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stonework_5052672d-b690-4f47-83cc-e9462c05b2dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'five-staggered-masonry-blocks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/construction'
    aliases = ()
    keywords = ('masonry', 'blocks', 'stonework', 'wall', 'brick', 'construction')

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
        self.add_polyline('outline',(4,8),(24,8),(44,8),(44,19),(34,19),(34,29),(44,29),(44,40),(24,40),(4,40),(4,29),(14,29),(14,19),(4,19),closed=True)
        self.add_line('upper-middle',(24,8),(24,19));self.add_line('lower-middle',(24,29),(24,40))
        self.add_polyline('row-upper',(14,19),(24,19),(34,19))
        self.add_polyline('row-lower',(14,29),(24,29),(34,29))
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}:self.relate('connect',a.element_id,b.element_id)
