"""Bunch of Grapes.

Plan: Sixr3 grapes in a3/2/1 lattice at topy14,middley27,bottomy39; stem fork reaches6.
Construction: Lucide grape: repeated circular berries.
Reduction: Separated berry contours for spacing; all six hollow berries and stem retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '595ebb35-2692-477a-a87b-7507db3ad2a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/19-595ebb35-2692-477a-a87b-7507db3ad2a5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'six-grape-bunch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('six', 'grape', 'bunch')

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
        for j,(x,y) in enumerate(((9,14),(24,14),(39,14),(16,27),(32,27),(24,39))):circle(f'grape-{j}',x,y,3)
        path('stem',(24,11),[('C',(18,6),(24,8),(21,6))]);join('stem','grape-1')
        path('stem-right',(24,11),[('C',(30,6),(24,8),(27,6))]);join('stem-right','stem');join('stem-right','grape-1')
