"""Foot Acupuncture Therapy.

Plan: Foot silhouette on left with three needles entering from right at evenly spaced y; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Toes reduced to broad rounded toe profile; needle heads use round stroke caps rather than tiny rings.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f03cca0a-0e3a-4528-a0f0-17a4b8398df9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/04-f03cca0a-0e3a-4528-a0f0-17a4b8398df9.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'foot-three-acupuncture-needles'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('foot', 'three', 'acupuncture', 'needles')

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
        path('foot',(28,16),[('L',(28,11)),('A',(22,11),3,3,False),('A',(8,11),7,7,False),('L',(8,36)),('A',(16,44),8,8,False),('L',(24,44)),('A',(28,40),4,4,False)])
        for j,y in enumerate((16,28,40)):
         line(f'needle-{j}',(24,y),(40,y))
        self.add_dot('needle-head-0',(40,16));self.add_dot('needle-head-1',(40,28));self.add_dot('needle-head-2',(40,40))
        join('foot','needle-0');join('foot','needle-2')
        for j in range(3):join(f'needle-{j}',f'needle-head-{j}')
