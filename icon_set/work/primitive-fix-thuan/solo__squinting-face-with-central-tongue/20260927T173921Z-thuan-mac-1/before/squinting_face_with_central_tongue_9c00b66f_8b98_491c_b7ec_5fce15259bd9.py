"""Squinting Face with Tongue.

Plan: Circular face with compact inward chevrons and broad tongue below smile; radius20 centered24.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Lower face rim opened where the tongue protrudes; Chevron eyes shortened; central tongue and full face retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c00b66f-8b98-491c-b7ec-5fce15259bd9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/17-9c00b66f-8b98-491c-b7ec-5fce15259bd9.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'squinting-face-with-central-tongue'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('squinting', 'face', 'with', 'central', 'tongue')

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
        self.add_arc('face',(8,36),(40,36),radius_x=20,radius_y=20,sweep=True,large_arc=True)
        poly('left-eye',(17,15),(20,17),(17,19));poly('right-eye',(31,15),(28,17),(31,19))
        path('smile',(14,27),[('C',(20,29),(16,29),(18,29)),('L',(28,29)),('C',(34,27),(30,29),(32,29))])
        path('tongue',(20,29),[('L',(20,40)),('A',(28,40),4,4,False),('L',(28,29))]);join('smile','tongue')
