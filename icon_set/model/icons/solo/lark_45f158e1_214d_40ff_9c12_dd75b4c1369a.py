"""Small Perched Songbird.

Plan: Perched lark with rounded head, attached wing, two legs and shared ground; bounds (6,6)-(42,42).
Construction: Lucide bird: round head, swept wing and true leg attachment nodes.
Reduction: Interior wing line omitted to keep the small bird silhouette clear; beak, tail, breast and legs retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45f158e1-214d-40ff-9c12-dd75b4c1369a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/24-45f158e1-214d-40ff-9c12-dd75b4c1369a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'lark'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('lark',)

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
        path('bird',(6,33),[('L',(25,12)),('C',(32,6),(25,8),(28,6)),('C',(37,10),(35,6),(36,8)),('L',(42,14)),('L',(36,18)),('C',(28,33),(36,27),(33,31)),('L',(20,34)),('L',(6,33))],True)
        line('leg-left',(20,34),(21,42));line('leg-right',(28,33),(31,42));join('bird','leg-left');join('bird','leg-right')
        poly('ground',(17,42),(21,42),(31,42),(36,42));join('ground','leg-left');join('ground','leg-right')
