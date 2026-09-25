"""Hammer and Anvil.

Plan: Hammer above anvil; wide horn and recessed waist; bounds (6,6)-(42,42).
Construction: Lucide anvil: curved horn, flat striking surface, narrowed waist and wide foot.
Reduction: Hammer head simplified to rounded-stroke square; anvil seam omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13d6349e-4150-4e10-bcef-11ae7f9e36d7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/49-13d6349e-4150-4e10-bcef-11ae7f9e36d7.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hammer-above-anvil'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('hammer', 'above', 'anvil')

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
        poly('hammer',(30,6),(42,6),(42,16),(30,16),(30,11),closed=True)
        line('handle',(6,11),(30,11));join('hammer','handle')
        path('anvil',(6,25),[('L',(42,25)),('L',(42,33)),('L',(34,33)),('C',(34,42),(30,34),(30,41)),('L',(18,42)),('C',(18,33),(22,41),(22,34)),('C',(6,25),(10,33),(6,29))],True)
