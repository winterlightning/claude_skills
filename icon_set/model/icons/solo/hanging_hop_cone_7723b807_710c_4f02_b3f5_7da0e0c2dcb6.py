"""Brewing Hop Cone.

Plan: Hop cone x10..38, y4..44 with 3 tiers of overlapping scale arcs and a top stalk.
Construction: Lucide grape: grouped organic plant contours.
Reduction: Reduced dense scales to three broad tiers.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7723b807-710c-4f02-b3f5-7da0e0c2dcb6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/11-7723b807-710c-4f02-b3f5-7da0e0c2dcb6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hanging-hop-cone'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('hanging', 'hop', 'cone')

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
        line('stem',(24,4),(24,12))
        path('cone',(24,12),[('C',(38,24),(33,12),(38,17)),('C',(34,35),(38,28),(36,33)),('C',(24,44),(32,40),(28,42)),('C',(14,35),(20,42),(16,40)),('C',(10,24),(12,33),(10,28)),('C',(24,12),(10,17),(15,12))],True);join('stem','cone')
        path('scale-upper',(10,24),[('C',(24,12),(17,24),(22,20)),('C',(38,24),(26,20),(31,24))]);join('scale-upper','cone')
        path('scale-lower',(14,35),[('C',(24,26),(19,35),(23,30)),('C',(34,35),(25,30),(29,35))]);join('scale-lower','cone')
