"""Four Interlocking Puzzle Pieces.

Plan: Four puzzle pieces partitioned by a shared cross with one broad circular interlock; bounds (6,6)-(42,42).
Construction: Lucide puzzle: circular tab interrupted seam; four piece topology retained.
Reduction: Four seam tabs reduced to one broad tab to keep each opening at SOLO48 clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cab69194-7d72-4ec5-92ef-c43974df941f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/07-cab69194-7d72-4ec5-92ef-c43974df941f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'four-piece-jigsaw-puzzle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('four', 'piece', 'jigsaw', 'puzzle')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        poly('frame',(6,6),(20,6),(42,6),(42,30),(42,42),(20,42),(6,42),(6,30),closed=True)
        path('vertical',(20,6),[('L',(20,14)),('A',(20,22),4,4,True),('L',(20,30)),('L',(20,42))])
        poly('horizontal',(6,30),(20,30),(42,30))
        join('frame','vertical');join('frame','horizontal');join('vertical','horizontal')
