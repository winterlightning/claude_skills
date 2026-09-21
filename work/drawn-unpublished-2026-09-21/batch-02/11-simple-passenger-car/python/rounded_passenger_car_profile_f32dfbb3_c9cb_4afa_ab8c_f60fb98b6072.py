"""Rounded Passenger Car Profile
Plan: Paired wheels beneath low body and raised cabin.
Keyshape: HRECT_M; exact inset SOLO48 envelope.
Construction: Lucide car: body stops at wheel rims.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f32dfbb3-c9cb-4afa-ab8c-f60fb98b6072'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/buggy_f32dfbb3-c9cb-4afa-ab8c-f60fb98b6072.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-passenger-car-profile'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('roof',(10,18),[('L',(15,12)),('C',(19,10),(16,10),(17,10)),('L',(29,10)),('C',(33,12),(31,10),(32,10)),('L',(38,18))])
        path('body',(8,32),[('L',(4,32)),('L',(4,23)),('A',(9,18),5,5,True),('L',(39,18)),('A',(44,23),5,5,True),('L',(44,32)),('L',(40,32))])
        for x in (14,34):circle(f'wheel-{x}',x,32,6)
        self.add_line('underbody',(20,32),(28,32))
        self.relate('connect','roof','body')
        for x in (14,34):
         self.relate('connect','body',f'wheel-{x}');self.relate('connect','underbody',f'wheel-{x}')
