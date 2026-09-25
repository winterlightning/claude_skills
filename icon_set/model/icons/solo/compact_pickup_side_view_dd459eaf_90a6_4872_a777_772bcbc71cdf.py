"""Compact pickup with raised cabin, bed and paired wheels.
Plan: HRECT_M matches the low vehicle silhouette.
Reduction: Wheels reduced to radius three; body terminates at wheel rims. Cabin, bed and both wheels retained.
Construction: car: body terminates at wheel cardinal points; shared wheel radius and baseline. Asymmetric cabin/bed arrangement retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd459eaf-90a6-4872-a777-772bcbc71cdf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pickup_dd459eaf-90a6-4872-a777-772bcbc71cdf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'compact-pickup-side-view'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pickup', 'truck', 'vehicle', 'wheels', 'cab', 'transport')

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
        # Paired wheels share radius/baseline; body ends on wheel cardinal nodes.
        path('body',(9,35),[('L',(8,35)),('A',(4,31),4,4,True),('L',(4,18)),('L',(22,18)),('L',(22,10)),('L',(30,10)),('L',(38,18)),('L',(44,18)),('L',(44,31)),('A',(40,35),4,4,True),('L',(39,35))])
        self.add_line('cabin-base',(22,18),(38,18));self.relate('connect','cabin-base','body')
        self.add_line('base',(15,35),(33,35))
        for x in (12,36):
            circle(f'wheel-{x}',x,35,3)
            self.relate('connect','base',f'wheel-{x}');self.relate('connect','body',f'wheel-{x}')
