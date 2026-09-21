"""Rounded Three-Toed Bird Track
Plan: Three forward toes and one rear toe share a central joint at (24,30). Mirror outer toes on x24.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: No useful exact Lucide match; coherent round-ended branching strokes.
Reduction: Replaced narrow double-outline toes with single round strokes, retaining all four toes.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95265ca4-ddcd-4898-979c-468dc73f3582'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/animal print bird 2_95265ca4-ddcd-4898-979c-468dc73f3582.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-three-toed-bird-track'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('bird', 'track', 'footprint', 'toes', 'animal', 'print', 'wildlife')

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
        self.add_polyline('center',(24,4),(24,30),(24,44))
        for name,x in [('left',8),('right',40)]:
            self.add_line(name,(24,30),(x,14))
            self.relate('connect',name,'center-1');self.relate('connect',name,'center-2')
        self.relate('connect','left','right')
