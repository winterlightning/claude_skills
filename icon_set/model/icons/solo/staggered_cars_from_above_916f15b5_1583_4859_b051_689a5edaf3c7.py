"""Staggered Cars from Above
Plan: Large overhead car upper-right and a cropped second vehicle lower-left form a physical driving scene.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: No useful exact Lucide match; rounded vehicle shell.
Reduction: Omitted mirrors; retained windshield and partial second car.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '916f15b5-1583-4859-b051-689a5edaf3c7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blind spot lane change assistance_916f15b5-1583-4859-b051-689a5edaf3c7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'staggered-cars-from-above'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cars', 'traffic', 'vehicle', 'driving', 'blind-spot', 'road', 'overhead')

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
        rect('car',20,6,22,26,6)
        self.add_line('windshield',(29,16),(33,16))
        path('following-car',(6,42),[('L',(6,38)),('A',(14,38),4,4,True),('L',(14,42))])
