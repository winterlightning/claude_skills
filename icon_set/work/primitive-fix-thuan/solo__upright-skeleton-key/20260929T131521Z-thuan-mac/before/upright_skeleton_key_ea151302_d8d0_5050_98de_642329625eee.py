"""Simple Skeleton Key.

Plan: Round skeleton-key bow with hole, solid shaft and two right teeth. Extremes10,4,38,44.
Construction: Lucide key-round original/atomic-debug: circular bow with sparse teeth.
Reduction: Shaft becomes a solid stroke; preserve round bow/hole and exactly two teeth.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea151302-d8d0-5050-98de-642329625eee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/47-ea151302-d8d0-5050-98de-642329625eee.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'upright-skeleton-key'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('upright', 'skeleton', 'key')

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
        path('bow',(22,4),[('A',(34,16),12,12,True),('A',(22,28),12,12,True),('A',(10,16),12,12,True),('A',(22,4),12,12,True)],True)
        circle('hole',22,16,3)
        poly('shaft',(22,28),(22,36),(22,44));join('bow','shaft')
        for y in (36,44):line(f'tooth-{y}',(22,y),(38,y));join('shaft',f'tooth-{y}')
