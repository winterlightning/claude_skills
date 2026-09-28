"""Three Star Rating.

Plan: Attempt a horizontal row of three equal five-point stars. Native row cannot fill an exact28u-high solo rectangle without narrow distorted stars or insufficient inter-star clearance.
Construction: Lucide star original/debug: five-point outline; repeated equal row retained.
Reduction: No star removed or row arrangement changed. Attempt retained for validation and manual review if it fails.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf0d9970-8b38-5723-b109-a3be9696acdb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/26-cf0d9970-8b38-5723-b109-a3be9696acdb.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-star-rating-row'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "rating"
    categories = ("rating", "primitives")
    aliases = ()
    keywords = ('three', 'star', 'rating', 'row')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        for j,cx in enumerate((10,24,38)):
         poly(f'star-{j}',(cx,10),(cx+2,20),(cx+6,20),(cx+3,27),(cx+4,38),(cx,32),(cx-4,38),(cx-3,27),(cx-6,20),(cx-2,20),closed=True)
