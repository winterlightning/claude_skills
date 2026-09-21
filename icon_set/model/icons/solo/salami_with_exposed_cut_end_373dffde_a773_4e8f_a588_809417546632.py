"""Salami with Exposed Cut End
Plan: Horizontal sausage with oval cut face and tied wrapper.
Keyshape: HRECT_M; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Wrapper end opened; cut-face speckles reduced to one.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '373dffde-a773-4e8f-a588-809417546632'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/salami_373dffde-a773-4e8f-a588-809417546632.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'salami-with-exposed-cut-end'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('salami', 'sausage', 'food', 'meat', 'slice', 'wrapper')

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
        path('cut',(4,24),[('A',(13,10),9,14,True),('A',(22,24),9,14,True),('A',(13,38),9,14,True),('A',(4,24),9,14,True)],True)
        path('body',(13,10),[('L',(26,10)),('A',(36,24),10,14,True),('A',(26,38),10,14,True),('L',(13,38))]);self.relate('connect','cut','body')
        self.add_polyline('tie',(44,16),(36,24),(44,32));self.relate('connect','tie','body')
        self.add_dot('speckle',(13,24))
