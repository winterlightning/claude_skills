"""Spray Can with Mist.

Plan: Centerline6,6,42,42. Spray bottle at left, attached neck/pump and three separate mist strokes at right.
Construction: Lucide spray-can original/debug: physical nozzle with separate spray marks.
Reduction: Omitted the large mist-cloud outline; three spray rays retain the spraying action.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf258936-83aa-50c6-8b53-19bfd6e5ee83'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/36-bf258936-83aa-50c6-8b53-19bfd6e5ee83.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'spray-bottle-with-mist'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('spray', 'bottle', 'with', 'mist')

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
        path('bottle',(10,23),[('L',(18,23)),('A',(22,27),4,4,True),('L',(22,38)),('A',(18,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,27)),('A',(10,23),4,4,True)],True)
        poly('neck',(10,23),(10,14),(14,14),(18,14),(18,23));join('neck','bottle')
        poly('pump',(14,14),(14,6),(22,6));join('pump','neck')
        line('mist-upper',(32,6),(40,6));line('mist-middle',(32,17),(42,17));line('mist-lower',(32,28),(40,31))
