"""Spiral Lollipop on Upright Stick
Plan: Single curling candy contour with upright stick; spiral turn preserved.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Inner curl shortened to maintain a clear spiral opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6f3f418-9129-4fb0-abbb-79cc66b9dabb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/lollipop_a6f3f418-9129-4fb0-abbb-79cc66b9dabb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spiral-lollipop-on-upright-stick'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('lollipop', 'candy', 'spiral', 'stick', 'sweet', 'treat', 'food')

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
        path('spiral',(24,36),[('A',(8,20),16,16,True),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('C',(24,27),(40,27),(30,27)),('A',(17,20),7,7,True),('A',(24,13),7,7,True)])
        self.add_line('stick',(24,36),(24,44));self.relate('connect','stick','spiral')
