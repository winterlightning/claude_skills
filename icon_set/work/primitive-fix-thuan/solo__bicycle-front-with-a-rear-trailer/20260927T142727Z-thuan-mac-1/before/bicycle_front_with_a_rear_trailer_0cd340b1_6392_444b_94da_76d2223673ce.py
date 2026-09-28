"""Bicycle Front with a Rear Trailer
Plan: Two wheels share y32; the front fork joins its wheel at the top; the trailer and connecting frame sit above the small rear wheel. Deliberately unequal wheels and rightward movement.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide bike: circular wheels and a spare frame.
Reduction: Dropped internal trailer trim; retained trailer, both wheels, fork and handlebar.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cd340b1-6392-444b-94da-76d2223673ce'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bike stroller back_0cd340b1-6392-444b-94da-76d2223673ce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bicycle-front-with-a-rear-trailer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bicycle', 'trailer', 'cart', 'wheel', 'transport', 'frame', 'towing')

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
        circle('front-wheel',36,32,8);circle('trailer-wheel',10,36,4)
        self.add_polyline('trailer',(4,12),(20,12),(20,18),(20,23),(10,23),(4,23),closed=True)
        self.add_polyline('tow',(20,18),(24,18),(32,8))
        self.add_polyline('fork',(36,24),(32,8),(28,8))
        self.add_line('axle',(10,23),(10,32))
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}:self.relate('connect',a.element_id,b.element_id)
