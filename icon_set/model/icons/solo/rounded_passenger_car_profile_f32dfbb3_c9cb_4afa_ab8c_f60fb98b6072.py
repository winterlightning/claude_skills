"""Passenger car with a raised cabin and paired wheels.
Plan: HRECT_M follows the wide, low vehicle.
Reduction: Wheel radius reduced to three; cabin and wheel gaps enlarged.
Construction: car: body ends at wheel rims and both wheels share radius and baseline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f32dfbb3-c9cb-4afa-ab8c-f60fb98b6072'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/buggy_f32dfbb3-c9cb-4afa-ab8c-f60fb98b6072.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-passenger-car-profile'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('car', 'vehicle', 'transport', 'wheels', 'passenger', 'cabin', 'profile')

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
        # Mirrored cabin and paired wheel construction; body terminates at wheel rims.
        path('roof',(12,22),[('L',(17,12)),('C',(20,10),(18,10),(19,10)),('L',(28,10)),('C',(31,12),(29,10),(30,10)),('L',(36,22))])
        path('body',(11,35),[('L',(8,35)),('A',(4,31),4,4,True),('L',(4,26)),('A',(8,22),4,4,True),('L',(12,22)),('L',(36,22)),('L',(40,22)),('A',(44,26),4,4,True),('L',(44,31)),('A',(40,35),4,4,True),('L',(37,35))])
        for x in (14,34):circle(f'wheel-{x}',x,35,3)
        self.add_line('underbody',(17,35),(31,35))
        self.relate('connect','roof','body')
        for x in (14,34):
            self.relate('connect','body',f'wheel-{x}')
            self.relate('connect','underbody',f'wheel-{x}')
