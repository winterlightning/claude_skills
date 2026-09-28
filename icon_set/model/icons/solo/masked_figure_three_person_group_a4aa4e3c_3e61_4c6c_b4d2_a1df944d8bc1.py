"""Group with Masked Leader.

Plan: Closed balaclava with eye slot above three matched people; bounds (8,4)-(40,44).
Construction: Shared human user.svg: circular group heads and smooth shoulders; head radius2 bottom34, shoulder42 gives exact4 ink gap.
Reduction: Closed mask retained with a single eye slot; fine drapes and lower facial details omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4aa4e3c-3e61-4c6c-b4d2-a1df944d8bc1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/44-a4aa4e3c-3e61-4c6c-b4d2-a1df944d8bc1.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'masked-figure-three-person-group'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('masked', 'figure', 'three', 'person', 'group')

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
        path('mask',(14,13),[('A',(34,13),10,9,True),('A',(14,13),10,9,True)],True)
        line('eye-slot',(23,13),(25,13))
        for j,x in enumerate((10,24,38)):circle(f'head-{j}',x,32,2)
        path('crowd',(8,44),[('C',(10,42),(8,43),(9,42)),('C',(17,44),(13,42),(15,44)),('C',(24,42),(19,44),(21,42)),('C',(31,44),(27,42),(29,44)),('C',(38,42),(33,44),(35,42)),('C',(40,44),(39,42),(40,43))])
