"""Standing Gopher Rodent.

Plan: Upright plump rodent with circular ears, small face and two broad feet; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Curled forepaws omitted; ears, eyes, muzzle and broad separated feet retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5c54c96-084e-42b3-90da-b98178199c09'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/24-f5c54c96-084e-42b3-90da-b98178199c09.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'upright-round-eared-rodent'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('upright', 'round', 'eared', 'rodent')

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
        path('rodent',(12,36),[('C',(8,17),(8,30),(8,23)),('L',(8,9)),('A',(18,9),5,5,True),('L',(30,9)),('A',(40,9),5,5,True),('L',(40,17)),('C',(36,36),(40,23),(40,30)),('L',(40,44)),('L',(28,44)),('L',(24,39)),('L',(20,44)),('L',(8,44)),('L',(12,36))],True)
        self.add_dot('eye-left',(19,19));self.add_dot('eye-right',(29,19));line('muzzle',(24,27),(24,30))
