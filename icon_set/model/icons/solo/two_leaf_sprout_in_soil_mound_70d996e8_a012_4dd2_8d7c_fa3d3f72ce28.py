"""Two Leaf Sprout in Soil Mound
Plan: Paired pointed leaves above central stem and low uneven soil mound.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide sprout: joined leaf tips and stem.
Reduction: Tiny soil texture omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70d996e8-a012-4dd2-8d7c-fa3d3f72ce28'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dirt_70d996e8-a012-4dd2-8d7c-fa3d3f72ce28.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-leaf-sprout-in-soil-mound'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('sprout', 'soil', 'leaves', 'plant', 'seedling', 'mound', 'growth')

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
        path('soil',(6,42),[('C',(14,32),(6,35),(9,34)),('C',(24,30),(17,27),(19,30)),('C',(34,32),(29,30),(31,27)),('C',(42,42),(39,34),(42,35)),('L',(6,42))],True)
        self.add_line('stem',(24,20),(24,30));self.relate('connect','stem','soil')
        for s in (-1,1):
         path(f'leaf-{s}',(24,20),[('C',(24+s*16,6),(24+s*1,9),(24+s*9,6)),('C',(24,20),(24+s*16,17),(24+s*10,20))],True);self.relate('connect',f'leaf-{s}','stem')
        self.relate('connect','leaf--1','leaf-1')
