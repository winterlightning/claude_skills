"""A broad multimedia projector with a circular left lens and two right ventilation slits. HRECT_M is the broadest shallow available envelope. Source supplies front layout; Lucide projector supplies a circular lens and minimal vent mark. Housing owns lens and repeated vents; no incidental detail added."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd1642925-c41a-4fac-91c9-42439f1cbb77'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/projector_d1642925-c41a-4fac-91c9-42439f1cbb77.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'wide-multimedia-projector'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Wide Multimedia Projector',)
    keywords = ('projector', 'lens', 'multimedia', 'device', 'video', 'equipment')
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
        rect('housing',4,10,40,28,6)
        circle('lens',18,24,5)
        for y in (20,28): line(f'vent-{y}',(32,y),(35,y))
