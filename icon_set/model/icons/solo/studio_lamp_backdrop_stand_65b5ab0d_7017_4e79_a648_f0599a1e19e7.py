"""Studio Lamp and Backdrop Stand
Plan: Studio lamp and backdrop as a physical equipment group; two separate stands.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Crossbar thickness and small rear housing omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65b5ab0d-7017-4e79-a648-f0599a1e19e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/photography equipment lights background_65b5ab0d-7017-4e79-a648-f0599a1e19e7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'studio-lamp-backdrop-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('studio', 'light', 'tripod', 'backdrop', 'photography', 'equipment')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        poly('backdrop',(12,6),(38,6),(38,34),(38,42));poly('backdrop-feet',(30,42),(38,34),(42,42));join('backdrop','backdrop-feet')
        path('lamp',(22,17),[('L',(22,31)),('L',(16,31)),('A',(16,17),7,7,True),('L',(22,17))],True)
        poly('stand',(16,31),(16,36),(16,42));poly('feet',(6,42),(16,36),(22,42));join('stand','feet');join('stand','lamp')
