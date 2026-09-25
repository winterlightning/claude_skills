"""Soaring Glider Plane.

Plan: Banking glider with diagonal capsule fuselage and two exposed wings above a curved air trail; bounds (8,4)-(40,44).
Construction: Lucide plane: distinct fuselage with wings occluded at true shared body nodes; rounded nose and tail.
Reduction: Two trails reduced to one broad curve; glider body remains outlined. Initial stroke-only candidate retained for comparison.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4fcb649-0d89-4829-aa18-5a06211d7de9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/02-a4fcb649-0d89-4829-aa18-5a06211d7de9.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'banking-glider-with-air-trails'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('banking', 'glider', 'with', 'air', 'trails')

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
        path('fuselage',(11,20),[('L',(19,14)),('L',(31,5)),('A',(37,13),5,5,True),('L',(29,19)),('L',(17,28)),('A',(11,20),5,5,True)],True)
        line('wing-upper',(8,8),(19,14));line('wing-lower',(29,19),(40,25));join('fuselage','wing-upper');join('fuselage','wing-lower')
        path('air-trail',(8,44),[('C',(28,38),(16,44),(24,42))])
