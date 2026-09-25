"""Fresh Fennel Bulb.

Plan: Fennel bulb with upright stalks and one sweeping layer; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Root hairs and repeated bulb layers omitted; three long stalks and one bulb-layer sweep retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96fcc65b-4232-4a6a-b39b-08253185e90f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/13-96fcc65b-4232-4a6a-b39b-08253185e90f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'fennel-bulb-with-stalks'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('fennel', 'bulb', 'with', 'stalks')

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
        path('bulb',(12,4),[('C',(14,24),(15,18),(15,19)),('C',(8,34),(9,29),(8,30)),('C',(24,44),(8,42),(16,44)),('C',(40,34),(32,44),(40,42)),('C',(34,24),(40,30),(39,29)),('C',(36,4),(33,19),(33,18))])
        path('center-stalk',(24,4),[('L',(24,22)),('C',(23,35),(24,29),(20,30))])
