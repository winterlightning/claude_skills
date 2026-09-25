"""Glass Jam Jar with Label.

Plan: Jam jar with broad cloth lid and centered blank label; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Cloth cover integrated with the lid; two broad scallops replace the fine cloth waves.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd71526a-9676-446c-9ea4-8ce656d6157e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/30-bd71526a-9676-446c-9ea4-8ce656d6157e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'jam-jar-with-cloth-cover'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('jam', 'jar', 'with', 'cloth', 'cover')

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
        path('jar',(8,15),[('L',(8,38)),('A',(14,44),6,6,False),('L',(34,44)),('A',(40,38),6,6,False),('L',(40,15))])
        path('cover',(8,15),[('L',(12,4)),('L',(36,4)),('L',(40,15)),('C',(24,15),(35,19),(29,11)),('C',(8,15),(19,19),(13,11))],True)
        join('jar','cover');rect('label',17,26,14,9,3)
