"""Confused Face
Plan: Round face, paired eyes and uneven mouth
Keyshape CIRCLE: (2, 2, 46, 46).
Construction reference: No useful local smile match; circular face construction.
Reduction: Remove cramped eyebrows; uneven mouth carries confusion."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2442834f-69c1-4c5b-9c90-b256f2ccac05'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face confused_2442834f-69c1-4c5b-9c90-b256f2ccac05.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'confused-face-with-wavy-mouth'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('face', 'confused', 'expression', 'emotion', 'eyes', 'mouth', 'puzzled')

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
        circle('face',24,24,20)
        self.add_dot('left-eye',(16,19));self.add_dot('right-eye',(32,19))
        path('mouth',(16,32),[('C',(32,30),(21,24),(27,38))])
