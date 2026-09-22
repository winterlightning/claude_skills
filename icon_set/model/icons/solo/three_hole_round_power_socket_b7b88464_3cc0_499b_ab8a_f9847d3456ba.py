"""A Type K round socket face with paired pin holes and a flat-topped grounding hole. Circle keyshape gives the socket face full room; redundant outer wall plate omitted. Source defines hole arrangement; Lucide plug previously inspected for paired terminals. Pin circles derive from mirrored x positions and shared radius."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7b88464-3cc0-499b-ab8a-f9847d3456ba'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/power outlet type k_b7b88464-3cc0-499b-ab8a-f9847d3456ba.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'three-hole-round-power-socket'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Three-Hole Round Power Socket',)
    keywords = ('socket', 'outlet', 'electrical', 'power', 'plug', 'wall')
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
        circle('socket',24,24,20)
        for x in (18,30): circle(f'pin-{x}',x,17,2)
        path('ground',(20,28),[('L',(28,28)),('A',(20,28),4,7,True)],True)
