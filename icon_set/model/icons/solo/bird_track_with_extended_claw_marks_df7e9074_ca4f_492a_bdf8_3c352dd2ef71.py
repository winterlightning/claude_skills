"""Bird Track with Extended Claw Marks
Plan: Four toes radiate from a central stem, with long fine-looking terminal extensions expressed in the same mandatory stroke.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: No useful exact Lucide match.
Reduction: Unified claw and toe strokes instead of crowded nested outlines; preserves four directions.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df7e9074-ca4f-492a-bdf8-3c352dd2ef71'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/animal print bird 3_df7e9074-ca4f-492a-bdf8-3c352dd2ef71.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bird-track-with-extended-claw-marks'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bird', 'track', 'footprint', 'claws', 'toes', 'animal', 'print')

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
        self.add_polyline('center',(24,4),(24,28),(24,44))
        for name,x in [('left',8),('right',40)]:
            self.add_polyline(name,(24,28),(x,12),(x,8))
            self.relate('connect',name+'-1','center-1');self.relate('connect',name+'-1','center-2')
        self.relate('connect','left-1','right-1')
