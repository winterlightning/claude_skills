"""Tapered Cream Tube with Cap
Plan: Tapered tube with broad top seam and bottom cap
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: No useful Lucide match; simple tapered contour.
Reduction: Omit empty label."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9ad83a1-1edf-4b8d-b496-234522ea9376'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cream_b9ad83a1-1edf-4b8d-b496-234522ea9376.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tapered-cream-tube-with-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cream', 'tube', 'cosmetic', 'cap', 'skincare', 'container', 'toiletry')

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
        path('tube',(8,4),[('L',(40,4)),('L',(34,34)),('L',(14,34)),('L',(8,4))],True)
        self.add_line('seam',(10,12),(38,12));self.relate('connect','seam','tube')
        path('cap',(14,34),[('L',(14,44)),('L',(34,44)),('L',(34,34))]);self.relate('connect','cap','tube')
