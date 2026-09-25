"""Tadpole with Raised Tail
Plan: Broad left-facing head narrows into rising curved tail.
Keyshape: HRECT_M; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2dd2c3fe-0eea-41e2-94df-00b1d9d02c4b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/polliwog_2dd2c3fe-0eea-41e2-94df-00b1d9d02c4b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tadpole-with-raised-tail'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tadpole', 'polliwog', 'amphibian', 'frog', 'tail', 'pond')

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
        path('tadpole',(4,24),[('C',(16,10),(4,15),(9,10)),('C',(31,18),(23,10),(26,18)),('C',(44,11),(36,18),(41,14)),('C',(28,32),(44,27),(34,29)),('C',(15,38),(23,33),(24,38)),('C',(4,24),(7,38),(4,32))],True)
        circle('eye',16,24,3)
