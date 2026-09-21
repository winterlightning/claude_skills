"""Microchip with Twelve Pins
Plan: Square chip, nested core and three pins per side, shared axes
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide cpu, repeated edge pins.
Reduction: Keep twelve pins; central core widened."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d1a5aae-34f3-4ba1-98c6-b575f90d433a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/semiconductor_5d1a5aae-34f3-4ba1-98c6-b575f90d433a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'microchip-with-twelve-pins'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('chip', 'microchip', 'semiconductor', 'processor', 'electronics', 'circuit')

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
        rect('body',10,10,28,28,2)
        rect('core',19,19,10,10)
        for i,v in enumerate((16,24,32)):
            for side,a,b in [('top',(v,6),(v,10)),('bottom',(v,38),(v,42)),('left',(6,v),(10,v)),('right',(38,v),(42,v))]:
                name=f'{side}-{i}';self.add_line(name,a,b);self.relate('connect',name,'body')
