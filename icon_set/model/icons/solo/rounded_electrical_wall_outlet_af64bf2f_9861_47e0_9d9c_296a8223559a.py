"""Rounded wall outlet with paired vertical slots and a horizontal ground. Square plate owns mirrored slots about x24. Source supplies slot arrangement; redundant inner socket border omitted for clearance. Lucide plug supplies rounded housing and paired parallel terminals."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'af64bf2f-9861-47e0-9d9c-296a8223559a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/outlet_af64bf2f-9861-47e0-9d9c-296a8223559a.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'rounded-electrical-wall-outlet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Rounded Electrical Wall Outlet',)
    keywords = ('outlet', 'socket', 'electrical', 'wall', 'power', 'plate')
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
        rect('plate',6,6,36,36,8)
        for x in (18,30): line(f'pin-{x}',(x,17),(x,23))
        line('ground',(22,32),(26,32))
