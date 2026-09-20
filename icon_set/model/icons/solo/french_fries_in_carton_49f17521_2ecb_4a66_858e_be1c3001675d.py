"""French Fries in Carton.

Plan: Three outlined fries meet the carton rim with exact shared nodes; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Fries reduced to single thick strokes; carton cutout uses a shallow faceted curve and three heights remain.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49f17521-2ecb-4a66-858e-be1c3001675d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/09-49f17521-2ecb-4a66-858e-be1c3001675d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'french-fries-in-carton'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('french', 'fries', 'in', 'carton')

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
        poly('carton',(8,24),(16,28),(24,30),(32,28),(40,24),(40,44),(8,44),closed=True)
        line('fry-left',(16,28),(16,9));line('fry-middle',(24,30),(24,4));line('fry-right',(32,28),(32,12))
        for part in ('fry-left','fry-middle','fry-right'):join('carton',part)
