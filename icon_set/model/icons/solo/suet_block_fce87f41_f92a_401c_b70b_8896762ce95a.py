"""Suet Block with Seeds.

Plan: Three-quarter suet block with upper diamond face and two seed dots on the lower face; bounds (6,6)-(42,42).
Construction: Lucide box: shared three-quarter face corners, with sparse seed texture from source.
Reduction: Rounded corners simplified and fine seed scatter reduced to two larger dots on the lower face.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fce87f41-f92a-401c-b70b-8896762ce95a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/47-fce87f41-f92a-401c-b70b-8896762ce95a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'suet-block'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('suet', 'block')

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
        poly('block',(6,16),(24,6),(42,16),(42,32),(24,42),(6,32),closed=True)
        poly('top-edge',(6,16),(24,22),(42,16));join('block','top-edge')
        self.add_dot('seed-left',(20,30));self.add_dot('seed-right',(28,30))
