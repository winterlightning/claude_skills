"""Small Pointed Beard.

Plan: Rounded beard/fur patch with three broad lower pointed tufts; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Fine strand breaks omitted; broad rounded top and pointed tufts retain the fur/beard reading.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa621030-12a4-43cf-8621-6f23cc435296'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/26-fa621030-12a4-43cf-8621-6f23cc435296.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'pointed-shaggy-fur-patch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('pointed', 'shaggy', 'fur', 'patch')

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
        path('beard',(8,20),[('C',(20,4),(8,10),(12,4)),('L',(34,4)),('A',(40,10),6,6,True),('L',(40,30)),('L',(33,36)),('L',(29,32)),('L',(24,44)),('L',(17,33)),('L',(10,38)),('L',(8,20))],True)
