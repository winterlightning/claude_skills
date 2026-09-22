"""A dashboard with a full-width header, tall left pane and two stacked right panes. HRECT_L gives each pane measurable space. Source defines the four-panel arrangement; Lucide panels-top-left supplies rounded shell and connected dividers. All receiving contours split at actual nodes. No detached symbol: divisions are intrinsic."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ccb75c3d-d503-467f-95c7-2c3351e3080c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/panel_ccb75c3d-d503-467f-95c7-2c3351e3080c.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'four-panel-dashboard-layout'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Four-Panel Dashboard Layout',)
    keywords = ('dashboard', 'layout', 'panels', 'interface', 'window', 'sections')
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
        path('frame',(8,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,18)),('L',(44,29)),('L',(44,36)),('A',(40,40),4,4,True),('L',(20,40)),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,18)),('L',(4,12)),('A',(8,8),4,4,True)],True)
        poly('header',(4,18),(20,18),(44,18))
        poly('sidebar',(20,18),(20,29),(20,40))
        line('right-split',(20,29),(44,29))
        for a,b in [('frame','header'),('frame','sidebar'),('frame','right-split'),('header','sidebar'),('sidebar','right-split')]: join(a,b)
