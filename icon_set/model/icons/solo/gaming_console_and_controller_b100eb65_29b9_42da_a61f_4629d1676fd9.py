"""Gaming Console and Controller.

Plan: Upright console occluded by a larger rounded gamepad; source side preserved. Extremes6,6,42,42.
Construction: Lucide gamepad-2 original/atomic-debug: two rounded grips and recessed lower edge.
Reduction: Enlarge controller for clear paired controls; omit console microcontrols and disc seam, preserve console silhouette and original overlap side.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b100eb65-29b9-42da-a61f-4629d1676fd9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/08-b100eb65-29b9-42da-a61f-4629d1676fd9.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gaming-console-and-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('gaming', 'console', 'and', 'controller')

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
        x=lambda v:24+1*(v-24)
        path('console',(x(14),42),[('L',(x(6),42)),('L',(x(6),10)),('A',(x(10),6),4,4,True),('L',(x(29),6)),('A',(x(33),10),4,4,True),('L',(x(33),20))])
        path('pad',(x(14),42),[('L',(x(14),29)),('A',(x(23),20),9,9,True),('L',(x(33),20)),('A',(x(42),29),9,9,True),('L',(x(42),42)),('L',(x(33),38)),('L',(x(23),38)),('L',(x(14),42))],True);join('console','pad')
        for x0 in (23,33):self.add_dot(f'button-{x0}',(x(x0),29))
