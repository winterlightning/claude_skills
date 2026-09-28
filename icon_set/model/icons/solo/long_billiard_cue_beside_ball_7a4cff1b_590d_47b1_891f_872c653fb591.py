"""Long Billiard Cue Beside Ball
Plan: A long diagonal cue and a separated ball occupy opposite sides of the diagonal.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: No useful exact Lucide match; round-ended line and circular ball.
Reduction: Cue rendered as one heavy stroke instead of an unworkably narrow double outline.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a4cff1b-590d-47b1-891f-872c653fb591'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/cue_7a4cff1b-590d-47b1-891f-872c653fb591.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-billiard-cue-beside-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('billiards', 'cue', 'ball', 'pool', 'sport', 'equipment', 'game')

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
        self.add_line('cue',(6,42),(42,6))
        circle('ball',36,36,6)
