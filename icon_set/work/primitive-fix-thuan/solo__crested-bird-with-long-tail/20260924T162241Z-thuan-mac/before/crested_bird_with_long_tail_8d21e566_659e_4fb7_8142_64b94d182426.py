"""Crested Bird with Long Tail
Plan: Right-facing crested bird with sweeping tail and wing
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide bird coherent silhouette.
Reduction: Remove tiny eye; retain crest, beak and tail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d21e566-659e-4fb7-8142-64b94d182426'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/cardinal_8d21e566-659e-4fb7-8142-64b94d182426.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crested-bird-with-long-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cardinal', 'bird', 'crest', 'tail', 'wing', 'beak', 'wildlife')

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
        path('bird',(6,42),[('L',(12,24)),('C',(28,14),(18,22),(20,14)),('L',(32,6)),('L',(36,14)),('L',(42,18)),('L',(36,22)),('C',(26,34),(36,30),(32,34)),('L',(6,42))],True)
        self.add_line('leg',(26,34),(26,42));self.relate('connect','leg','bird')
