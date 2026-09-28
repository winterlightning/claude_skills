"""Traditional Asian Teapot.

Plan: Centerline4,8,44,40. Squat vessel with overhead arch, broad left spout, right loop and centered pedestal.
Construction: No useful direct Lucide teapot match; source overhead arch and asymmetric spout/loop retained.
Reduction: Omitted tiny lid knob; vessel base simplified into the pedestal junction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f439bad7-bf84-59e6-9fdd-6df7d285d27a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__asian-teapot-overhead-handle/20260927T160834Z-thuan-mac-1/reference/asian food tea pot_f439bad7-bf84-59e6-9fdd-6df7d285d27a.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'asian-teapot-overhead-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('asian', 'teapot', 'overhead', 'handle')

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
        path('vessel',(14,21),[('L',(34,21)),('L',(34,30)),('A',(28,40),10,10,True),('L',(20,40)),('A',(14,30),10,10,True),('L',(14,21))],True)
        path('arch',(14,21),[('L',(14,18)),('A',(34,18),10,10,True),('L',(34,21))]);join('arch','vessel')
        poly('spout',(14,23),(4,18),(6,30),(14,32));join('spout','vessel')
        path('loop',(34,23),[('C',(44,25),(40,17),(44,20)),('C',(34,32),(44,32),(40,35))]);join('vessel','loop')
