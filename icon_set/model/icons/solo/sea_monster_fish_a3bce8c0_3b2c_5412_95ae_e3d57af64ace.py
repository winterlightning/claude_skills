"""Aggressive Sea Monster Fish.

Plan: Fish monster single sweeping outline with dorsal fin and curled tail. Extremes 6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Simplify fin and curled tail into coherent curves; retain open jaw and tiny eye.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3bce8c0-3b2c-5412-95ae-e3d57af64ace'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/28-a3bce8c0-3b2c-5412-95ae-e3d57af64ace.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'sea-monster-fish'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('sea', 'monster', 'fish')

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
        path('fish',(6,10),[('C',(29,10),(14,4),(24,6)),('L',(38,6)),('L',(35,18)),('C',(31,25),(31,21),(29,22)),('C',(42,30),(36,31),(42,29)),('C',(37,42),(42,38),(42,42)),('C',(23,32),(30,42),(26,37)),('L',(15,42)),('L',(18,27)),('C',(6,24),(11,28),(6,27)),('L',(13,22)),('L',(6,10))],True)
        self.add_dot('eye',(20,16))
