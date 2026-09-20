"""Cute Cartoon Dinosaur Character.

Plan: Cute left-facing dinosaur silhouette with long snout, belly, feet and rising tail. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: One arm and merged feet keep the squat silhouette clear; preserve snout and upright tail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd9d90b5-f0db-46ab-be17-4c36fa3593a7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/42-bd9d90b5-f0db-46ab-be17-4c36fa3593a7.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'cute-dinosaur-character'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cute', 'dinosaur', 'character')

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
        path('dinosaur',(6,18),[('A',(12,12),6,6,True),('L',(18,12)),('A',(26,6),8,6,True),('A',(34,14),8,8,True),('L',(34,25)),('C',(42,22),(38,28),(40,27)),('L',(42,34)),('C',(34,42),(42,39),(38,42)),('L',(15,42)),('L',(17,34)),('L',(20,30)),('L',(20,25)),('L',(12,25)),('A',(6,19),6,6,True),('L',(6,18))],True)
        self.add_dot('eye',(25,16))
        path('arm',(34,25),[('C',(28,34),(34,32),(32,34))]);join('dinosaur','arm')
