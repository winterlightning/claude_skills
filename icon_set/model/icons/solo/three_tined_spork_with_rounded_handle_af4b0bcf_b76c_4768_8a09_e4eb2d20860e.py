"""A three-tined spork with a broad rounded bowl and loop-shaped handle.
Plan: VRECT_M fits the upright utensil within centerlines (10,4)-(38,44).
Reduction: Tines reduced to centerline strokes; bowl and rounded outlined handle retained.
Construction: Lucide utensils: shared-axis tines, rounded bowl transitions and long handle.
Layout: Bowl sides mirror around x24; handle uses equal vertical sides and radius6 lower cap."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af4b0bcf-b76c-4768-8a09-e4eb2d20860e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/spork_af4b0bcf-b76c-4768-8a09-e4eb2d20860e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'three-tined-spork-with-rounded-handle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('spork', 'utensil', 'spoon', 'fork', 'tines', 'cutlery')

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
        # Shared bowl shoulders join the rounded handle at exact endpoints.
        path('bowl',(12,4),[('C',(10,16),(10,8),(10,12)),('A',(18,24),8,8,False),('L',(24,24)),('L',(30,24)),('A',(38,16),8,8,False),('C',(36,4),(38,12),(38,8))])
        self.add_line('middle-tine',(24,4),(24,24))
        path('handle',(18,24),[('L',(18,38)),('A',(30,38),6,6,False),('L',(30,24))])
        self.relate('connect','bowl','handle');self.relate('connect','bowl','middle-tine')
