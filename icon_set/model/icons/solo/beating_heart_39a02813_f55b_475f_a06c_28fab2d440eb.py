"""Beating Heart Symbol.

Plan: Heart below three short detached beat rays. Extremes6,6,42,42.
Construction: Lucide heart original/atomic-debug: paired lobes and coherent descending sides.
Reduction: Three shortened beat rays preserve motion; enlarged clearance from lobes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39a02813-f55b-475f-a06c-28fab2d440eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/33-39a02813-f55b-475f-a06c-28fab2d440eb.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'beating-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('beating', 'heart')

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
        path('heart',(26,24),[('C',(42,27),(33,13),(42,19)),('C',(26,42),(42,34),(32,38)),('C',(10,27),(20,38),(10,34)),('C',(26,24),(10,19),(19,13))],True)
        for n,(a,b) in enumerate([((6,13),(7,14)),((13,6),(14,7)),((23,6),(23,7))]):line(f'beat-{n}',a,b)
